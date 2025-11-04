#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Update sources.json entries from their remote config files.

.DESCRIPTION
    This script fetches each source's config.json from sourceUrl and updates the entry.
    It also auto-generates _feeds from repositoryUrl and adds _installUrl where missing.
    Optionally commits and pushes changes to git.

.PARAMETER Push
    If specified, automatically commits and pushes changes to git. Default: $false

.EXAMPLE
    .\update_sources_from_configs.ps1
    
.EXAMPLE
    .\update_sources_from_configs.ps1 -Push
#>

param(
    [switch]$Push = $false
)

$ErrorActionPreference = "Stop"

Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "🔄 Updating sources from their config files" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan

# Pull latest changes from git
Write-Host "`n📥 Pulling latest changes from git..." -ForegroundColor White
try {
    $pullOutput = git pull --rebase 2>&1
    Write-Host "   $pullOutput" -ForegroundColor Gray
}
catch {
    Write-Host "   ⚠️  Git pull failed: $_" -ForegroundColor Yellow
    Write-Host "   Continuing anyway..." -ForegroundColor Yellow
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
                    
                    # Check if property exists on source
                    $propertyExists = $source.PSObject.Properties.Name -contains $field
                    $sourceValue = if ($propertyExists) { $source.$field } else { $null }
                    
                    # Compare values (handle arrays/objects)
                    $valueChanged = $false
                    if ($null -eq $sourceValue -and $null -ne $configValue) {
                        $valueChanged = $true
                    }
                    elseif ($null -ne $sourceValue -and $null -ne $configValue) {
                        $configJson = $configValue | ConvertTo-Json -Depth 10 -Compress
                        $sourceJson = $sourceValue | ConvertTo-Json -Depth 10 -Compress
                        if ($configJson -ne $sourceJson) {
                            $valueChanged = $true
                        }
                    }
                    
                    if ($valueChanged) {
                        # Use Add-Member for new properties, direct assignment for existing
                        if (-not $propertyExists) {
                            $source | Add-Member -NotePropertyName $field -NotePropertyValue $configValue -Force
                        } else {
                            $source.$field = $configValue
                        }
                        $updatedFields += $field
                    }
                }
            }
            
            if ($updatedFields.Count -gt 0) {
                Write-Host "   📝 Updated: $($updatedFields -join ', ')" -ForegroundColor Cyan
                $updatedCount++
            }
            else {
                Write-Host "   ℹ️  No changes needed" -ForegroundColor Gray
            }
            
            # Add _installUrl if not present and sourceUrl is .json
            if (-not $source._installUrl -and $sourceUrl -match '\.json$') {
                $source | Add-Member -NotePropertyName "_installUrl" -NotePropertyValue $sourceUrl -Force
                Write-Host "   ➕ Added _installUrl" -ForegroundColor Green
                $updatedCount++
            }
        }
        
    }
    catch [System.Net.WebException] {
        $statusCode = [int]$_.Exception.Response.StatusCode
        if ($statusCode -eq 404) {
            Write-Host "   ❌ 404 Not Found" -ForegroundColor Red
            if ($source._tags -notcontains 'not-found') {
                $source._tags += 'not-found'
            }
            $errorCount++
        }
        else {
            Write-Host "   ⚠️  HTTP $statusCode" -ForegroundColor Yellow
            $errorCount++
        }
    }
    catch {
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
                commits  = "https://github.com/$owner/$repo/commits/$branch.atom"
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
                commits  = "https://gitlab.com/$owner/$repo/-/commits/master?format=atom"
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

# Save updated sources.json
Write-Host "`n💾 Saving sources.json..." -ForegroundColor White
$sources | ConvertTo-Json -Depth 100 | Set-Content $sourcesPath -Encoding UTF8
Write-Host "✅ sources.json saved successfully" -ForegroundColor Green

if ($Push) {
    # Check if there are any changes to commit
    Write-Host "`n🔍 Checking for changes..." -ForegroundColor White
    Push-Location (Join-Path $PSScriptRoot "..")
    $diffResult = git diff --quiet sources.json
    $hasChanges = $LASTEXITCODE -ne 0

    if ($hasChanges) {
        Write-Host "📝 Changes detected, committing..." -ForegroundColor Cyan
        
        # Stage sources.json
        try {
            git add sources.json
            Write-Host "   ✅ Changes staged" -ForegroundColor Green
        }
        catch {
            Write-Host "   ❌ Failed to stage changes: $_" -ForegroundColor Red
            Pop-Location
            exit 1
        }
        
        # Create commit message
        $commitMsg = "chore: Auto-update sources from configs`n`n"
        $commitMsg += "- Updated: $updatedCount sources`n"
        if ($errorCount -gt 0) {
            $commitMsg += "- Errors: $errorCount sources`n"
        }
        $commitMsg += "`nGenerated by update_sources_from_configs.ps1"
        
        # Commit changes
        try {
            git commit -m $commitMsg
            Write-Host "   ✅ Changes committed" -ForegroundColor Green
        }
        catch {
            Write-Host "   ❌ Failed to commit changes: $_" -ForegroundColor Red
            Pop-Location
            exit 1
        }
        
        # Push changes
        Write-Host "`n📤 Pushing changes to remote..." -ForegroundColor White
        try {
            $pushOutput = git push 2>&1
            Write-Host "   $pushOutput" -ForegroundColor Gray
            Write-Host "   ✅ Changes pushed successfully" -ForegroundColor Green
        }
        catch {
            Write-Host "   ❌ Failed to push changes: $_" -ForegroundColor Red
            Write-Host "   💡 You may need to pull and resolve conflicts manually" -ForegroundColor Yellow
            Pop-Location
            exit 1
        }
    }
    else {
        Write-Host "ℹ️  No changes to commit" -ForegroundColor Gray
    }

    Pop-Location
}
else {
    Write-Host "`n💡 Skipping git commit/push (use -Push flag to enable)" -ForegroundColor Yellow
}

Write-Host ""
exit 0
