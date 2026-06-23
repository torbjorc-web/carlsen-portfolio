from django.db import OperationalError, ProgrammingError
from django.shortcuts import render, get_object_or_404

from .models import Service


def service_list(request):
    try:
        services = list(Service.objects.all())
    except (OperationalError, ProgrammingError):
        services = []
    return render(request, 'services/service_list.html', {'services': services})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'services/service_detail.html', {'service': service})
