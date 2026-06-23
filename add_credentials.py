import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from learning.models import LearningCredential, SkillArea
from django.core.files.base import ContentFile
from datetime import date

# Get or create skill areas
python_skill, _ = SkillArea.objects.get_or_create(
    slug='python',
    defaults={'name': 'Python', 'description': 'Python programming and data science'}
)
web_skill, _ = SkillArea.objects.get_or_create(
    slug='web-development',
    defaults={'name': 'Web Development', 'description': 'Web frameworks and full-stack development'}
)
ai_skill, _ = SkillArea.objects.get_or_create(
    slug='ai-and-data',
    defaults={'name': 'AI and Data', 'description': 'Artificial intelligence, machine learning, and data analysis'}
)
gamedev_skill, _ = SkillArea.objects.get_or_create(
    slug='game-development',
    defaults={'name': 'Game Development', 'description': 'Game development with frameworks like Phaser'}
)
dotnet_skill, _ = SkillArea.objects.get_or_create(
    slug='dotnet',
    defaults={'name': '.NET', 'description': 'Microsoft .NET framework development'}
)

# Mapping of credentials to create
credentials_data = [
    {
        'title': 'AI Engineering',
        'slug': 'ai-engineering-codecademy',
        'credential_type': 'professional_cert',
        'summary': 'Professional certification in AI engineering with hands-on projects and real-world applications.',
        'pdf': 'Ai enginering codecademy.pdf',
        'skills': [ai_skill],
        'is_featured': False,
    },
    {
        'title': 'Game Development with Phaser',
        'slug': 'game-development-phaser',
        'credential_type': 'course',
        'summary': 'Course on building interactive 2D games using the Phaser framework.',
        'pdf': 'Game development with Phaser.pdf',
        'skills': [gamedev_skill],
        'is_featured': False,
    },
    {
        'title': 'Create Video Games with Phaser',
        'slug': 'create-video-games-phaser',
        'credential_type': 'skill_path',
        'summary': 'Comprehensive skill path for creating video games using Phaser game engine.',
        'pdf': 'Create video games with Phaser.pdf',
        'skills': [gamedev_skill],
        'is_featured': False,
    },
    {
        'title': 'Data Scientist ISCP',
        'slug': 'data-scientist-iscp',
        'credential_type': 'professional_cert',
        'summary': 'International certification in data science with comprehensive curriculum.',
        'pdf': 'Data Scientist ISCP.pdf',
        'skills': [python_skill, ai_skill],
        'is_featured': False,
    },
    {
        'title': 'Data Scientist Machine Learning',
        'slug': 'data-scientist-ml',
        'credential_type': 'professional_cert',
        'summary': 'Professional certification focusing on machine learning techniques and data science applications.',
        'pdf': 'Data scientist machine learning.pdf',
        'skills': [python_skill, ai_skill],
        'is_featured': False,
    },
    {
        'title': 'Business Intelligence & Data Analytics',
        'slug': 'bi-data-analytics',
        'credential_type': 'career_path',
        'summary': 'Career path in business intelligence and data analytics for enterprise solutions.',
        'pdf': 'BI DA.pdf',
        'skills': [ai_skill],
        'is_featured': False,
    },
    {
        'title': 'Data Scientist Analytics',
        'slug': 'data-scientist-analytics',
        'credential_type': 'career_path',
        'summary': 'Advanced career path in data science and analytics with real-world case studies.',
        'pdf': 'Data Scientist Analytics.pdf',
        'skills': [python_skill, ai_skill],
        'is_featured': False,
    },
    {
        'title': 'Computer Science',
        'slug': 'computer-science',
        'credential_type': 'career_path',
        'summary': 'Comprehensive computer science career path covering algorithms, data structures, and fundamentals.',
        'pdf': 'Computer science.pdf',
        'skills': [python_skill],
        'is_featured': False,
    },
    {
        'title': 'Django & .NET Backend Development',
        'slug': 'django-dotnet-backend',
        'credential_type': 'course',
        'summary': 'Course covering backend development with Django and .NET frameworks.',
        'pdf': 'Django net.pdf',
        'skills': [web_skill, dotnet_skill],
        'is_featured': False,
    },
    {
        'title': 'Machine Learning & AI Engineer Path',
        'slug': 'ml-ai-engineer-path',
        'credential_type': 'career_path',
        'summary': 'Advanced career path for aspiring machine learning and AI engineers with project-based learning.',
        'pdf': 'Machine Learning-AI Engineer Path.pdf',
        'skills': [python_skill, ai_skill],
        'is_featured': False,
    },
    {
        'title': 'Full Stack Engineer',
        'slug': 'full-stack-engineer',
        'credential_type': 'career_path',
        'summary': 'Complete career path for full stack engineering covering frontend, backend, and databases.',
        'pdf': "TorbCar's Full_Stack_Engineer_ Codecademy.pdf",
        'skills': [web_skill, python_skill],
        'is_featured': False,
    },
    {
        'title': 'ASP.NET Developer',
        'slug': 'aspnet-developer',
        'credential_type': 'career_path',
        'summary': 'Career path for ASP.NET development with Microsoft technologies and best practices.',
        'pdf': "TorbCar's asp.net_ Codecademy.pdf",
        'skills': [dotnet_skill, web_skill],
        'is_featured': False,
    },
]

# Create credentials
for cred_data in credentials_data:
    try:
        # Check if already exists
        if LearningCredential.objects.filter(slug=cred_data['slug']).exists():
            print(f"⚠️  Skipping {cred_data['title']} - already exists")
            continue
        
        # Create credential
        cert = LearningCredential.objects.create(
            title=cred_data['title'],
            slug=cred_data['slug'],
            credential_type=cred_data['credential_type'],
            summary=cred_data['summary'],
            completed_at=date(2026, 6, 23),
            provider='Codecademy',
            is_featured=cred_data['is_featured'],
        )
        
        # Add skills
        for skill in cred_data['skills']:
            cert.skill_areas.add(skill)
        
        # Attach PDF
        pdf_path = f'c:\\Users\\torbj\\OneDrive\\Carlsen-portfolio\\media\\certificates\\{cred_data["pdf"]}'
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as f:
                cert.certificate_file.save(cred_data['pdf'], ContentFile(f.read()), save=True)
            print(f"✅ Created {cred_data['title']} with PDF")
        else:
            print(f"⚠️  Created {cred_data['title']} but PDF not found at {pdf_path}")
            
    except Exception as e:
        print(f"❌ Error creating {cred_data['title']}: {str(e)}")

print("\n✅ All credentials processed!")
