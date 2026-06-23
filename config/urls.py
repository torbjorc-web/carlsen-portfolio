from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('projects/', include('portfolio.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('learning/', include('learning.urls')),
    prefix_default_language=False,
)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]

handler404 = 'core.views.under_construction'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
