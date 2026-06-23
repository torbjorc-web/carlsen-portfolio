#!/usr/bin/env python
"""
Script to add all credentials to Render production database
Run this on Render shell with: python add_credentials_render.py
"""
import os
import django
import psycopg2
from pathlib import Path

# Configure Django for production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')
django.setup()

from learning.models import LearningCredential, SkillArea
from datetime import date

print("🚀 Adding credentials to Render production database...\n")

# Get or create skill areas
skill_areas = {
    'python': SkillArea.objects.get_or_create(
        slug='python',
        defaults={'name': 'Python', 'description': 'Python programming and data science'}
    )[0],
    'web-development': SkillArea.objects.get_or_create(
        slug='web-development',
        defaults={'name': 'Web Development', 'description': 'Web frameworks and full-stack development'}
    )[0],
    'ai-and-data': SkillArea.objects.get_or_create(
        slug='ai-and-data',
        defaults={'name': 'AI and Data', 'description': 'Artificial intelligence, machine learning, and data analysis'}
    )[0],
    'game-development': SkillArea.objects.get_or_create(
        slug='game-development',
        defaults={'name': 'Game Development', 'description': 'Game development with frameworks like Phaser'}
    )[0],
    'dotnet': SkillArea.objects.get_or_create(
        slug='dotnet',
        defaults={'name': '.NET', 'description': 'Microsoft .NET framework development'}
    )[0],
}

# Credentials to create (without PDFs - those will be uploaded separately)
credentials_data = [
    {
        'title': 'AI Engineering',
        'slug': 'ai-engineering-codecademy',
        'credential_type': 'professional_cert',
        'summary': 'Professional certification in AI engineering with hands-on projects and real-world applications.',
        'skills': ['ai-and-data'],
    },
    {
        'title': 'Game Development with Phaser',
        'slug': 'game-development-phaser',
        'credential_type': 'course',
        'summary': 'Course on building interactive 2D games using the Phaser framework.',
        'skills': ['game-development'],
    },
    {
        'title': 'Create Video Games with Phaser',
        'slug': 'create-video-games-phaser',
        'credential_type': 'skill_path',
        'summary': 'Comprehensive skill path for creating video games using Phaser game engine.',
        'skills': ['game-development'],
    },
    {
        'title': 'Data Scientist ISCP',
        'slug': 'data-scientist-iscp',
        'credential_type': 'professional_cert',
        'summary': 'International certification in data science with comprehensive curriculum.',
        'skills': ['python', 'ai-and-data'],
    },
    {
        'title': 'Data Scientist Machine Learning',
        'slug': 'data-scientist-ml',
        'credential_type': 'professional_cert',
        'summary': 'Professional certification focusing on machine learning techniques and data science applications.',
        'skills': ['python', 'ai-and-data'],
    },
    {
        'title': 'Business Intelligence & Data Analytics',
        'slug': 'bi-data-analytics',
        'credential_type': 'career_path',
        'summary': 'Career path in business intelligence and data analytics for enterprise solutions.',
        'skills': ['ai-and-data'],
    },
    {
        'title': 'Data Scientist Analytics',
        'slug': 'data-scientist-analytics',
        'credential_type': 'career_path',
        'summary': 'Advanced career path in data science and analytics with real-world case studies.',
        'skills': ['python', 'ai-and-data'],
    },
    {
        'title': 'Computer Science',
        'slug': 'computer-science',
        'credential_type': 'career_path',
        'summary': 'Comprehensive computer science career path covering algorithms, data structures, and fundamentals.',
        'skills': ['python'],
    },
    {
        'title': 'Django & .NET Backend Development',
        'slug': 'django-dotnet-backend',
        'credential_type': 'course',
        'summary': 'Course covering backend development with Django and .NET frameworks.',
        'skills': ['web-development', 'dotnet'],
    },
    {
        'title': 'Machine Learning & AI Engineer Path',
        'slug': 'ml-ai-engineer-path',
        'credential_type': 'career_path',
        'summary': 'Advanced career path for aspiring machine learning and AI engineers with project-based learning.',
        'skills': ['python', 'ai-and-data'],
    },
    {
        'title': 'Full Stack Engineer',
        'slug': 'full-stack-engineer',
        'credential_type': 'career_path',
        'summary': 'Complete career path for full stack engineering covering frontend, backend, and databases.',
        'skills': ['web-development', 'python'],
    },
    {
        'title': 'ASP.NET Developer',
        'slug': 'aspnet-developer',
        'credential_type': 'career_path',
        'summary': 'Career path for ASP.NET development with Microsoft technologies and best practices.',
        'skills': ['dotnet', 'web-development'],
    },
]

# Create credentials
created_count = 0
skipped_count = 0

for cred_data in credentials_data:
    try:
        # Check if already exists
        if LearningCredential.objects.filter(slug=cred_data['slug']).exists():
            print(f"⏭️  {cred_data['title']} - already exists")
            skipped_count += 1
            continue
        
        # Create credential
        cert = LearningCredential.objects.create(
            title=cred_data['title'],
            slug=cred_data['slug'],
            credential_type=cred_data['credential_type'],
            summary=cred_data['summary'],
            completed_at=date(2026, 6, 23),
            provider='Codecademy',
            is_featured=False,
        )
        
        # Add skills
        for skill_key in cred_data['skills']:
            cert.skill_areas.add(skill_areas[skill_key])
        
        print(f"✅ Created: {cred_data['title']}")
        created_count += 1
            
    except Exception as e:
        print(f"❌ Error creating {cred_data['title']}: {str(e)}")

print(f"\n📊 Summary:")
print(f"   ✅ Created: {created_count}")
print(f"   ⏭️  Skipped: {skipped_count}")
print(f"   📈 Total credentials now: {LearningCredential.objects.count()}")
print("\n✨ Done! All credentials have been added to the production database.")
