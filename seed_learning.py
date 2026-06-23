"""
Seed script for learning credentials.
Run locally: python manage.py shell < seed_learning.py
"""
from learning.models import SkillArea, LearningCredential
from datetime import date

# Clear existing data
LearningCredential.objects.all().delete()
SkillArea.objects.all().delete()

# Create skill areas
areas = {
    'python': SkillArea.objects.create(
        name='Python',
        slug='python',
        description='Python programming fundamentals and advanced concepts'
    ),
    'web': SkillArea.objects.create(
        name='Web Development',
        slug='web-development',
        description='Full-stack web development with Django and modern frontend'
    ),
    'data': SkillArea.objects.create(
        name='Data Science',
        slug='data-science',
        description='Data analysis, visualization, and machine learning'
    ),
    'ai_ml': SkillArea.objects.create(
        name='AI & Machine Learning',
        slug='ai-machine-learning',
        description='LLM integration, model training, and AI applications'
    ),
    'it_support': SkillArea.objects.create(
        name='IT Support',
        slug='it-support',
        description='System administration, troubleshooting, and IT operations'
    ),
}

# Create learning credentials
credentials = [
    {
        'title': 'Python for Data Analysis',
        'provider': 'Codecademy',
        'slug': 'python-data-analysis',
        'credential_type': 'skill_path',
        'summary': 'Comprehensive Python course focused on data manipulation, analysis, and visualization using pandas and matplotlib.',
        'completed_at': date(2024, 6, 15),
        'certificate_id': 'CC-2024-06-12345',
        'skills_text': 'Python, Pandas, Data Visualization, NumPy',
        'is_featured': True,
        'order': 1,
        'skill_areas': [areas['python'], areas['data']],
    },
    {
        'title': 'Full Stack JavaScript Career Path',
        'provider': 'Codecademy',
        'slug': 'fullstack-javascript',
        'credential_type': 'career_path',
        'summary': 'Complete career path covering HTML, CSS, JavaScript, React, Node.js, and database management.',
        'completed_at': date(2024, 3, 20),
        'certificate_id': 'CC-2024-03-67890',
        'skills_text': 'JavaScript, React, Node.js, Express, MongoDB',
        'is_featured': True,
        'order': 2,
        'skill_areas': [areas['web']],
    },
    {
        'title': 'Django Web Development Mastery',
        'provider': 'Real Python',
        'slug': 'django-mastery',
        'credential_type': 'course',
        'summary': 'Advanced Django concepts including ORM, authentication, deployment, and performance optimization.',
        'completed_at': date(2023, 11, 10),
        'certificate_id': 'RP-2023-11-11111',
        'skills_text': 'Django, REST APIs, Authentication, PostgreSQL, Deployment',
        'is_featured': True,
        'order': 3,
        'skill_areas': [areas['web'], areas['python']],
    },
    {
        'title': 'Machine Learning Specialization',
        'provider': 'Coursera',
        'slug': 'ml-specialization',
        'credential_type': 'professional_cert',
        'summary': 'Four-course specialization covering supervised learning, unsupervised learning, and neural networks.',
        'completed_at': date(2024, 1, 5),
        'certificate_id': 'COR-2024-01-22222',
        'skills_text': 'Machine Learning, Scikit-learn, TensorFlow, Neural Networks',
        'is_featured': True,
        'order': 4,
        'skill_areas': [areas['ai_ml'], areas['data'], areas['python']],
    },
    {
        'title': 'CompTIA A+ Certification Prep',
        'provider': 'Professor Messer',
        'slug': 'comptia-aplus',
        'credential_type': 'professional_cert',
        'summary': 'Comprehensive preparation course for CompTIA A+ certification covering hardware, networking, and troubleshooting.',
        'completed_at': date(2023, 8, 22),
        'certificate_id': 'EXAM-2023-08-33333',
        'skills_text': 'System Administration, Networking, Hardware, Troubleshooting, Windows/Linux',
        'is_featured': True,
        'order': 5,
        'skill_areas': [areas['it_support']],
    },
]

# Create credentials and associate skill areas
for cred in credentials:
    skill_areas = cred.pop('skill_areas')
    learning_cred = LearningCredential.objects.create(**cred)
    learning_cred.skill_areas.set(skill_areas)
    print(f"✅ Created: {learning_cred.title}")

print("\n✅ Database seeded successfully!")
print(f"Total credentials: {LearningCredential.objects.count()}")
print(f"Total skill areas: {SkillArea.objects.count()}")
