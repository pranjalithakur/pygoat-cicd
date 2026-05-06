"""
File Handler Module - Ground Truth
This module demonstrates secure file handling practices.
"""
import os
from pathlib import Path


class FileHandler:
    """Secure file operations handler"""
    
    ALLOWED_EXTENSIONS = {'.txt', '.json', '.csv', '.log'}
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir).resolve()
        self.base_dir.mkdir(exist_ok=True)
    
    def validate_path(self, filename):
        """Validate file path to prevent directory traversal"""
        file_path = (self.base_dir / filename).resolve()
        
        if not str(file_path).startswith(str(self.base_dir)):
            raise ValueError("Invalid file path: directory traversal detected")
        
        return file_path
    
    def validate_extension(self, filename):
        """Validate file extension"""
        ext = Path(filename).suffix.lower()
        if ext not in self.ALLOWED_EXTENSIONS:
            raise ValueError(f"File extension {ext} not allowed")
        return True
    
    def read_file(self, filename):
        """Safely read a file"""
        file_path = self.validate_path(filename)
        self.validate_extension(filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write_file(self, filename, content):
        """Safely write to a file"""
        file_path = self.validate_path(filename)
        self.validate_extension(filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
