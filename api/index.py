#!/usr/bin/env python
import os
import sys
import traceback

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoctorX.settings')

# Vercel handler - must be at top level
def handler(environ, start_response):
    """Vercel serverless function handler"""
    try:
        # Import Django inside handler to avoid initialization issues
        import django
        from django.core.wsgi import get_wsgi_application
        
        # Setup Django if not already setup
        if not django.apps.apps.ready:
            django.setup()
        
        # Get the WSGI application
        wsgi_app = get_wsgi_application()
        
        # Call the WSGI application
        return wsgi_app(environ, start_response)
        
    except ImportError as e:
        # Handle import errors
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        error_msg = f"Import Error: {str(e)}"
        print(f"Vercel Handler Import Error: {error_msg}")
        return [error_msg.encode()]
        
    except Exception as e:
        # Handle all other errors with detailed logging
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        
        # Log the full error for debugging
        error_msg = f"Server Error: {str(e)}"
        traceback_str = traceback.format_exc()
        print(f"Vercel Handler Error: {error_msg}")
        print(f"Full traceback: {traceback_str}")
        
        return [error_msg.encode()]

# Alternative names for compatibility
app = handler
application = handler
