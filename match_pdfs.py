import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from learning.models import LearningCredential
from django.core.files.base import ContentFile

# Map existing credentials to PDF files from user
pdf_updates = {
    'ai-engineer-career-path': 'Ai enginering codecademy.pdf',
    'learn-game-development-phaserjs': 'Game development with Phaser.pdf',
    'data-scientist-professional-certificate-nnlpsc': 'Data scientist machine learning.pdf',
    'data-scientist-machine-learning-specialization': 'Data scientist machine learning.pdf',
    'computer-science-fundamentals': 'Computer science.pdf',
    'django-web-framework-essentials': 'Django net.pdf',
    'full-stack-engineer-career-path': "TorbCar's Full_Stack_Engineer_ Codecademy.pdf",
    'aspnet-career-path': "TorbCar's asp.net_ Codecademy.pdf",
    'codecademy-profile-badge': "TorbCar's profile _ Codecademy.pdf",
}

for slug, pdf_filename in pdf_updates.items():
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

# Count credentials with PDFs
with_pdf = LearningCredential.objects.exclude(certificate_file='').count()
total = LearningCredential.objects.count()

print(f"\n✅ Summary: {with_pdf}/{total} credentials have PDFs attached")
