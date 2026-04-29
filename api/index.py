#!/usr/bin/env python
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoctorX.settings')

# Import WSGI application
from django.core.wsgi import get_wsgi_application

# Get the WSGI application
wsgi_app = get_wsgi_application()

# Vercel handler - must be at top level
def handler(environ, start_response):
    """Vercel serverless function handler"""
    try:
        return wsgi_app(environ, start_response)
    except Exception as e:
        # Error handling for debugging
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [f"Error: {str(e)}".encode()]

# Alternative names for compatibility
app = handler
application = handler
