from django.contrib import admin
from .models import Appointment

# Hide models from Django Admin - they should only be managed via custom dashboard
class HiddenModelAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False  # Hide from non-superusers
    
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_add_permission(self, request):
        return False  # Prevent adding through Django Admin
    
    def has_change_permission(self, request, obj=None):
        return False  # Prevent editing through Django Admin
    
    def has_delete_permission(self, request, obj=None):
        return False  # Prevent deleting through Django Admin

# Register models as hidden (only superusers can see them)
admin.site.register(Appointment, HiddenModelAdmin)
