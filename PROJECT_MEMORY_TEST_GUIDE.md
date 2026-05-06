# Project Memory Testing Guide

This guide helps you test Cursor's Project Memory feature using the PyGoat codebase.

## Overview
Project Memory learns from your feedback on PR scans and adapts to your codebase patterns.

## Files Created
1. `introduction/memory_test_main.py` - Ground truth (add to main branch)
2. `introduction/memory_test_feature.py` - Test cases (add to feature branch)

---

## Step-by-Step Testing Process

### Phase 1: Setup Main Branch (Ground Truth)

```bash
# Ensure you're on main branch
git checkout main

# Stage only the main test file
git add introduction/memory_test_main.py

# Commit the ground truth
git commit -m "Add approved security patterns for Project Memory baseline

This file establishes:
- Approved security patterns (Argon2, input sanitization)
- Intentional educational vulnerabilities (XSS, SQLi demos)
- Secure API endpoint patterns

These are our ground truth patterns for Memory to learn from."

# Push to remote
git push origin main
```

**What's in main branch:**
- ✅ Approved security patterns (Argon2, sanitization)
- ✅ Educational vulnerabilities (intentionally insecure training examples)
- ✅ Secure API patterns

---

### Phase 2: Create Feature Branch with New Patterns

```bash
# Create and switch to feature branch
git checkout -b feature/test-project-memory

# Stage the feature test file
git add introduction/memory_test_feature.py

# Commit the test cases
git commit -m "Add new features and patterns to test Project Memory

New patterns added:
- Similar secure patterns matching approved baseline
- New educational demos (command injection, path traversal)
- Legacy code with known issues (MD5 hash, hardcoded secrets)
- Real vulnerabilities to catch (SQL injection, eval)
- Ambiguous cases (subprocess, pickle usage)

This PR will test how Project Memory learns from feedback."

# Push feature branch
git push origin feature/test-project-memory
```

**What's in feature branch:**
- 🆕 New secure code matching approved patterns
- 🎓 New educational vulnerabilities (intentional for training)
- ⚠️ Legacy issues (known technical debt)
- 🐛 Real bugs (actual vulnerabilities)
- ❓ Ambiguous cases (to train Memory on your preferences)

---

### Phase 3: Create Pull Request

1. Go to GitHub/GitLab
2. Create PR: `feature/test-project-memory` → `main`
3. Wait for Cursor's diff scan to complete
4. Review the findings

---

### Phase 4: Provide Feedback (This Trains Memory!)

When you see findings in the PR, provide feedback based on these scenarios:

#### SCENARIO 1: Approved Pattern Matches
**Findings on:**
- `NewFeatureSecure.new_password_feature()`
- `NewFeatureSecure.new_input_validation()`

**Action:** ✅ **DISMISS** or mark as "False Positive"
**Why:** These match the approved patterns from main branch
**Memory learns:** These patterns are safe in your codebase

---

#### SCENARIO 2: Educational/Demo Vulnerabilities
**Findings on:**
- `educational_command_injection()`
- `demo_path_traversal()`
- `educational_deserialization()`

**Action:** ✅ **DISMISS** with note "Educational content"
**Why:** PyGoat is a training platform - these are intentional
**Memory learns:** 
- Functions with `educational_` or `demo_` prefix are intentional
- Classes with "Educational" or "Demo" in name are training content

---

#### SCENARIO 3: Known Legacy Issues
**Findings on:**
- `legacy_md5_hash()`
- `legacy_hardcoded_secret()`

**Action:** ⚠️ **MARK AS RESOLVED** or "Known Issue"
**Why:** You're aware of these but haven't fixed them yet
**Memory learns:** These are tracked technical debt

---

#### SCENARIO 4: Real Bugs (Should Be Caught)
**Findings on:**
- `vulnerable_sql_query()`
- `vulnerable_file_read()`
- `vulnerable_eval()`

**Action:** 🚨 **KEEP** and fix them
**Why:** These are actual security vulnerabilities in non-educational code
**Memory learns:** These patterns should always be flagged

---

#### SCENARIO 5 & 6: Ambiguous Cases
**Findings on:**
- `new_api_with_subprocess()`
- `new_feature_with_pickle()`

**Action:** YOUR CHOICE - this trains Memory on your preferences
- If you DISMISS: Memory learns subprocess/pickle is OK in your context
- If you KEEP: Memory learns to always warn about these

---

### Phase 5: Merge the PR

```bash
# After providing all feedback, merge the PR
git checkout main
git merge feature/test-project-memory
git push origin main
```

**Important:** Memory learns AFTER the PR is merged!

---

### Phase 6: Verify Memory Learning (Create Second PR)

Create a second feature branch with similar patterns:

```bash
git checkout -b feature/verify-memory-learning

# Create a new file with similar patterns
cat > introduction/memory_verification.py << 'EOF'
"""Test if Project Memory learned from previous PR feedback"""

from argon2 import PasswordHasher
import pickle

class VerificationTests:
    def another_password_feature(self, pwd):
        # Should NOT be flagged - matches approved pattern
        ph = PasswordHasher()
        return ph.hash(pwd)
    
    def educational_xxe_demo(self, xml_data):
        # Should NOT be flagged - has 'educational_' prefix
        return xml_data  # Intentionally vulnerable
    
    def another_sql_injection(self, user_input):
        # SHOULD be flagged - real vulnerability, not educational
        query = f"SELECT * FROM users WHERE name = {user_input}"
        return query
EOF

git add introduction/memory_verification.py
git commit -m "Verify Project Memory learned patterns"
git push origin feature/verify-memory-learning
```

Create a PR and check:
- ✅ Approved patterns should have fewer/no warnings
- ✅ Educational functions should be recognized as intentional
- ⚠️ Real vulnerabilities should still be caught

---

## Expected Learning Outcomes

After completing this test, Project Memory should learn:

1. **Approved Patterns** ✅
   - Argon2 password hashing is your standard
   - `re.escape()` is your approved sanitization
   - These should not trigger false positives

2. **Educational Context** 🎓
   - Functions with `educational_` or `demo_` prefix are intentional
   - Classes with "Educational" in name are training content
   - These are not bugs - they're the product

3. **Legacy Technical Debt** ⚠️
   - MD5 usage is known and tracked
   - Hardcoded secrets are being migrated
   - These are acknowledged but not urgent

4. **Real Vulnerabilities** 🚨
   - SQL injection outside educational context is a bug
   - Unrestricted file access is dangerous
   - `eval()` usage should be flagged

5. **Your Preferences** 🎯
   - How you handle subprocess usage
   - Your stance on pickle in this codebase
   - Context-specific security decisions

---

## Troubleshooting

**Q: I don't see a diff scan on my PR**
A: Ensure Cursor is configured to scan PRs in your repository settings

**Q: Memory isn't learning my patterns**
A: Make sure you're providing feedback AND merging the PR. Memory only updates after merge.

**Q: Can I test this without creating real PRs?**
A: No - Project Memory specifically learns from PR review feedback and merge events

---

## Summary

**Main Branch:** `memory_test_main.py` (ground truth)
**Feature Branch:** `memory_test_feature.py` (test cases)

Provide feedback based on the 6 scenarios above, merge the PR, then verify Memory learned by creating a second PR with similar patterns.
