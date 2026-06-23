import os
import traceback

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# Use prod settings by default, can be overridden by environment variable.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.prod"))

# Hobby deployment helper: run migrations automatically on container startup.
if os.getenv("RUN_MIGRATIONS_ON_START", "1") == "1":
    try:
        call_command("migrate", interactive=False, run_syncdb=True, verbosity=1)
    except Exception as exc:
        print(f"[startup] migrate failed: {exc}")
        traceback.print_exc()

application = get_wsgi_application()
