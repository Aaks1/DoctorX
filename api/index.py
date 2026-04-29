#!/usr/bin/env python
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoctorX.settings')

try:
    # Load Django
    import django
    django.setup()
    
    # Import WSGI application
    from django.core.wsgi import get_wsgi_application
    
    # Export the WSGI application for Vercel
    application = get_wsgi_application()
    
except Exception as e:
    # Create a minimal WSGI app for error handling
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b"Django setup failed"]
