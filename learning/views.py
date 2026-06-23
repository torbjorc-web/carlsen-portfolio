from django.shortcuts import render
from .models import LearningCredential

def learning_list(request):
    credentials = LearningCredential.objects.prefetch_related('skill_areas').all()
    return render(request, 'learning/learning_list.html', {'credentials': credentials})
