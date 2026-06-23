from django.contrib import admin
from .models import SiteSettings, AboutProfile, ContactMessage, LoginActivity

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'homepage_title', 'email', 'location')

@admin.register(AboutProfile)
class AboutProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'selected_service', 'project_type', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'selected_service', 'project_type', 'message')

@admin.register(LoginActivity)
class LoginActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'ip_address', 'user_agent')
