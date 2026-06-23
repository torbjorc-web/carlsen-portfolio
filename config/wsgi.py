import os
import traceback

import django
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# Use prod settings by default, can be overridden by environment variable.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.prod"))

# Setup Django first
django.setup()

# Hobby deployment helper: run migrations automatically on container startup.
if os.getenv("RUN_MIGRATIONS_ON_START", "1") == "1":
    try:
        call_command("migrate", interactive=False, run_syncdb=True, verbosity=1)
    except Exception as exc:
        print(f"[startup] migrate failed: {exc}")
        traceback.print_exc()

# Optional emergency helper: reset/create admin without shell access.
if os.getenv("RESET_ADMIN_ON_START", "0") == "1":
    reset_username = os.getenv("RESET_ADMIN_USERNAME", "").strip()
    reset_password = os.getenv("RESET_ADMIN_PASSWORD", "")
    reset_email = os.getenv("RESET_ADMIN_EMAIL", "").strip()

    if reset_username and reset_password:
        try:
            User = get_user_model()
            user, created = User.objects.get_or_create(
                username=reset_username,
                defaults={
                    "email": reset_email,
                    "is_staff": True,
                    "is_superuser": True,
                    "is_active": True,
                },
            )
            user.email = reset_email or user.email
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
            user.set_password(reset_password)
            user.save()
            action = "created" if created else "updated"
            print(f"[startup] admin user {action}: {reset_username}")
        except Exception as exc:
            print(f"[startup] admin reset failed: {exc}")
            traceback.print_exc()
    else:
        print("[startup] admin reset skipped: RESET_ADMIN_USERNAME/RESET_ADMIN_PASSWORD missing")

application = get_wsgi_application()
