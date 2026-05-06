"""
Ground Truth File for Project Memory Testing - MAIN BRANCH
This file establishes baseline security patterns that are APPROVED in this codebase.
"""

from django.http import HttpResponse
from django.shortcuts import render
from argon2 import PasswordHasher
import re
import hashlib


class ApprovedSecurityPatterns:
    """
    These are our APPROVED security patterns.
    Project Memory should learn these are acceptable.
    """
    
    def secure_password_hash(self, password):
        """
        APPROVED: We use Argon2 for password hashing.
        This is our standard and should NOT trigger warnings.
        """
        ph = PasswordHasher()
        return ph.hash(password)
    
    def sanitize_user_input(self, user_input):
        """
        APPROVED: Our standard input sanitization method.
        """
        sanitized = re.escape(user_input)
        return sanitized
    
    def safe_file_upload(self, filename):
        """
        APPROVED: Our file validation pattern.
        """
        allowed_extensions = ['.jpg', '.png', '.pdf']
        extension = filename[filename.rfind('.'):]
        if extension.lower() in allowed_extensions:
            return True
        return False


class EducationalExamples:
    """
    These are INTENTIONALLY VULNERABLE for educational purposes.
    PyGoat is a training platform - these vulnerabilities are the product.
    Project Memory should learn that functions with 'educational_' prefix
    or in this class are intentionally insecure.
    """
    
    def educational_xss_demo(self, request):
        """
        INTENTIONAL VULNERABILITY: XSS demonstration for training.
        This is NOT a bug - it's the product.
        """
        user_input = request.GET.get('input', '')
        # No sanitization - this is intentional for training
        html = f"<div>You entered: {user_input}</div>"
        return HttpResponse(html)
    
    def educational_sql_injection(self, user_id):
        """
        INTENTIONAL VULNERABILITY: SQL injection demo for training.
        This is NOT a bug - it's educational content.
        """
        query = f"SELECT * FROM users WHERE id = {user_id}"
        return query


def secure_api_endpoint(request):
    """
    APPROVED: This is how we handle API endpoints securely.
    Uses proper validation and error handling.
    """
    if request.method != 'POST':
        return HttpResponse('Method not allowed', status=405)
    
    data = request.POST.get('data', '')
    validated_data = re.escape(data)
    
    return HttpResponse(f'Processed: {validated_data}')
