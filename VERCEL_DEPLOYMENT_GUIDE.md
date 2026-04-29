# 🚀 Vercel Deployment Guide - Step by Step

## 📋 Prerequisites
- ✅ Neon database configured
- ✅ GitHub repository ready
- ✅ Vercel account (free at vercel.com)

---

## 🎯 Step 1: Go to Vercel

1. Open [vercel.com](https://vercel.com)
2. Click **"Sign Up"** or **"Log In"**
3. Connect your GitHub account when prompted

---

## 🎯 Step 2: Import Your Repository

1. Click **"Add New..."** → **"Project"**
2. Find your repository: `Aaks1/pakkiora`
3. Click **"Import"**

---

## 🎯 Step 3: Configure Project

### Basic Settings:
- **Project Name**: `doctorx-app` (or your preferred name)
- **Framework Preset**: **Other** (Django)
- **Root Directory**: `./` (leave default)

### Build & Development Settings:
- **Build Command**: Leave empty (handled by vercel.json)
- **Output Directory**: Leave empty
- **Install Command**: Leave empty (handled by vercel.json)

---

## 🎯 Step 4: Add Environment Variables

**CRITICAL**: Add these environment variables exactly as shown:

1. **DATABASE_URL**
   ```
   postgresql://neondb_owner:npg_T0YBXCPNQ3Hk@ep-misty-surf-a7k9k9ds-pooler.ap-southeast-2.aws.neon.tech/neondb?channel_binding=require&sslmode=require
   ```

2. **SECRET_KEY**
   ```
   g2du@2ryzje600cy*jujojp5tlf^f&9_4p2iu5c9@o&%t&#zhy
   ```

3. **ALLOWED_HOSTS**
   ```
   doctorx-app.vercel.app
   ```
   *(Replace with your actual project name)*

4. **DEBUG**
   ```
   False
   ```

5. **DJANGO_SETTINGS_MODULE**
   ```
   DoctorX.settings
   ```

---

## 🎯 Step 5: Deploy

1. Click **"Deploy"**
2. Wait for deployment (3-5 minutes)
3. Your app will be available at: `https://doctorx-app.vercel.app`

---

## 🔍 Troubleshooting

### If deployment fails:
1. Check the **Functions** and **Build** logs
2. Verify all environment variables are correct
3. Make sure your GitHub repo is up to date

### Common issues:
- **ALLOWED_HOSTS**: Must match your Vercel URL exactly
- **DATABASE_URL**: Copy entire string without spaces
- **Static files**: Should work automatically with vercel.json

---

## 🎉 Success!

Your DoctorX app is now live with:
- **Frontend**: Vercel hosting
- **Database**: Neon PostgreSQL
- **URL**: `https://your-project-name.vercel.app`

---

## 📱 Next Steps

1. **Test your app** - Create accounts, book appointments
2. **Monitor logs** - Check Vercel dashboard for any issues
3. **Custom domain** - Add custom domain if needed (free)

---

## 🔄 Making Updates

To update your app:
1. Push changes to GitHub
2. Vercel automatically redeploys
3. Your app updates live!

---

## 📁 Files Created/Modified

- `vercel.json` - Updated for proper Django deployment
- `api/index.py` - Vercel serverless function handler
- `.env` - Contains all necessary environment variables

---

**🎯 Your deployment architecture:**
```
Users → Vercel (Django App) → Neon (Database)
```

Ready to deploy! 🚀
