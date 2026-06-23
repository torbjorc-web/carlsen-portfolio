from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import OperationalError, ProgrammingError
from django.shortcuts import render, redirect, get_object_or_404

from learning.models import LearningCredential
from portfolio.models import Project

from .forms import ContactForm
from .models import ContactMessage, LoginActivity


def home(request):
    try:
        latest_projects = list(
            Project.objects.filter(status='published').order_by('-published_at', '-id')[:3]
        )
        latest_credentials = list(
            LearningCredential.objects.order_by('-completed_at', '-id')[:3]
        )
    except (OperationalError, ProgrammingError):
        latest_projects = []
        latest_credentials = []

    return render(request, 'core/home.html', {
        'latest_projects': latest_projects,
        'latest_credentials': latest_credentials,
    })


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    selected_service_title = None
    form = None
    services_disabled = True  # Set to False when services are ready

    if request.method == 'POST':
        if services_disabled:
            # Don't process form if services are disabled
            return render(request, 'core/contact.html', {
                'services_disabled': services_disabled,
                'selected_service_title': selected_service_title,
            })
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        selected_service_title = request.POST.get('selected_service')
    else:
        selected_service_title = request.GET.get('service')
        if not services_disabled:
            initial = {}
            if selected_service_title:
                initial['selected_service'] = selected_service_title
            form = ContactForm(initial=initial)

    return render(request, 'core/contact.html', {
        'form': form,
        'selected_service_title': selected_service_title,
        'services_disabled': services_disabled,
    })


@login_required
@user_passes_test(lambda user: user.is_staff)
def dashboard(request):
    try:
        messages = ContactMessage.objects.order_by('-created_at')[:50]
        message_count = ContactMessage.objects.count()
        unread_count = ContactMessage.objects.filter(is_read=False).count()
        login_activities = LoginActivity.objects.select_related('user')[:15]
        unique_login_users = LoginActivity.objects.values('user').distinct().count()
    except (OperationalError, ProgrammingError):
        messages = []
        message_count = 0
        unread_count = 0
        login_activities = []
        unique_login_users = 0

    return render(request, 'dashboard.html', {
        'messages': messages,
        'message_count': message_count,
        'unread_count': unread_count,
        'login_activities': login_activities,
        'unique_login_users': unique_login_users,
    })


@login_required
@user_passes_test(lambda user: user.is_staff)
def message_detail(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)
    if not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'dashboard_message_detail.html', {
        'message': message,
    })


def under_construction(request, exception=None):
    return render(request, 'under_construction.html', status=404)
