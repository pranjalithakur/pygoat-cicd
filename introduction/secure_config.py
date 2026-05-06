"""
Secure Configuration Module - Ground Truth
This module demonstrates secure configuration management practices.
"""
import os
from pathlib import Path


class SecureConfig:
    """Secure configuration handler using environment variables"""
    
    def __init__(self):
        self.api_key = os.getenv('API_KEY', '')
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///secure.db')
        self.secret_key = os.getenv('SECRET_KEY', '')
    
    def validate(self):
        """Validate that required secrets are set"""
        if not self.api_key:
            raise ValueError("API_KEY environment variable not set")
        if not self.secret_key:
            raise ValueError("SECRET_KEY environment variable not set")
        return True
    
    def get_api_key(self):
        """Retrieve API key from environment"""
        return self.api_key
    
    def get_database_url(self):
        """Retrieve database URL from environment"""
        return self.database_url
