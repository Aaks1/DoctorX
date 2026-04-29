# 🗄️ Dual Database Setup for DoctorX (Neon + SQLite)

## Overview
Your Django project can use both databases:
- **SQLite**: For local development
- **Neon PostgreSQL**: For production/deployment

## Configuration

### Step 1: Update settings.py
```python
# Database Configuration - Environment based switching
import os
import dj_database_url

if os.environ.get('USE_NEON') == 'true':
    # Use Neon PostgreSQL for production
    DATABASES = {
        'default': dj_database_url.parse('postgresql://neondb_owner:npg_T0YBXCPNQ3Hk@ep-misty-surf-a7k9k9ds-pooler.ap-southeast-2.aws.neon.tech/neondb?channel_binding=require&sslmode=require')
    }
    print("🟢 Using Neon PostgreSQL Database")
else:
    # Use SQLite for development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    print("🔵 Using SQLite Database")
```

### Step 2: Create .env file
```bash
# .env
# For development (SQLite)
USE_NEON=false

# For production (Neon)
# USE_NEON=true
```

## Usage

### Local Development (SQLite)
```bash
# Default uses SQLite
python manage.py runserver
```

### Production/Deployment (Neon)
```bash
# Set environment variable to use Neon
set USE_NEON=true
python manage.py runserver
```

### Deployment on Vercel
In Vercel Environment Variables:
```
Name: USE_NEON
Value: true
```

## Database Operations

### Migrations
```bash
# SQLite migrations
python manage.py migrate

# Neon migrations
set USE_NEON=true
python manage.py migrate
```

### Create Superuser
```bash
# SQLite superuser
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@doctorx.com', 'admin123'); print('SQLite superuser created')"

# Neon superuser
set USE_NEON=true
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@doctorx.com', 'admin123'); print('Neon superuser created')"
```

## Benefits

### SQLite (Development)
✅ Fast and lightweight
✅ No internet connection required
✅ Easy to reset/delete
✅ Perfect for local testing

### Neon (Production)
✅ Cloud-based PostgreSQL
✅ Automatic backups
✅ Scalable
✅ Works with deployment platforms

## Testing Database Connection
```bash
# Test which database is active
python manage.py shell -c "from django.db import connection; print('Database:', connection.settings_dict['ENGINE']); print('Name:', connection.settings_dict.get('NAME', 'Neon'))"
```

## Switching Between Databases
```bash
# Switch to Neon
set USE_NEON=true
python manage.py runserver

# Switch to SQLite
set USE_NEON=false
python manage.py runserver
```

## Deployment Configuration

### Vercel Environment Variables
```
USE_NEON=true
DATABASE_URL=postgresql://neondb_owner:npg_T0YBXCPNQ3Hk@ep-misty-surf-a7k9k9ds-pooler.ap-southeast-2.aws.neon.tech/neondb?channel_binding=require&sslmode=require
SECRET_KEY=your-secret-key
DEBUG=false
```

### Docker (Optional)
```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    environment:
      - USE_NEON=true
    build: .
    ports:
      - "8000:8000"
```

## Default Superuser
Both databases will have:
- **Username**: admin
- **Password**: admin123
- **Email**: admin@doctorx.com

## Quick Commands
```bash
# Check current database
python manage.py shell -c "from django.db import connection; print('Current DB:', 'Neon' if 'neon' in str(connection.settings_dict.get('NAME', '')) else 'SQLite')"

# Create admin user in current DB
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@doctorx.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin user already exists')"

# Sync both databases
python manage.py migrate
set USE_NEON=true
python manage.py migrate
```

## 🚀 Ready to Use
Your DoctorX project now supports both databases seamlessly!
- Local development with SQLite
- Production deployment with Neon
