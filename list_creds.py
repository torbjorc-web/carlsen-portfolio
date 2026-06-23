import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from learning.models import LearningCredential

print("📚 All credentials and their slugs:\n")
for cert in LearningCredential.objects.all().order_by('title'):
    pdf_status = "✅" if cert.certificate_file else "❌"
    print(f"{pdf_status} | {cert.slug:40} | {cert.title}")
