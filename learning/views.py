from django.db import OperationalError, ProgrammingError
from django.shortcuts import render

from .models import LearningCredential


def learning_list(request):
    try:
        credentials = list(LearningCredential.objects.prefetch_related('skill_areas').all())
    except (OperationalError, ProgrammingError):
        credentials = []
    return render(request, 'learning/learning_list.html', {'credentials': credentials})
