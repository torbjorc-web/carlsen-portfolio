import os
from datetime import date
from django.db import transaction
from .models import LearningCredential, SkillArea


def create_skill_areas():
    """Create skill area categories."""
    areas = [
        ('backend', 'Backend Development'),
        ('ai-ml', 'AI & Machine Learning'),
        ('data-science', 'Data Science'),
        ('web-dev', 'Web Development'),
        ('game-dev', 'Game Development'),
        ('business-analytics', 'Business Analytics'),
        ('cs-fundamentals', 'Computer Science Fundamentals'),
        ('it-support', 'IT Support & Systems'),
    ]
    
    for slug, name in areas:
        area, created = SkillArea.objects.get_or_create(
            slug=slug,
            defaults={'name': name}
        )
        if created:
            print(f'✓ Created skill area: {name}')


def create_credentials():
    """Create learning credentials from verified courses and certifications."""
    
    credentials_data = [
        {
            'title': 'AI Engineer Career Path',
            'provider': 'Codecademy',
            'slug': 'ai-engineer-career-path',
            'credential_type': 'career_path',
            'summary': 'Comprehensive AI engineering curriculum covering machine learning, neural networks, LLM fundamentals, and practical AI project development.',
            'completed_at': date(2026, 6, 21),
            'certificate_id': 'E3864447-0',
            'skills_text': 'Machine Learning, Neural Networks, LLMs, Python, TensorFlow, Keras',
            'is_featured': True,
            'order': 1,
            'skill_areas': ['ai-ml', 'data-science'],
        },
        {
            'title': 'Learn Game Development with Phaser.js',
            'provider': 'Codecademy',
            'slug': 'game-dev-phaser-js',
            'credential_type': 'skill_path',
            'summary': 'Interactive course on building 2D games using Phaser.js framework. Covers game mechanics, physics, animations, and JavaScript game development.',
            'completed_at': date(2026, 6, 16),
            'certificate_id': 'AEE19764-0',
            'skills_text': 'JavaScript, Phaser.js, Game Mechanics, Canvas Rendering',
            'is_featured': True,
            'order': 2,
            'skill_areas': ['game-dev', 'web-dev'],
        },
        {
            'title': 'Create Video Games with Phaser',
            'provider': 'Codecademy',
            'slug': 'create-video-games-phaser',
            'credential_type': 'course',
            'summary': 'Practical game development course building complete games with Phaser engine. Hands-on projects in interactive 2D game creation.',
            'completed_at': date(2026, 6, 16),
            'skills_text': 'Phaser, Game Design, JavaScript, Interactive Development',
            'is_featured': False,
            'order': 3,
            'skill_areas': ['game-dev'],
        },
        {
            'title': 'Data Scientist: Machine Learning',
            'provider': 'Codecademy',
            'slug': 'data-scientist-ml-spec',
            'credential_type': 'skill_path',
            'summary': 'Comprehensive machine learning specialization covering supervised/unsupervised learning, model evaluation, and real-world ML applications.',
            'completed_at': date(2026, 5, 28),
            'skills_text': 'Scikit-learn, Machine Learning, Model Training, Evaluation Metrics, Python',
            'is_featured': True,
            'order': 4,
            'skill_areas': ['ai-ml', 'data-science'],
        },
        {
            'title': 'Computer Science Fundamentals',
            'provider': 'Codecademy',
            'slug': 'cs-fundamentals',
            'credential_type': 'skill_path',
            'summary': 'Core computer science concepts including algorithms, data structures, complexity analysis, and problem-solving foundations.',
            'completed_at': date(2026, 5, 20),
            'skills_text': 'Algorithms, Data Structures, Big O Notation, Problem Solving, Python',
            'is_featured': False,
            'order': 5,
            'skill_areas': ['cs-fundamentals'],
        },
        {
            'title': 'Django Web Framework Essentials',
            'provider': 'Self-Study',
            'slug': 'django-web-framework',
            'credential_type': 'skill_path',
            'summary': 'Django framework fundamentals for building scalable web applications. ORM, views, templates, migrations, and deployment best practices.',
            'completed_at': date(2026, 6, 10),
            'skills_text': 'Django, Python, ORM, MTV Architecture, Web Development, PostgreSQL',
            'is_featured': True,
            'order': 6,
            'skill_areas': ['backend', 'web-dev'],
        },
        {
            'title': 'Full Stack Engineer Career Path',
            'provider': 'Codecademy',
            'slug': 'full-stack-engineer-career',
            'credential_type': 'career_path',
            'summary': 'Comprehensive full-stack engineering curriculum covering both frontend and backend technologies. HTML/CSS, JavaScript, databases, and server-side frameworks.',
            'completed_at': date(2026, 5, 15),
            'skills_text': 'Frontend, Backend, JavaScript, Databases, Full-Stack Development, React, Node.js',
            'is_featured': True,
            'order': 7,
            'skill_areas': ['web-dev', 'backend'],
        },
        {
            'title': 'ASP.NET Career Path',
            'provider': 'Codecademy',
            'slug': 'aspnet-career-path',
            'credential_type': 'career_path',
            'summary': 'ASP.NET framework specialization for building enterprise web applications. C#, MVC patterns, databases, and cloud-ready architecture.',
            'completed_at': date(2026, 5, 10),
            'skills_text': 'ASP.NET, C#, MVC, Entity Framework, Web Services, SQL Server',
            'is_featured': True,
            'order': 8,
            'skill_areas': ['backend', 'web-dev'],
        },
        {
            'title': 'Microsoft 365 Administration',
            'provider': 'Self-Study',
            'slug': 'microsoft-365-admin',
            'credential_type': 'skill_path',
            'summary': 'Core Microsoft 365 administration including user management, Exchange Online, SharePoint, Teams, and security fundamentals for IT support.',
            'completed_at': date(2026, 4, 15),
            'skills_text': 'Microsoft 365, Exchange Online, SharePoint, Teams, User Management, Security',
            'is_featured': True,
            'order': 9,
            'skill_areas': ['it-support'],
        },
        {
            'title': 'IT Support Fundamentals',
            'provider': 'Self-Study',
            'slug': 'it-support-fundamentals',
            'credential_type': 'skill_path',
            'summary': 'System support and troubleshooting fundamentals including Windows systems, network basics, ticketing systems, and helpdesk best practices.',
            'completed_at': date(2026, 4, 1),
            'skills_text': 'Windows Systems, Troubleshooting, Helpdesk, Active Directory, Network Basics',
            'is_featured': True,
            'order': 10,
            'skill_areas': ['it-support'],
        },
    ]
    
    with transaction.atomic():
        for cred_data in credentials_data:
            skill_area_slugs = cred_data.pop('skill_areas', [])
            
            credential, created = LearningCredential.objects.get_or_create(
                slug=cred_data['slug'],
                defaults=cred_data
            )
            
            if created:
                # Add skill areas
                for slug in skill_area_slugs:
                    try:
                        area = SkillArea.objects.get(slug=slug)
                        credential.skill_areas.add(area)
                    except SkillArea.DoesNotExist:
                        pass
                
                print(f'✓ Created credential: {credential.title}')
            else:
                print(f'→ Credential already exists: {credential.title}')


def run():
    """Main seed function."""
    print('\n🌱 Seeding learning credentials...\n')
    create_skill_areas()
    print()
    create_credentials()
    print('\n✅ Seeding complete!\n')
