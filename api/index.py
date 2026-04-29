import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoctorX.settings')

# Initialize Django
import django
django.setup()

# Import WSGI application
from django.core.wsgi import get_wsgi_application

# Export the WSGI application for Vercel
app = get_wsgi_application()

# Vercel serverless function handler
def handler(request):
    return app(request.environ, lambda status, headers: None)
