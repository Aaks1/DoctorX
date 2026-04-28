# Vercel Deployment Guide - Piki Ora Medical Centre

This guide will help you deploy the Piki Ora Medical Centre appointment management system to Vercel.

## 🚀 Prerequisites

- GitHub repository with the code pushed
- Vercel account (free tier is sufficient)
- PostgreSQL database (Vercel provides free PostgreSQL)

## 📋 Step-by-Step Deployment

### 1. Connect Vercel to GitHub

1. Go to [vercel.com](https://vercel.com) and sign up/log in
2. Click **"Add New..."** → **"Project"**
3. **Import Git Repository**: Connect to your GitHub account
4. Select the `piki-ora-medical-centre` repository
5. Click **"Import"**

### 2. Configure Build Settings

Vercel will automatically detect Django. Configure the following:

**Build & Development Settings:**
- **Framework Preset**: Django
- **Root Directory**: `./`
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Output Directory**: `staticfiles`
- **Install Command**: `pip install -r requirements.txt`
- **Development Command**: `python manage.py runserver`

### 3. Environment Variables

Add the following environment variables in Vercel:

**Required Variables:**
```
DEBUG=False
SECRET_KEY=your-secret-key-here
DJANGO_SETTINGS_MODULE=DoctorX.settings
```

**Database Variables (Vercel PostgreSQL):**
```
DATABASE_URL=postgresql://username:password@host:port/database
```

**Optional Variables:**
```
ALLOWED_HOSTS=your-vercel-app-url.vercel.app
```

### 4. Database Setup

**Option A: Use Vercel PostgreSQL (Recommended)**
1. In Vercel dashboard, go to **"Storage"** → **"Create Database"**
2. Select **"PostgreSQL"**
3. Choose a name (e.g., `piki-ora-db`)
4. Copy the connection string
5. Add it to your environment variables as `DATABASE_URL`

**Option B: Use External Database**
- Set `DATABASE_URL` environment variable with your PostgreSQL connection string

### 5. Deploy the Application

1. Click **"Deploy"**
2. Wait for the deployment to complete
3. Your app will be available at a `.vercel.app` URL

### 6. Post-Deployment Setup

**Run Database Migrations:**
1. Go to Vercel dashboard → Your project → **"Functions"** tab
2. Click **"Add Function"** → **"Python Function"**
3. Create a migration function or use Vercel CLI locally:
   ```bash
   vercel env pull .env
   python manage.py migrate
   vercel env push
   ```

**Create Superuser:**
1. Use Vercel CLI or create a management command
2. Or create an admin user through the admin interface

## 🔧 Configuration Files

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "DoctorX/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "DoctorX/wsgi.py"
    }
  ],
  "env": {
    "DJANGO_SETTINGS_MODULE": "DoctorX.settings"
  }
}
```

### requirements.txt (Updated)
```
Django>=4.2.0,<5.0
Pillow>=10.0.0
python-decouple>=3.8
django-crispy-forms>=2.0
crispy-bootstrap5>=0.7
dj-database-url>=2.0.0
psycopg2-binary>=2.9.0
gunicorn>=20.1.0
whitenoise>=6.0.0
```

## 🌍 Access Your Application

After deployment, your application will be available at:
- **Main URL**: `https://your-app-name.vercel.app`
- **Admin URL**: `https://your-app-name.vercel.app/admin/`

## 🔍 Troubleshooting

### Common Issues

**1. Static Files Not Loading**
- Ensure `whitenoise` is in requirements.txt
- Check `STATIC_URL` and `STATICFILES_DIRS` settings
- Verify collectstatic command runs during build

**2. Database Connection Error**
- Verify `DATABASE_URL` environment variable
- Check PostgreSQL database is running
- Ensure `dj-database-url` is installed

**3. 500 Internal Server Error**
- Check Vercel function logs
- Verify all environment variables are set
- Ensure Django settings are production-ready

**4. Migration Issues**
- Run migrations manually using Vercel CLI
- Check database connection string
- Verify database permissions

### Debug Mode

For debugging, temporarily set:
```
DEBUG=True
```
in your environment variables, then redeploy.

## 📱 Testing the Deployment

1. **Home Page**: Visit your Vercel URL
2. **Registration**: Test user registration
3. **Login**: Test patient and admin login
4. **Booking**: Test appointment booking
5. **Admin Dashboard**: Test admin functionality

## 🔄 Continuous Deployment

Vercel automatically deploys when you push to GitHub:
- Push to `main` branch → Production deployment
- Push to other branches → Preview deployments

## 📊 Monitoring

- **Vercel Dashboard**: Monitor performance and errors
- **Logs**: View function logs and error messages
- **Analytics**: Track visitor statistics

## 🛡️ Security Notes

- **SECRET_KEY**: Use a strong, unique secret key
- **DEBUG**: Keep `DEBUG=False` in production
- **Database**: Use SSL connection strings
- **Environment Variables**: Never commit secrets to Git

## 📞 Support

For Vercel-specific issues:
- Check [Vercel Documentation](https://vercel.com/docs)
- Review Vercel function logs
- Test locally with Vercel CLI

For application issues:
- Review Django error logs
- Check database connectivity
- Verify environment variables

---

**Piki Ora Medical Centre**  
*Deployed on Vercel - Modern Healthcare Management*
