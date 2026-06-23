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

## Fresh Clone Setup (Database)

`db.sqlite3` is intentionally ignored and not committed. After cloning, create your local database by running migrations:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If you already have the virtual environment, start from `Activate.ps1`.
