# Quick Start - Project Memory Test

## TL;DR

### Main Branch - Add This File:
```
introduction/memory_test_main.py
```
Contains: Approved patterns and educational vulnerabilities

### Feature Branch - Add This File:
```
introduction/memory_test_feature.py
```
Contains: New patterns to test Memory learning

---

## Quick Commands

### 1. Setup Main Branch
```bash
git checkout main
git add introduction/memory_test_main.py
git commit -m "Add Project Memory baseline patterns"
git push origin main
```

### 2. Create Feature Branch
```bash
git checkout -b feature/test-project-memory
git add introduction/memory_test_feature.py
git commit -m "Add test patterns for Project Memory"
git push origin feature/test-project-memory
```

### 3. Create PR
- Create PR on GitHub: `feature/test-project-memory` → `main`
- Wait for Cursor diff scan

### 4. Provide Feedback on Findings

| Finding Type | Action | Why |
|--------------|--------|-----|
| `NewFeatureSecure` methods | ✅ DISMISS | Matches approved pattern |
| `educational_*` functions | ✅ DISMISS | Intentional for training |
| `legacy_*` functions | ⚠️ KNOWN ISSUE | Tracked tech debt |
| `vulnerable_*` in `ActualBugs` | 🚨 KEEP/FIX | Real vulnerabilities |
| `subprocess`, `pickle` usage | 🤔 YOUR CHOICE | Trains your preferences |

### 5. Merge PR
```bash
git checkout main
git merge feature/test-project-memory
git push origin main
```

### 6. Verify Learning
Create another PR with similar patterns and check if Memory learned!

---

## What Memory Should Learn

✅ Argon2 is approved  
✅ `educational_*` functions are intentional  
✅ Legacy MD5 is tracked  
🚨 Real SQL injection is bad  
🎯 Your subprocess/pickle preferences

---

See `PROJECT_MEMORY_TEST_GUIDE.md` for detailed explanation.
