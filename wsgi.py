#!/usr/bin/env python
import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoctorX.settings')

# Load Django
import django
django.setup()

# Import WSGI application
from django.core.wsgi import get_wsgi_application

# Export the WSGI application
application = get_wsgi_application()
