#!/usr/bin/env python
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoctorX.settings')

# Load Django
import django
django.setup()

# Import WSGI application
from django.core.wsgi import get_wsgi_application

# Export the WSGI application for Vercel
app = get_wsgi_application()

# Vercel expects the handler to be named 'handler' or 'application'
handler = app
application = app
