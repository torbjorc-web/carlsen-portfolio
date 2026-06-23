import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from learning.models import LearningCredential
from django.core.files.base import ContentFile

# Map credentials to their PDF files
pdf_mappings = {
    'create-video-games-phaser': 'Create video games with Phaser.pdf',
    'data-scientist-iscp': 'Data Scientist ISCP.pdf',
    'bi-data-analytics': 'BI DA.pdf',
    'data-scientist-analytics': 'Data Scientist Analytics.pdf',
    'python-for-data-analysis': "TorbCar's profile _ Codecademy.pdf",
    'django-full-stack-development': None,  # Already has PDF
    'ai-workflow-prompt-engineering': None,  # Already has PDF
}

for slug, pdf_filename in pdf_mappings.items():
    if pdf_filename is None:
        continue
    
    try:
        cert = LearningCredential.objects.get(slug=slug)
        
        # Skip if already has a PDF
        if cert.certificate_file:
            print(f"⏭️  {cert.title} - already has PDF")
            continue
        
        pdf_path = f'c:\\Users\\torbj\\OneDrive\\Carlsen-portfolio\\media\\certificates\\{pdf_filename}'
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as f:
                cert.certificate_file.save(pdf_filename, ContentFile(f.read()), save=True)
            print(f"✅ Added PDF to {cert.title}")
        else:
            print(f"⚠️  PDF not found: {pdf_path}")
            
    except LearningCredential.DoesNotExist:
        print(f"❌ Credential not found: {slug}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

# List all credentials
print("\n📚 All credentials:")
for cert in LearningCredential.objects.all().order_by('order', '-completed_at'):
    pdf_status = "✅ PDF" if cert.certificate_file else "❌ No PDF"
    print(f"  {pdf_status} | {cert.title}")

print(f"\nTotal: {LearningCredential.objects.count()} credentials")
