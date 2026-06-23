from django.contrib import admin
from .models import Technology, ProjectCategory, Project

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'published_at')
    list_filter = ('status', 'is_featured', 'categories', 'technologies')
    search_fields = ('title', 'short_description', 'problem', 'solution', 'outcome')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies', 'categories', 'credentials', 'services')
