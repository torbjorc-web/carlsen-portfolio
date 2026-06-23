import os
import dj_database_url
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "carlsen-website.onrender.com",
    ".onrender.com",
]

DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()

SQLITE_FALLBACK = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if DATABASE_URL:
    try:
        DATABASES = {
            "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
        }
    except Exception:
        # Fall back safely for hobby deployments when DATABASE_URL is malformed.
        DATABASES = SQLITE_FALLBACK
else:
    DATABASES = SQLITE_FALLBACK
