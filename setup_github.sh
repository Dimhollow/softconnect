#!/bin/bash

# SoftConnect GitHub Setup Script
# This script helps you set up your GitHub repository

echo "🚀 SoftConnect GitHub Setup"
echo "================================"
echo ""

# Check if we're in the right directory
if [ ! -f "BRANDING.md" ]; then
    echo "❌ Error: Please run this script from the rustdesk repository root"
    exit 1
fi

# Ask for GitHub username
echo "📝 Please provide your GitHub details:"
read -p "GitHub username: " GITHUB_USER

if [ -z "$GITHUB_USER" ]; then
    echo "❌ GitHub username is required"
    exit 1
fi

# Ask for repository name
read -p "Repository name (default: softconnect): " REPO_NAME
REPO_NAME=${REPO_NAME:-softconnect}

echo ""
echo "📋 Summary:"
echo "   GitHub User: $GITHUB_USER"
echo "   Repository:  $REPO_NAME"
echo "   URL: https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""

read -p "Continue? (y/n): " CONFIRM
if [ "$CONFIRM" != "y" ]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo "================================"
echo ""

# Check if repository already exists on GitHub
echo "⚠️  IMPORTANT: Before continuing, please:"
echo "   1. Go to https://github.com/new"
echo "   2. Create a new repository named '$REPO_NAME'"
echo "   3. Make it Private or Public (your choice)"
echo "   4. DO NOT initialize with README, .gitignore, or license"
echo ""
read -p "Have you created the repository? (y/n): " CREATED
if [ "$CREATED" != "y" ]; then
    echo ""
    echo "Please create the repository first, then run this script again."
    exit 0
fi

echo ""
echo "🔗 Setting up git remote..."

# Remove old origin if exists
git remote remove origin 2>/dev/null

# Add new origin
git remote add origin "https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo "✓ Remote added"

# Push to GitHub
echo ""
echo "📤 Pushing code to GitHub..."
echo "   You may be prompted for your GitHub credentials"
echo ""

git push -u origin master

if [ $? -eq 0 ]; then
    echo ""
    echo "================================"
    echo "✅ Success!"
    echo ""
    echo "📦 Your repository is now live at:"
    echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
    echo ""
    echo "🔄 GitHub Actions should start building automatically"
    echo "   Check progress at:"
    echo "   https://github.com/$GITHUB_USER/$REPO_NAME/actions"
    echo ""
    echo "📥 Once builds complete, download installers from:"
    echo "   https://github.com/$GITHUB_USER/$REPO_NAME/releases"
    echo ""
else
    echo ""
    echo "❌ Push failed. Please check your GitHub credentials and try again."
    echo ""
    echo "Manual push command:"
    echo "   git push -u origin master"
    exit 1
fi
