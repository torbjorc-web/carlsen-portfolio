# Master file map for the Django portfolio

## Project root
- `manage.py` -> from `manage_py`
- `requirements.txt` -> from `requirements_txt`
- `db.sqlite3` -> created after migrations
- `.env` -> optional

## `config/`
- `config/__init__.py` -> from `config_init_py_final`
- `config/asgi.py` -> from `config_asgi_py`
- `config/wsgi.py` -> from `config_wsgi_py`
- `config/urls.py` -> from `config_urls_py`
- `config/settings/__init__.py` -> from `config_settings_init_py_final`
- `config/settings/base.py` -> from `config_settings_base_py`
- `config/settings/dev.py` -> from `config_settings_dev_py`
- `config/settings/prod.py` -> from `config_settings_prod_py`

## `core/`
- `core/__init__.py` -> from `core_init_py`
- `core/models.py` -> from `core_models.py`
- `core/views.py` -> from `core_views.py`
- `core/forms.py` -> from `core_forms.py`
- `core/admin.py` -> from `core_admin.py`
- `core/urls.py` -> from `core_urls.py`
- `core/templates/core/home.html` -> from `home_html`
- `core/templates/core/about.html` -> from `core_about_html`
- `core/templates/core/contact.html` -> from `core_contact_html`

## `services/`
- `services/__init__.py` -> from `services_init_py`
- `services/models.py` -> from `services_models.py`
- `services/views.py` -> from `services_views.py`
- `services/admin.py` -> from `services_admin.py`
- `services/urls.py` -> from `services_urls.py`
- `services/templates/services/service_list.html` -> from `services_service_list_html`

## `portfolio/`
- `portfolio/__init__.py` -> from `portfolio_init_py`
- `portfolio/models.py` -> from `portfolio_models.py`
- `portfolio/views.py` -> from `portfolio_views.py`
- `portfolio/admin.py` -> from `portfolio_admin.py`
- `portfolio/urls.py` -> from `portfolio_urls.py`
- `portfolio/templates/portfolio/project_list.html` -> from `portfolio_project_list_html`
- `portfolio/templates/portfolio/project_detail.html` -> from `portfolio_project_detail_html`

## `learning/`
- `learning/__init__.py` -> from `learning_init_py`
- `learning/models.py` -> from `learning_models.py`
- `learning/views.py` -> from `learning_views.py`
- `learning/admin.py` -> from `learning_admin.py`
- `learning/urls.py` -> from `learning_urls.py`
- `learning/templates/learning/learning_list.html` -> from `learning_learning_list_html`
- `learning/seed_codecademy.py` -> from `learning_seed_py`

## Shared templates
- `templates/base.html` -> from `base_html`

## Documentation files
- `django_portfolio_blueprint.md`
- `django_portfolio_setup_guide.md`
- `django_portfolio_starter_readme.md`
- `django_portfolio_files_bundle.md`
- `django_portfolio_file_map.md`
- `django_portfolio_rename_map.md`
- `django_portfolio_settings_files_readme.md`
- `django_portfolio_code_files_readme.md`
- `django_portfolio_final_scaffold_readme.md`
