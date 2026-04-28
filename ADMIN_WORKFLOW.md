# Django Admin Workflow Instructions

## Overview
This system uses a RESTRICTED hybrid approach where:
- **Django Admin** (`/admin/`) - ONLY for superusers to create admin accounts
- **Custom Admin Dashboard** (`/accounts/dashboard/admin/`) - For daily clinic operations and creating other admins

## IMPORTANT SECURITY RESTRICTIONS

### Django Admin Access - SUPERUSER ONLY
- **Only superusers** can access Django Admin (`/admin/`)
- **Regular admins CANNOT** access Django Admin
- **Doctors and Patients CANNOT** access Django Admin
- **Only User and UserProfile models** are visible in Django Admin
- **Doctor, Appointment, and other models** are hidden from Django Admin

### Custom Admin Dashboard - REGULAR ADMINS
- **Admin users** login via `/accounts/login/` (same as other users)
- **Redirected to admin dashboard** based on their role
- **Can create other admins** via custom dashboard
- **Cannot access Django Admin**

## Setup Instructions

### 1. Create Superuser (First Time Setup)
```bash
python manage.py createsuperuser
```
- Create your main administrator account
- This account will have access to Django Admin at `/admin/`
- This is the ONLY account that can access Django Admin

### 2. Create Admin Users via Django Admin (Superuser Only)
1. **Superuser** logs into Django Admin: `http://127.0.0.1:8000/admin/`
2. Go to "Users" section
3. Click "Add user"
4. Create new admin user with:
   - Username
   - Email
   - Password
   - Set as "Staff status" = True
   - Set as "Superuser status" = False (for regular admins)

### 3. Create Admin User Profiles (Superuser Only)
1. In Django Admin, go to "User profiles" section
2. Click "Add user profile"
3. Select the admin user from dropdown
4. Set role to "Administrator"
5. Fill in any additional details

### 4. Create Additional Admins (Custom Dashboard)
Regular admins can create other admins through the custom dashboard:

1. **Admin** logs into custom dashboard: `http://127.0.0.1:8000/accounts/login/`
2. Navigate to "Admin Dashboard"
3. Click "Create New Admin"
4. Fill in admin details:
   - First Name, Last Name
   - Username (unique)
   - Email
   - Password + Confirm Password
5. Submit form
6. This creates:
   - Django User with staff status (for Django Admin access by superuser)
   - UserProfile with ADMIN role
   - Admin can login via `/accounts/login/`

### 5. Create Doctors (Two Methods)

#### Method A: Doctor Profile Only (No Login Access)
1. **Admin** logs into custom dashboard: `http://127.0.0.1:8000/accounts/login/`
2. Navigate to "Manage Doctors"
3. Fill in doctor details
4. **DO NOT** check "Create User Account for Doctor"
5. This creates a doctor profile but no login access

#### Method B: Doctor Profile + User Account (With Login Access)
1. **Admin** logs into custom dashboard: `http://127.0.0.1:8000/accounts/login/`
2. Navigate to "Manage Doctors"
3. Fill in doctor details
4. **CHECK** "Create User Account for Doctor"
5. Additional fields appear:
   - Username (for doctor login)
   - Password (temporary password)
   - License Number (medical license)
6. Submit form
7. This creates both doctor profile AND user account

## User Access

### Superuser (Django Admin)
- URL: `/admin/`
- Can create/manage all users
- Can access all Django models
- Used for system administration

### Administrators (Custom Dashboard)
- URL: `/accounts/login/`
- Can manage doctors
- Can view all appointments
- Can manage patient accounts
- Cannot access Django Admin (unless also superuser)

### Doctors (Custom Dashboard)
- URL: `/accounts/login/`
- Can view their own appointments
- Can manage patient appointments
- Can update their schedule
- Cannot access admin functions

### Patients (Custom Dashboard)
- URL: `/accounts/login/`
- Can book appointments
- Can view their own appointments
- Can manage their profile

## Workflow Summary

### Initial Setup (One-time)
1. Create superuser: `python manage.py createsuperuser`
2. Login to Django Admin (`/admin/`)
3. Create admin users via Django Admin
4. Create UserProfile records for admin users

### Daily Operations
1. Admins login to custom dashboard (`/accounts/login/`)
2. Admins create/manage doctors via custom dashboard
3. Doctors login to custom dashboard to manage appointments
4. Patients login to custom dashboard to book appointments

### User Creation Flow
```
Superuser (Django Admin) 
    creates Admin users
    creates User profiles for admins

Admin (Custom Dashboard)
    creates Doctor profiles
    creates Doctor user accounts (optional)

Doctors (Custom Dashboard)
    manage their appointments
    view patient details

Patients (Custom Dashboard)
    book appointments
    manage their bookings
```

## Important Notes

1. **Django Admin vs Custom Admin**: 
   - Django Admin: For system setup and user management
   - Custom Admin Dashboard: For daily clinic operations

2. **Doctor Account Creation**:
   - Option 1: Profile only (no login)
   - Option 2: Profile + user account (with login)

3. **Role Assignment**:
   - All users need UserProfile records with correct roles
   - Roles: PATIENT, DOCTOR, ADMIN

4. **Security**:
   - Superusers have full system access
   - Admins have clinic management access
   - Doctors have appointment management access
   - Patients have self-service access

## Troubleshooting

### "Admin privileges required" Error
- Ensure user has UserProfile with role='ADMIN'
- Check that user is logged in correctly

### "Doctor privileges required" Error
- Ensure doctor has UserProfile with role='DOCTOR'
- Ensure DoctorUser record exists linking user to doctor profile

### User cannot login
- Check if user exists in Django Admin
- Check if UserProfile exists with correct role
- For doctors, check if DoctorUser record exists
