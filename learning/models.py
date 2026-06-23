from django.db import models

class SkillArea(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class LearningCredential(models.Model):
    CREDENTIAL_TYPES = [
        ('career_path', 'Career Path'),
        ('skill_path', 'Skill Path'),
        ('course', 'Course'),
        ('professional_cert', 'Professional Certification'),
    ]
    title = models.CharField(max_length=255)
    provider = models.CharField(max_length=120, default='Codecademy')
    slug = models.SlugField(unique=True)
    credential_type = models.CharField(max_length=30, choices=CREDENTIAL_TYPES)
    summary = models.TextField(blank=True)
    completed_at = models.DateField(null=True, blank=True)
    certificate_id = models.CharField(max_length=50, blank=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_image = models.ImageField(upload_to='certificate_images/', blank=True, null=True)
    skills_text = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    skill_areas = models.ManyToManyField(SkillArea, related_name='credentials', blank=True)

    class Meta:
        ordering = ['order', '-completed_at', 'title']

    def __str__(self):
        return self.title
