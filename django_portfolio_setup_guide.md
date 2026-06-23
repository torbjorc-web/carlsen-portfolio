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
