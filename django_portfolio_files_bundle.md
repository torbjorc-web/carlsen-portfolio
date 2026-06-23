# Django portfolio files bundle

## django_portfolio_blueprint.md
```md
# Django portfolio starter blueprint

This blueprint is tailored for a consulting-focused portfolio for **Torbjørn Carlsen**, combining Python, Django, data science, AI/NLP, analytics, and selected game-development learning into one clear structure.

## Portfolio name options

### Strongest recommendation
**Carlsen Data & Web Studio**

Why it works:
- Uses your surname, which supports personal branding for solo consulting.
- Covers both analytics and software work.
- Sounds professional in both Norwegian and English contexts.
- Fits a portfolio site, GitHub profile, and future consulting business.

### Other good options
- **Torbjørn Carlsen Studio**
- **Carlsen AI & Data Studio**
- **Carlsen Analytics & Apps**
- **Northcode by Carlsen**
- **Carlsen Digital Solutions**
- **Carlsen Insight & Software**

### Best homepage title
**Torbjørn Carlsen**

### Best subtitle
Python, Django, Data Science, and AI Solutions

This keeps the homepage personal while letting the broader brand sit in the site footer, domain name, LinkedIn, and consulting materials.

## Suggested Django apps

Create these apps:

- `core` — homepage, about, contact, site settings.
- `portfolio` — projects, project images, categories, technologies.
- `services` — consulting services.
- `learning` — certificates, learning paths, skill areas.
- `blog` — optional later.

## Suggested project structure

```text
portfolio_site/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
├── portfolio/
├── services/
├── learning/
├── templates/
│   ├── base.html
│   ├── includes/
│   ├── core/
│   ├── portfolio/
│   ├── services/
│   └── learning/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
└── requirements.txt
```

## Data model blueprint

### core/models.py

```python
from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default='Carlsen Data & Web Studio')
    homepage_title = models.CharField(max_length=120, default='Torbjørn Carlsen')
    tagline = models.CharField(max_length=180, default='Python, Django, Data Science, and AI Solutions')
    hero_title = models.CharField(max_length=180)
    hero_subtitle = models.TextField()
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    resume_url = models.URLField(blank=True)

    def __str__(self):
        return self.site_name


class AboutProfile(models.Model):
    full_name = models.CharField(max_length=120)
    short_bio = models.TextField()
    long_bio = models.TextField()
    consulting_focus = models.TextField(blank=True)
    background_summary = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    project_type = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.email}'
```

### services/models.py

```python
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = models.TextField(blank=True)
    problem_it_solves = models.TextField(blank=True)
    deliverables = models.TextField(blank=True)
    ideal_for = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
```

### portfolio/models.py

```python
from django.db import models
from learning.models import LearningCredential
from services.models import Service

