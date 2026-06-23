from django.db import models
from learning.models import LearningCredential
from services.models import Service


class Technology(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    client_type = models.CharField(max_length=120, blank=True)
    problem = models.TextField(blank=True)
    context = models.TextField(blank=True)
    goal = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    outcome = models.TextField(blank=True)
    lessons_learned = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    categories = models.ManyToManyField(ProjectCategory, blank=True)
    credentials = models.ManyToManyField(LearningCredential, related_name='projects', blank=True)
    services = models.ManyToManyField(Service, related_name='projects', blank=True)

    def __str__(self):
        return self.title