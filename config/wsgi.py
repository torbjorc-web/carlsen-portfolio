import os
from django.core.wsgi import get_wsgi_application

# Use prod settings by default, can be overridden by environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'config.settings.prod'))
application = get_wsgi_application()
