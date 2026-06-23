from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = models.TextField(blank=True)
    problem_it_solves = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    ideal_for = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
