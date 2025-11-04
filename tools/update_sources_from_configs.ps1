#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Update sources.json entries from their remote config files.

.DESCRIPTION
    This script fetches each source's config.json from sourceUrl and updates the entry.
    It also auto-generates _feeds from repositoryUrl and adds _installUrl where missing.

.PARAMETER DryRun
    If specified, shows what would change without modifying sources.json

.EXAMPLE
    .\update_sources_from_configs.ps1
    
.EXAMPLE
    .\update_sources_from_configs.ps1 -DryRun
#>

param(
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "🔄 Updating sources from their config files" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan

if ($DryRun) {
    Write-Host "`n🔍 DRY RUN MODE - No changes will be saved" -ForegroundColor Yellow
}

# Load sources.json
Write-Host "`n📖 Loading sources.json..." -ForegroundColor White
$sourcesPath = Join-Path $PSScriptRoot "..\sources.json"
$sources = Get-Content $sourcesPath -Raw | ConvertFrom-Json

$total = $sources.Count
$updatedCount = 0
$errorCount = 0

# Process each source
for ($idx = 0; $idx -lt $total; $idx++) {
    $source = $sources[$idx]
    $sourceName = $source.name ?? "Unknown"
    
    Write-Host "`n$('─' * 60)" -ForegroundColor DarkGray
    Write-Host "📦 [$($idx + 1)/$total] $sourceName" -ForegroundColor White
    
    $sourceUrl = $source.sourceUrl
    if (-not $sourceUrl) {
        Write-Host "   ⚠️  No sourceUrl" -ForegroundColor Yellow
        continue
    }
    
    Write-Host "   URL: $sourceUrl" -ForegroundColor Gray
    
    # Initialize _tags if not present
    if (-not $source._tags) {
        $source | Add-Member -NotePropertyName "_tags" -NotePropertyValue @() -Force
    }
    
    # Remove 'not-found' tag (will re-add if still 404)
    $originalTags = $source._tags
    $source._tags = @($source._tags | Where-Object { $_ -ne 'not-found' })
    
    try {
        # Fetch the config
        $response = Invoke-WebRequest -Uri $sourceUrl -TimeoutSec 10 -ErrorAction Stop
        
        if ($response.StatusCode -eq 200) {
            Write-Host "   ✅ Config fetched" -ForegroundColor Green
            
            $config = $response.Content | ConvertFrom-Json
            
            # Fields to update from config
            $updateFields = @(
                'name', 'description', 'author', 'authorUrl',
                'platformUrl', 'scriptUrl', 'version', 'iconUrl',
                'scriptSignature', 'scriptPublicKey', 'packages',
                'allowEval', 'allowUrls', 'supportedClaimTypes',
                'authentication', 'settings', 'changelog', 'constants',
                'subscriptionRateLimit', 'primaryClaimFieldType'
            )
            
            $updatedFields = @()
            foreach ($field in $updateFields) {
                if ($config.PSObject.Properties.Name -contains $field) {
                    $configValue = $config.$field
                    $sourceValue = $source.$field
                    
                    # Compare values (handle arrays/objects)
                    $valueChanged = $false
                    if ($null -eq $sourceValue -and $null -ne $configValue) {
                        $valueChanged = $true
                    } elseif ($null -ne $sourceValue -and $null -ne $configValue) {
                        $configJson = $configValue | ConvertTo-Json -Depth 10 -Compress
                        $sourceJson = $sourceValue | ConvertTo-Json -Depth 10 -Compress
                        if ($configJson -ne $sourceJson) {
                            $valueChanged = $true
                        }
                    }
                    
                    if ($valueChanged) {
                        $source.$field = $configValue
                        $updatedFields += $field
                    }
                }
            }
            
            if ($updatedFields.Count -gt 0) {
                Write-Host "   📝 Updated: $($updatedFields -join ', ')" -ForegroundColor Cyan
                $updatedCount++
            } else {
                Write-Host "   ℹ️  No changes needed" -ForegroundColor Gray
            }
            
            # Add _installUrl if not present and sourceUrl is .json
            if (-not $source._installUrl -and $sourceUrl -match '\.json$') {
                $source | Add-Member -NotePropertyName "_installUrl" -NotePropertyValue $sourceUrl -Force
                Write-Host "   ➕ Added _installUrl" -ForegroundColor Green
                $updatedCount++
            }
        }
        
    } catch [System.Net.WebException] {
        $statusCode = [int]$_.Exception.Response.StatusCode
        if ($statusCode -eq 404) {
            Write-Host "   ❌ 404 Not Found" -ForegroundColor Red
            if ($source._tags -notcontains 'not-found') {
                $source._tags += 'not-found'
            }
            $errorCount++
        } else {
            Write-Host "   ⚠️  HTTP $statusCode" -ForegroundColor Yellow
            $errorCount++
        }
    } catch {
        Write-Host "   ❌ Error: $($_.Exception.Message)" -ForegroundColor Red
        $errorCount++
    }
    
    # Generate _feeds from repositoryUrl if not present
    $repoUrl = $source.repositoryUrl
    if ($repoUrl -and -not $source._feeds) {
        # Parse GitHub URLs
        if ($repoUrl -match 'https?://github\.com/([^/]+)/([^/]+)') {
            $owner = $Matches[1]
            $repo = $Matches[2].TrimEnd('/')
            $branch = 'main'  # Default to main
            
            $feeds = [PSCustomObject]@{
                commits = "https://github.com/$owner/$repo/commits/$branch.atom"
                releases = "https://github.com/$owner/$repo/releases.atom"
            }
            $source | Add-Member -NotePropertyName "_feeds" -NotePropertyValue $feeds -Force
            Write-Host "   ➕ Added _feeds for GitHub repo" -ForegroundColor Green
            $updatedCount++
        }
        # Parse GitLab URLs
        elseif ($repoUrl -match 'https?://gitlab\.com/([^/]+)/([^/]+)') {
            $owner = $Matches[1]
            $repo = $Matches[2].TrimEnd('/')
            
            $feeds = [PSCustomObject]@{
                commits = "https://gitlab.com/$owner/$repo/-/commits/master?format=atom"
                releases = "https://gitlab.com/$owner/$repo/-/releases.atom"
            }
            $source | Add-Member -NotePropertyName "_feeds" -NotePropertyValue $feeds -Force
            Write-Host "   ➕ Added _feeds for GitLab repo" -ForegroundColor Green
            $updatedCount++
        }
    }
}

# Summary
Write-Host "`n$('=' * 60)" -ForegroundColor Cyan
Write-Host "✅ Updated: $updatedCount sources" -ForegroundColor Green
Write-Host "❌ Errors: $errorCount sources" -ForegroundColor Red
Write-Host "=" * 60 -ForegroundColor Cyan

if (-not $DryRun) {
    # Save updated sources.json
    Write-Host "`n💾 Saving sources.json..." -ForegroundColor White
    $sources | ConvertTo-Json -Depth 100 | Set-Content $sourcesPath -Encoding UTF8
    Write-Host "✅ sources.json saved successfully" -ForegroundColor Green
} else {
    Write-Host "`n🔍 DRY RUN - No changes saved" -ForegroundColor Yellow
}

Write-Host ""
exit 0
