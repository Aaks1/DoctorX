from django.contrib import admin
from .models import UserProfile, Doctor, AdminProfile

# Register models with default Django admin
admin.site.register(UserProfile)
admin.site.register(Doctor)
admin.site.register(AdminProfile)
