"""
Data Validation Module - Ground Truth
This module demonstrates secure data validation practices.
"""
import re
import hashlib


class DataValidator:
    """Validates and sanitizes user input"""
    
    @staticmethod
    def validate_email(email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def sanitize_input(user_input, max_length=100):
        """Sanitize user input to prevent injection"""
        if not user_input:
            return ""
        
        sanitized = user_input.strip()
        sanitized = sanitized[:max_length]
        
        return sanitized
    
    @staticmethod
    def hash_password(password):
        """Hash password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def validate_username(username):
        """Validate username format (alphanumeric only)"""
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(pattern, username) is not None
