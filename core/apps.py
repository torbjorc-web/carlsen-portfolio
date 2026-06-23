from django.apps import AppConfig
from django.conf import settings


def create_default_admin(sender, **kwargs):
    if kwargs.get('raw', False):
        return

    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        username = 'admin'
        password = 'admin123'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email='', password=password)
    except Exception:
        pass


def record_login_activity(sender, user, request, **kwargs):
    try:
        from .models import LoginActivity
        ip_address = request.META.get('REMOTE_ADDR', '')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        LoginActivity.objects.create(
            user=user,
            ip_address=ip_address,
            user_agent=user_agent,
        )
    except Exception:
        pass


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        if settings.DEBUG:
            from django.db.models.signals import post_migrate
            post_migrate.connect(create_default_admin, sender=self, dispatch_uid='core.create_default_admin')

        from django.contrib.auth.signals import user_logged_in
        user_logged_in.connect(record_login_activity, dispatch_uid='core.record_login_activity')
