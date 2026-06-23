# Terminal commands to run after pasting the files

## 1. Go to your project folder
```bash
cd path/to/carlsen-portfolio
```

## 2. Create and activate a virtual environment
### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Make sure the app folders exist
```bash
python manage.py startapp core
python manage.py startapp services
python manage.py startapp portfolio
python manage.py startapp learning
```

If the apps already exist, skip this step.

## 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Create a superuser
```bash
python manage.py createsuperuser
```

## 7. Run the server
```bash
python manage.py runserver
```

## 8. Open the site
```text
http://127.0.0.1:8000/
```

## 9. Load content in admin
- Create SiteSettings.
- Add AboutProfile.
- Add services.
- Add learning credentials.
- Add projects and mark the best ones as featured.
