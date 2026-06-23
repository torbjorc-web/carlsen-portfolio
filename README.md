# Carlsen Portfolio (Django)

This repository contains a Django portfolio project with apps for core pages, services, projects, and learning credentials.

## Project Overview

- Brand: Carlsen Data & Web Studio
- Homepage title: Torbjorn Carlsen
- Focus: Python, Django, Data Science, AI, and digital consulting

## Project Structure

```text
carlsen-portfolio/
|- manage.py
|- requirements.txt
|- config/
|  |- settings/
|  |  |- base.py
|  |  |- dev.py
|  |  |- prod.py
|  |- urls.py
|  |- asgi.py
|  |- wsgi.py
|- core/
|- services/
|- portfolio/
|- learning/
|- templates/
|- static/
|- media/ (local, ignored)
```

## Apps

- `core`: home, about, contact, dashboard, site-level content
- `services`: service listings and details
- `portfolio`: project list/detail pages
- `learning`: credentials and learning highlights

## Local Setup

### 1. Create and activate virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create admin user

```bash
python manage.py createsuperuser
```

### 5. Run the server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Database Note

`db.sqlite3` is intentionally ignored and not committed. Each clone should create its own local DB by running migrations.

## Settings Layout

- `config/settings/base.py`: shared defaults
- `config/settings/dev.py`: development overrides
- `config/settings/prod.py`: production overrides
- `config/settings/__init__.py`: settings import entrypoint

## Typical Build Order

1. Configure settings and URLs
2. Build core pages
3. Build services pages
4. Build portfolio pages
5. Build learning pages
6. Add admin content
7. Polish UI and deploy

## GitHub Workflow

Initial setup:

```bash
git init
git branch -M main
git remote add origin https://github.com/<your-user>/<your-repo>.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

Daily updates:

```bash
git add .
git commit -m "Describe changes"
git push
```

## Notes on Ignored Files

The following are local/runtime artifacts and should remain untracked:

- `.venv/`
- `__pycache__/`
- `*.pyc`
- `db.sqlite3`
- `media/`
- `*.crdownload`

## Content Admin Checklist

- Create/update site settings
- Add services
- Add projects
- Add learning credentials
- Verify contact flow and dashboard messages
