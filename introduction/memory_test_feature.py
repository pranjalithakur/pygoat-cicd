"""
Feature Branch Test File for Project Memory Testing
This file contains NEW patterns to test if Project Memory learns from your feedback.
"""

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from argon2 import PasswordHasher
import hashlib
import pickle
import os
import subprocess


class NewFeatureSecure:
    """
    SCENARIO 1: These follow the same approved patterns from main branch.
    Project Memory should recognize these as safe since they match approved patterns.
    """
    
    def new_password_feature(self, password):
        """
        NEW FEATURE: Uses the same approved Argon2 pattern.
        Should NOT trigger warnings after Memory learns the pattern.
        """
        ph = PasswordHasher()
        hashed = ph.hash(password)
        return hashed
    
    def new_input_validation(self, user_data):
        """
        NEW FEATURE: Uses the same approved sanitization pattern.
        Should NOT trigger warnings - matches approved baseline.
        """
        import re
        sanitized = re.escape(user_data)
        return sanitized


class NewEducationalDemo:
    """
    SCENARIO 2: New educational vulnerabilities (intentional).
    When you DISMISS these findings, Memory should learn that:
    - Functions with 'educational_' or 'demo_' prefix are intentional
    - Classes with 'Educational' or 'Demo' in name are training content
    """
    
    def educational_command_injection(self, user_command):
        """
        INTENTIONAL: Command injection demo for training.
        This should be DISMISSED - it's educational content.
        """
        result = os.system(user_command)
        return result
    
    def demo_path_traversal(self, filename):
        """
        INTENTIONAL: Path traversal vulnerability demo.
        This should be DISMISSED - it's a training example.
        """
        file_path = f"../uploads/{filename}"
        with open(file_path, 'r') as f:
            return f.read()
    
    def educational_deserialization(self, data):
        """
        INTENTIONAL: Insecure deserialization for training.
        This should be DISMISSED as educational content.
        """
        obj = pickle.loads(data)
        return obj


class LegacyPatterns:
    """
    SCENARIO 3: Legacy code we're tracking but haven't fixed yet.
    When you mark these as "known issue", Memory should recognize
    this pattern in future scans and flag it as "known legacy issue".
    """
    
    def legacy_md5_hash(self, password):
        """
        KNOWN ISSUE: We know this uses weak MD5.
        Mark as "known issue" - we're tracking it but haven't migrated yet.
        """
        return hashlib.md5(password.encode()).hexdigest()
    
    def legacy_hardcoded_secret(self):
        """
        KNOWN ISSUE: Hardcoded credential - we're aware.
        Mark as "known issue" to track in Memory.
        """
        api_key = "sk_test_1234567890abcdef"
        return api_key


class ActualBugs:
    """
    SCENARIO 4: Real vulnerabilities that should be caught.
    These should be KEPT/FIXED - they are actual security issues.
    """
    
    def vulnerable_sql_query(self, request):
        """
        REAL BUG: SQL injection in production code.
        This should be caught and FIXED (not educational).
        """
        user_id = request.GET.get('id')
        # This is NOT in an educational class - it's a real bug
        query = f"SELECT * FROM production_users WHERE id = {user_id}"
        return query
    
    def vulnerable_file_read(self, request):
        """
        REAL BUG: Unrestricted file read vulnerability.
        This should be caught and FIXED.
        """
        filename = request.GET.get('file')
        # No validation - actual vulnerability
        with open(filename, 'r') as f:
            return f.read()
    
    def vulnerable_eval(self, user_code):
        """
        REAL BUG: Code injection via eval.
        This should be caught and FIXED.
        """
        result = eval(user_code)
        return result


def new_api_with_subprocess(request):
    """
    SCENARIO 5: Ambiguous case to test Memory learning.
    Uses subprocess which might be flagged, but could be legitimate.
    Your feedback will teach Memory how to handle this pattern.
    """
    command = request.GET.get('cmd', 'ls')
    # If you dismiss this, Memory learns subprocess usage in this context is OK
    # If you flag it, Memory learns to always warn about subprocess
    result = subprocess.run(command, shell=True, capture_output=True)
    return HttpResponse(result.stdout)


def new_feature_with_pickle(data_file):
    """
    SCENARIO 6: Pickle usage that might be flagged.
    Test if Memory learns your preference on pickle in this codebase.
    """
    with open(data_file, 'rb') as f:
        # Pickle is risky but might be acceptable in your internal tools
        obj = pickle.load(f)
    return obj