class Technology(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [('draft', 'Draft'), ('published', 'Published')]
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    client_type = models.CharField(max_length=120, blank=True)
    problem = models.TextField(blank=True)
    context = models.TextField(blank=True)
    goal = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    outcome = models.TextField(blank=True)
    lessons_learned = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateField(blank=True, null=True)
    technologies = models.ManyToManyField('Technology', blank=True)
    categories = models.ManyToManyField('ProjectCategory', blank=True)
    credentials = models.ManyToManyField(LearningCredential, related_name='projects', blank=True)
    services = models.ManyToManyField(Service, related_name='projects', blank=True)

    def __str__(self):
        return self.title
```

### learning/models.py

```python
from django.db import models

class SkillArea(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class LearningCredential(models.Model):
    CREDENTIAL_TYPES = [
        ('career_path', 'Career Path'),
        ('skill_path', 'Skill Path'),
        ('course', 'Course'),
        ('professional_cert', 'Professional Certification'),
    ]
    title = models.CharField(max_length=255)
    provider = models.CharField(max_length=120, default='Codecademy')
    slug = models.SlugField(unique=True)
    credential_type = models.CharField(max_length=30, choices=CREDENTIAL_TYPES)
    summary = models.TextField(blank=True)
    completed_at = models.DateField(null=True, blank=True)
    certificate_id = models.CharField(max_length=50, blank=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_image = models.ImageField(upload_to='certificate_images/', blank=True, null=True)
    skills_text = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    skill_areas = models.ManyToManyField(SkillArea, related_name='credentials', blank=True)

    class Meta:
        ordering = ['order', '-completed_at', 'title']

    def __str__(self):
        return self.title
```

## Add relationships

### portfolio/models.py additions

```python
from learning.models import LearningCredential
from services.models import Service

# inside Project model
credentials = models.ManyToManyField(LearningCredential, related_name='projects', blank=True)
services = models.ManyToManyField(Service, related_name='projects', blank=True)
```

### services/models.py additions

```python
from learning.models import LearningCredential

# inside Service model
credentials = models.ManyToManyField(LearningCredential, related_name='services', blank=True)
```

## Admin setup

### learning/admin.py

```python
from django.contrib import admin
from .models import SkillArea, LearningCredential

@admin.register(SkillArea)
class SkillAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(LearningCredential)
class LearningCredentialAdmin(admin.ModelAdmin):
    list_display = ('title', 'credential_type', 'completed_at', 'provider', 'is_featured')
    list_filter = ('credential_type', 'provider', 'is_featured', 'skill_areas')
    search_fields = ('title', 'summary', 'skills_text', 'certificate_id')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('skill_areas',)
```

## Seed data example

Create `learning/seed_codecademy.py`:

```python
from learning.models import SkillArea, LearningCredential

skill_map = {
    'ai-ml': 'AI and Machine Learning',
    'data-analytics': 'Data Science and Analytics',
    'web-dev': 'Web and Full-Stack Development',
    'game-dev': 'Interactive and Game Development',
}

for slug, name in skill_map.items():
    SkillArea.objects.get_or_create(slug=slug, defaults={'name': name})

credentials = [
    {
        'title': 'AI Engineer Career Path',
        'slug': 'ai-engineer-career-path',
        'credential_type': 'career_path',
        'completed_at': '2026-06-21',
        'certificate_id': 'E3BBA4A7-9',
        'summary': 'Structured training in AI engineering workflows and applied machine learning.',
        'skills_text': 'AI, machine learning, NLP, Python, practical AI workflows',
        'skill_area_slug': 'ai-ml',
    },
    {
        'title': 'Data Scientist Natural Language Processing Specialist Career Path',
        'slug': 'data-scientist-nlp-specialist-career-path',
        'credential_type': 'career_path',
        'completed_at': '2026-06-14',
        'certificate_id': '5E620DBC-D',
        'summary': 'Specialist training in NLP concepts and text analysis workflows.',
        'skills_text': 'NLP, text analysis, Python, language modeling foundations',
        'skill_area_slug': 'ai-ml',
    },
    {
        'title': 'Data Scientist Inference Specialist Career Path',
        'slug': 'data-scientist-inference-specialist-career-path',
        'credential_type': 'career_path',
        'completed_at': '2026-06-15',
        'certificate_id': '521FEA7A-7',
        'summary': 'Training in inference and statistical reasoning for data science.',
        'skills_text': 'inference, statistics, experimentation, Python',
        'skill_area_slug': 'ai-ml',
    },
    {
        'title': 'Data Scientist Machine Learning',
        'slug': 'data-scientist-machine-learning',
        'credential_type': 'career_path',
        'completed_at': '2026-06-13',
        'certificate_id': '01E03DE7-2',
        'summary': 'Machine learning training spanning foundations through neural networks.',
        'skills_text': 'SQL, Python, pandas, scikit-learn, statistics, data visualization, machine learning, neural networks',
        'skill_area_slug': 'ai-ml',
    },
    {
        'title': 'Business Intelligence Data Analyst Career Path',
        'slug': 'business-intelligence-data-analyst-career-path',
        'credential_type': 'career_path',
        'completed_at': '2026-06-13',
        'certificate_id': '5057BB15-9',
        'summary': 'BI-oriented analytics training for reporting and business insight.',
        'skills_text': 'BI, analytics, reporting, SQL, dashboards',
        'skill_area_slug': 'data-analytics',
    },
    {
        'title': 'Data Scientist Analytics',
        'slug': 'data-scientist-analytics',
        'credential_type': 'career_path',
        'completed_at': '2026-06-13',
        'certificate_id': 'BAFD7EFB-E',
        'summary': 'Analytics-focused data science training with databases, statistics, and BI tools.',
        'skills_text': 'SQL, Python, pandas, data cleaning, hypothesis testing, statistics, data visualization, Tableau, Excel',
        'skill_area_slug': 'data-analytics',
    },
    {
        'title': 'Full-Stack Engineer',
        'slug': 'full-stack-engineer',
        'credential_type': 'professional_cert',
        'completed_at': '2026-05-21',
        'certificate_id': 'B682C1F3-0',
        'summary': 'Professional certification across front-end and back-end web development.',
        'skills_text': 'HTML, CSS, JavaScript, Git, GitHub, React, Redux, Node.js, Express.js, SQL, PostgreSQL, web security, data structures, algorithms',
        'skill_area_slug': 'web-dev',
    },
    {
        'title': 'Build Web Apps with ASP.NET Skill Path',
        'slug': 'build-web-apps-with-aspnet-skill-path',
        'credential_type': 'skill_path',
        'completed_at': '2026-05-22',
        'certificate_id': '402040AF-0',
        'summary': 'Training in building web applications with ASP.NET.',
        'skills_text': 'ASP.NET, web apps, backend development',
        'skill_area_slug': 'web-dev',
    },
    {
        'title': 'Build Python Web Apps with Django Skill Path',
        'slug': 'build-python-web-apps-with-django-skill-path',
        'credential_type': 'skill_path',
        'completed_at': '2026-04-23',
        'certificate_id': 'D66A9AB4-0',
        'summary': 'Training in Django-based Python web app development.',
        'skills_text': 'Django, Python web development, templates, models, views',
        'skill_area_slug': 'web-dev',
    },
    {
        'title': 'Learn Game Development with Phaser.js Course',
        'slug': 'learn-game-development-with-phaser-js-course',
        'credential_type': 'course',
        'completed_at': '2026-06-16',
        'certificate_id': 'AAD1375A-7',
        'summary': 'Course in JavaScript-based game development with Phaser.js.',
        'skills_text': 'Phaser.js, JavaScript, interactive development',
        'skill_area_slug': 'game-dev',
    },
    {
        'title': 'Create Video Games with Phaser.js Skill Path',
        'slug': 'create-video-games-with-phaser-js-skill-path',
        'credential_type': 'skill_path',
        'completed_at': '2026-06-16',
        'certificate_id': '0F63DAF2-A',
        'summary': 'Skill path in building video games and interactive experiences with Phaser.js.',
        'skills_text': 'Phaser.js, game development, JavaScript, creative coding',
        'skill_area_slug': 'game-dev',
    },
]

for item in credentials:
    area = SkillArea.objects.get(slug=item.pop('skill_area_slug'))
    obj, _ = LearningCredential.objects.get_or_create(slug=item['slug'], defaults=item)
    obj.skill_areas.add(area)
```

## Services to create first

```text
1. Data analysis and reporting
2. Python automation and scripting
3. Django web applications
4. AI and NLP prototyping
```

## Best first portfolio projects

```text
1. Analytics dashboard for business or education reporting
2. Django internal workflow or record-management tool
3. NLP text classification or feedback-analysis project
4. Optional: interactive educational browser app using Phaser.js
```

## Template plan

```text
Home
- hero
- services
- featured projects
- learning highlights
- contact CTA

Services
- service cards
- process
- related credentials

Case Studies
- project grid
- project detail with linked credentials

Learning
- grouped credentials by skill area
- certificate cards
- skill summary

About
- background
- transition into consulting
- professional development

Contact
- contact form
- contact details
```

## Homepage learning block copy

```text
Recent structured training includes AI Engineer, Full-Stack Engineer, Django, ASP.NET, data analytics, machine learning, NLP, and Phaser.js. These learning paths support practical consulting work in automation, analytics, web development, and applied AI.
```

## About page professional development copy

```text
Professional development has focused on building practical strength across Python, Django, full-stack web development, data science, analytics, machine learning, and NLP. Coursework is reinforced through project-based implementation and portfolio case studies.
```

## Recommended domain ideas

- carlsendataweb.com
- torbjorncarlsen.dev
- carlsenstudio.dev
- carlsenanalytics.no
- carlsendigital.no

## Recommendation summary

For the portfolio itself, the clearest choice is:

**Torbjørn Carlsen**  
*Python, Django, Data Science, and AI Solutions*

For the broader studio or consulting identity, the strongest choice is:

**Carlsen Data & Web Studio**

This gives you a personal front-facing brand and a flexible business-style identity behind it.

```

## django_portfolio_setup_guide.md
```md
# Local setup guide for the Django portfolio

## 1. Create the project folder
```bash
mkdir carlsen-portfolio
cd carlsen-portfolio
python -m venv .venv
```

## 2. Activate the virtual environment
### Windows
```bash
.venv\Scripts\activate
```

### macOS / Linux
```bash
source .venv/bin/activate
```

## 3. Install dependencies
```bash
pip install Django Pillow whitenoise python-dotenv
pip freeze > requirements.txt
```

## 4. Start the Django project
```bash
django-admin startproject config .
python manage.py startapp core
python manage.py startapp portfolio
python manage.py startapp services
python manage.py startapp learning
```

## 5. Add the apps to `INSTALLED_APPS`
In `config/settings.py` or your split settings file, include:
```python
core
portfolio
services
learning
```

## 6. Create templates and static folders
```bash
mkdir templates
mkdir static
mkdir static/css
mkdir static/js
mkdir static/images
mkdir media
```

## 7. Add the base URLs
Use the URL structure already defined in the starter scaffold:
- `/`
- `/about/`
- `/contact/`
- `/services/`
- `/projects/`
- `/learning/`

## 8. Create the database models
Add these in their respective apps:
- `core.models.SiteSettings`
- `core.models.ContactMessage`
- `portfolio.models.Project`
- `portfolio.models.Technology`
- `portfolio.models.ProjectCategory`
- `learning.models.LearningCredential`
- `learning.models.SkillArea`

## 9. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 10. Create a superuser
```bash
python manage.py createsuperuser
```

## 11. Load your certificate data
Use the seed file concept from the scaffold and add all Codecademy certificates into the `learning` app.

## 12. Run the server
```bash
python manage.py runserver
```

Then open:
```text
http://127.0.0.1:8000/
```

## 13. Recommended build order
1. Home page.
2. Learning page.
3. Services page.
4. Projects page.
5. About page.
6. Contact form.
7. Polish and deploy.

## 14. First content to add
### Learning
- AI Engineer Career Path.
- Data Scientist NLP Specialist.
- Data Scientist Inference Specialist.
- Data Scientist Machine Learning.
- Business Intelligence Data Analyst.
- Data Scientist Analytics.
- Full-Stack Engineer.
- Build Web Apps with ASP.NET.
- Build Python Web Apps with Django.
- Phaser.js course and skill path.

### Projects
- Analytics dashboard.
- Django internal tool.
- NLP text project.
- Optional Phaser interactive demo.

### Services
- Data analysis and reporting.
- Python automation.
- Django web apps.
- AI / NLP prototyping.

## 15. Good first deployment target
If you want a simple first deployment later, use:
- Render
- Railway
- Fly.io
- PythonAnywhere

For the first local version, keep it simple and focus on content quality first.

```

## django_portfolio_starter_readme.md
```md
# Django portfolio starter

Generated starter scaffold for the portfolio site with:
- core, portfolio, services, learning apps
- base settings and URL routing
- starter models, views, and templates
- learning-section support for Codecademy credentials

Files included:
- `base_html.txt`
- `config_settings_base_py.txt`
- `config_urls_py.txt`
- `core_models_py.txt`
- `core_urls_py.txt`
- `core_views_py.txt`
- `portfolio_models_py.txt`
- `portfolio_urls_py.txt`
- `portfolio_views_py.txt`
- `learning_models_py.txt`
- `learning_urls_py.txt`
- `learning_views_py.txt`
- `home_html.txt`
- `requirements_txt.txt`
- `learning_seed_py.txt`

```

