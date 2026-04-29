#!/usr/bin/env python
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoctorX.settings')

# Debug: Print current working directory and Python path
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path[:3]}")
print(f"Project root: {project_root}")
print(f"Django settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

try:
    # Load Django
    import django
    django.setup()
    print("Django setup successful")
    
    # Import WSGI application
    from django.core.wsgi import get_wsgi_application
    
    # Export the WSGI application for Vercel
    application = get_wsgi_application()
    print("WSGI application created successfully")
    
except Exception as e:
    print(f"Error during Django setup: {e}")
    print(f"Error type: {type(e)}")
    import traceback
    traceback.print_exc()
    # Create a minimal WSGI app for debugging
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [f"Django setup failed: {e}".encode()]
