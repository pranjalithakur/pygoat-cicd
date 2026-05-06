#!/bin/bash

# Project Memory Test Setup Script
# This script sets up the git repository and creates branches for testing

echo "🔧 Setting up Project Memory test environment..."

# Initialize git if not already done
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - PyGoat project"
else
    echo "✅ Git repository already exists"
fi

# Ensure we're on main branch
echo "🌿 Checking out main branch..."
git checkout -b main 2>/dev/null || git checkout main

# Add the baseline file to main
echo "📝 Adding baseline patterns to main branch..."
git add introduction/memory_test_main.py
git add PROJECT_MEMORY_TEST_GUIDE.md
git add QUICK_START.md

git commit -m "Add Project Memory baseline patterns

This establishes ground truth for Project Memory:
- Approved security patterns (Argon2, input sanitization)
- Educational vulnerabilities (intentional for training)
- Secure API endpoint examples"

echo "✅ Main branch setup complete!"
echo ""
echo "📋 Main branch now contains:"
echo "   - introduction/memory_test_main.py (baseline patterns)"
echo "   - PROJECT_MEMORY_TEST_GUIDE.md (full guide)"
echo "   - QUICK_START.md (quick reference)"
echo ""

# Create feature branch
echo "🌿 Creating feature branch..."
git checkout -b feature/test-project-memory

# Add the feature test file
echo "📝 Adding test patterns to feature branch..."
git add introduction/memory_test_feature.py

git commit -m "Add test patterns for Project Memory

New patterns to test Memory learning:
- Secure patterns matching approved baseline
- New educational demos (command injection, path traversal)
- Legacy issues (MD5 hash, hardcoded secrets)
- Real vulnerabilities (SQL injection, eval)
- Ambiguous cases (subprocess, pickle)"

echo "✅ Feature branch setup complete!"
echo ""
echo "📋 Feature branch now contains:"
echo "   - introduction/memory_test_feature.py (test patterns)"
echo ""

# Show the diff
echo "📊 Changes in feature branch:"
git diff main --stat

echo ""
echo "✅ Setup complete! Next steps:"
echo ""
echo "1. Push main branch:"
echo "   git push -u origin main"
echo ""
echo "2. Push feature branch:"
echo "   git push -u origin feature/test-project-memory"
echo ""
echo "3. Create a Pull Request on GitHub/GitLab:"
echo "   feature/test-project-memory → main"
echo ""
echo "4. Review Cursor's diff scan findings"
echo ""
echo "5. Provide feedback based on the scenarios in PROJECT_MEMORY_TEST_GUIDE.md"
echo ""
echo "6. Merge the PR to train Project Memory"
echo ""
echo "📖 For detailed instructions, see PROJECT_MEMORY_TEST_GUIDE.md"
