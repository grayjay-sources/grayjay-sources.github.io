#!/usr/bin/env python3
"""
Update sources.json entries from their remote config files.

This script:
- Pulls latest changes from git
- Fetches each source's config.json from sourceUrl
- Updates all fields that changed
- Tags unreachable sources with 'not-found'
- Auto-generates _feeds from repositoryUrl
- Adds _installUrl where missing
- Commits and pushes changes back to git
"""

import json
import requests
import re
import sys
import subprocess
from typing import Dict, Any, List

def update_source_from_config(source: Dict[str, Any]) -> tuple[bool, List[str]]:
    """
    Update a single source from its config URL.
    
    Returns:
        (changed, messages): Tuple of whether source was changed and list of log messages
    """
    messages = []
    changed = False
    
    source_url = source.get('sourceUrl')
    if not source_url:
        messages.append("⚠️  No sourceUrl")
        return changed, messages
    
    source_name = source.get('name', 'Unknown')
    messages.append(f"URL: {source_url}")
    
    # Initialize _tags if not present
    if '_tags' not in source:
        source['_tags'] = []
    
    # Remove 'not-found' tag (will re-add if still 404)
    original_tags = source['_tags'].copy()
    source['_tags'] = [tag for tag in source['_tags'] if tag != 'not-found']
    
    try:
        # Fetch the config
        response = requests.get(source_url, timeout=10)
        
        if response.status_code == 404:
            messages.append("❌ 404 Not Found")
            if 'not-found' not in source['_tags']:
                source['_tags'].append('not-found')
                changed = True
            return changed, messages
            
        if response.status_code != 200:
            messages.append(f"⚠️  HTTP {response.status_code}")
            return changed, messages
            
        config = response.json()
        messages.append("✅ Config fetched")
        
        # Fields to update from config (only if present in config)
        update_fields = [
            'name', 'description', 'author', 'authorUrl', 
            'platformUrl', 'scriptUrl', 'version', 'iconUrl',
            'scriptSignature', 'scriptPublicKey', 'packages',
            'allowEval', 'allowUrls', 'supportedClaimTypes',
            'authentication', 'settings', 'changelog', 'constants',
            'subscriptionRateLimit', 'primaryClaimFieldType'
        ]
        
        updated_fields = []
        for field in update_fields:
            if field in config:
                if source.get(field) != config[field]:
                    source[field] = config[field]
                    updated_fields.append(field)
                    changed = True
        
        if updated_fields:
            messages.append(f"📝 Updated: {', '.join(updated_fields)}")
        else:
            messages.append("ℹ️  No changes needed")
            
        # Add _installUrl if not present and sourceUrl is a .json file
        if '_installUrl' not in source and source_url.endswith('.json'):
            source['_installUrl'] = source_url
            messages.append("➕ Added _installUrl")
            changed = True
            
    except requests.exceptions.Timeout:
        messages.append("⏱️  Timeout")
    except requests.exceptions.RequestException as e:
        messages.append(f"❌ Error: {str(e)}")
    except json.JSONDecodeError:
        messages.append("❌ Invalid JSON")
    except Exception as e:
        messages.append(f"❌ Unexpected error: {str(e)}")
    
    # Check if tags actually changed
    if source['_tags'] != original_tags:
        changed = True
    
    return changed, messages


def generate_feeds_from_repo(source: Dict[str, Any]) -> tuple[bool, List[str]]:
    """
    Generate _feeds object from repositoryUrl if not present.
    
    Returns:
        (changed, messages): Tuple of whether source was changed and list of log messages
    """
    messages = []
    changed = False
    
    if '_feeds' in source:
        return changed, messages
        
    repo_url = source.get('repositoryUrl')
    if not repo_url:
        return changed, messages
    
    # Parse GitHub URLs
    github_match = re.match(r'https?://github\.com/([^/]+)/([^/]+)', repo_url)
    gitlab_match = re.match(r'https?://gitlab\.com/([^/]+)/([^/]+)', repo_url)
    
    if github_match:
        owner, repo = github_match.groups()
        repo = repo.rstrip('/')
        # Detect default branch (assume main, could be master)
        branch = 'main'
        source['_feeds'] = {
            'commits': f"https://github.com/{owner}/{repo}/commits/{branch}.atom",
            'releases': f"https://github.com/{owner}/{repo}/releases.atom"
        }
        messages.append("➕ Added _feeds for GitHub repo")
        changed = True
    elif gitlab_match:
        owner, repo = gitlab_match.groups()
        repo = repo.rstrip('/')
        source['_feeds'] = {
            'commits': f"https://gitlab.com/{owner}/{repo}/-/commits/master?format=atom",
            'releases': f"https://gitlab.com/{owner}/{repo}/-/releases.atom"
        }
        messages.append("➕ Added _feeds for GitLab repo")
        changed = True
    
    return changed, messages


