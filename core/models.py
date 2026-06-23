from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default='Carlsen Data & Web Studio')
    homepage_title = models.CharField(max_length=120, default='Torbjørn Carlsen')
    tagline = models.CharField(max_length=180, default='Python, Django, Data Science, and AI Solutions')
    hero_title = models.CharField(max_length=180)
    hero_subtitle = models.TextField()
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    resume_url = models.URLField(blank=True)

    def __str__(self):
        return self.site_name

class AboutProfile(models.Model):
    full_name = models.CharField(max_length=120)
    short_bio = models.TextField()
    long_bio = models.TextField()
    consulting_focus = models.TextField(blank=True)
    background_summary = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    project_type = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.email}'
