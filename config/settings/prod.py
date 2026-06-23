import os

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

from .base import *

DEBUG = False
ALLOWED_HOSTS = [host for host in os.environ.get('ALLOWED_HOSTS', '*').split(',') if host]

# Require a strong SECRET_KEY from environment in production.
if not SECRET_KEY or SECRET_KEY.startswith('django-insecure-') or len(set(SECRET_KEY)) < 5 or len(SECRET_KEY) < 50:
	raise ImproperlyConfigured('Set a strong SECRET_KEY environment variable for production.')

DATABASES = {
	'default': dj_database_url.config(
		default=os.getenv('DATABASE_URL', f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
		conn_max_age=600,
		ssl_require=bool(os.getenv('DATABASE_URL')),
	)
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Enable strict transport security for HTTPS deployments.
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', '31536000'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Respect X-Forwarded-Proto when running behind a reverse proxy.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