def run_git_command(command: list, description: str) -> bool:
    """Run a git command and return success status."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            print(f"⚠️  {description} failed:")
            print(f"   {result.stderr.strip()}")
            return False
        if result.stdout.strip():
            print(f"   {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ {description} error: {str(e)}")
        return False


def main():
    print("="*60)
    print("🔄 Updating sources from their config files")
    print("="*60)
    
    # Pull latest changes from git
    print("\n📥 Pulling latest changes from git...")
    if not run_git_command(['git', 'pull', '--rebase'], 'Git pull'):
        print("⚠️  Warning: Git pull failed, continuing anyway...")
    
    # Load sources.json
    print("\n📖 Loading sources.json...")
    with open('sources.json', 'r', encoding='utf-8') as f:
        sources = json.load(f)
    
    total = len(sources)
    updated_count = 0
    error_count = 0
    
    # Process each source
    for idx, source in enumerate(sources):
        source_name = source.get('name', 'Unknown')
        print(f"\n{'─'*60}")
        print(f"📦 [{idx + 1}/{total}] {source_name}")
        
        # Update from config
        config_changed, config_messages = update_source_from_config(source)
        for msg in config_messages:
            print(f"   {msg}")
        
        # Generate feeds
        feeds_changed, feeds_messages = generate_feeds_from_repo(source)
        for msg in feeds_messages:
            print(f"   {msg}")
        
        # Track changes
        if config_changed or feeds_changed:
            updated_count += 1
        
        # Count errors (sources with 'not-found' tag or error messages)
        if 'not-found' in source.get('_tags', []):
            error_count += 1
        elif any('❌' in msg or '⚠️' in msg for msg in config_messages):
            error_count += 1
    
    # Save updated sources.json
    print(f"\n{'='*60}")
    print(f"✅ Updated: {updated_count} sources")
    print(f"❌ Errors: {error_count} sources")
    print(f"{'='*60}\n")
    
    print("💾 Saving sources.json...")
    with open('sources.json', 'w', encoding='utf-8') as f:
        json.dump(sources, f, indent=2, ensure_ascii=False)
    
    print("✅ sources.json saved successfully")
    
    # Check if there are any changes to commit
    print("\n🔍 Checking for changes...")
    result = subprocess.run(['git', 'diff', '--quiet', 'sources.json'], check=False)
    
    if result.returncode != 0:  # Changes detected
        print("📝 Changes detected, committing...")
        
        # Stage sources.json
        if not run_git_command(['git', 'add', 'sources.json'], 'Git add'):
            print("❌ Failed to stage changes")
            return 1
        
        # Create commit message
        commit_msg = f"chore: Auto-update sources from configs\n\n"
        commit_msg += f"- Updated: {updated_count} sources\n"
        if error_count > 0:
            commit_msg += f"- Errors: {error_count} sources\n"
        commit_msg += f"\nGenerated by update_sources_from_configs.py"
        
        # Commit changes
        if not run_git_command(['git', 'commit', '-m', commit_msg], 'Git commit'):
            print("❌ Failed to commit changes")
            return 1
        
        print("✅ Changes committed")
        
        # Push changes
        print("\n📤 Pushing changes to remote...")
        if not run_git_command(['git', 'push'], 'Git push'):
            print("❌ Failed to push changes")
            print("💡 You may need to pull and resolve conflicts manually")
            return 1
        
        print("✅ Changes pushed successfully")
    else:
        print("ℹ️  No changes to commit")
    
    # Exit with appropriate code
    if error_count > 0:
        print(f"\n⚠️  Completed with {error_count} errors")
        return 0  # Don't fail the workflow for fetch errors
    else:
        print("\n✅ All sources updated successfully")
        return 0


if __name__ == '__main__':
    sys.exit(main())
