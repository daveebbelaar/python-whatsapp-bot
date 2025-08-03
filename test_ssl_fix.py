#!/usr/bin/env python3
"""
Test script for SSL certificate error handling.

This script tests the SSL error handling improvements made to address issue #35.
"""

import os
import sys
import requests
from unittest.mock import patch, MagicMock

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

def test_ssl_error_handling():
    """Test that SSL errors are properly handled."""
    
    # Create a simple Flask app for testing
    from flask import Flask
    app = Flask(__name__)
    
    # Mock the current_app configuration
    mock_config = {
        'ACCESS_TOKEN': 'test_token',
        'VERSION': 'v18.0',
        'PHONE_NUMBER_ID': 'test_phone_id',
        'VERIFY_SSL': True
    }
    
    with app.app_context():
        # Set the config
        app.config.update(mock_config)
        
        # Import the function after setting up context
        from app.utils.whatsapp_utils import send_message
        
        # Test with SSL error
        with patch('requests.post') as mock_post:
            mock_post.side_effect = requests.exceptions.SSLError("SSL certificate verification failed")
            
            result = send_message('{"test": "data"}')
            
            # Check that we get the expected error response
            assert isinstance(result, tuple)
            assert result[1] == 500
            assert "SSL certificate verification failed" in result[0].json["message"]
            
            print("✅ SSL error handling test passed!")
    
    # Test with SSL verification disabled
    mock_config['VERIFY_SSL'] = False
    
    with app.app_context():
        # Set the config
        app.config.update(mock_config)
        
        from app.utils.whatsapp_utils import send_message
        
        with patch('requests.post') as mock_post:
            mock_post.side_effect = requests.exceptions.SSLError("SSL certificate verification failed")
            
            result = send_message('{"test": "data"}')
            
            # Check that we get the expected error response for disabled SSL
            assert isinstance(result, tuple)
            assert result[1] == 500
            assert "even with SSL verification disabled" in result[0].json["message"]
            
            print("✅ SSL disabled error handling test passed!")

if __name__ == "__main__":
    print("Testing SSL certificate error handling...")
    test_ssl_error_handling()
    print("All tests passed! 🎉") 