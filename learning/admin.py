from django.contrib import admin
from .models import SkillArea, LearningCredential

@admin.register(SkillArea)
class SkillAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(LearningCredential)
class LearningCredentialAdmin(admin.ModelAdmin):
    list_display = ('title', 'credential_type', 'completed_at', 'provider', 'is_featured')
    list_filter = ('credential_type', 'provider', 'is_featured', 'skill_areas')
    search_fields = ('title', 'summary', 'skills_text', 'certificate_id')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('skill_areas',)
