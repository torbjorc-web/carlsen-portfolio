# Best file creation order

## Step 1: Project root
1. `manage.py`
2. `.env` optional
3. `requirements.txt`

## Step 2: Config package
4. `config/__init__.py`
5. `config/asgi.py`
6. `config/wsgi.py`
7. `config/urls.py`
8. `config/settings/__init__.py`
9. `config/settings/base.py`
10. `config/settings/dev.py`
11. `config/settings/prod.py`

## Step 3: Core app
12. `core/__init__.py`
13. `core/models.py`
14. `core/forms.py`
15. `core/views.py`
16. `core/admin.py`
17. `core/urls.py`
18. `core/templates/core/home.html`
19. `core/templates/core/about.html`
20. `core/templates/core/contact.html`

## Step 4: Services app
21. `services/__init__.py`
22. `services/models.py`
23. `services/views.py`
24. `services/admin.py`
25. `services/urls.py`
26. `services/templates/services/service_list.html`

## Step 5: Portfolio app
27. `portfolio/__init__.py`
28. `portfolio/models.py`
29. `portfolio/views.py`
30. `portfolio/admin.py`
31. `portfolio/urls.py`
32. `portfolio/templates/portfolio/project_list.html`
33. `portfolio/templates/portfolio/project_detail.html`

## Step 6: Learning app
34. `learning/__init__.py`
35. `learning/models.py`
36. `learning/views.py`
37. `learning/admin.py`
38. `learning/urls.py`
39. `learning/templates/learning/learning_list.html`
40. `learning/seed_codecademy.py`

## Step 7: Shared templates
41. `templates/base.html`

# How to put it on GitHub

## 1. Create a repo on GitHub
- Go to GitHub and create a new repository.
- Name it something like `carlsen-portfolio`.
- Do not add README, .gitignore, or license if your local folder already has files.

## 2. Initialize git locally
```bash
git init
git branch -M main
```

## 3. Add a `.gitignore`
Use at least:
```text
.venv/
__pycache__/
*.pyc
db.sqlite3
staticfiles/
media/
.env
```

## 4. Commit your files
```bash
git add .
git commit -m "Initial Django portfolio scaffold"
```

## 5. Connect to GitHub
Replace the URL with your repo URL:
```bash
git remote add origin https://github.com/yourusername/carlsen-portfolio.git
git push -u origin main
```

## 6. Keep pushing changes
After edits:
```bash
git add .
git commit -m "Add learning and portfolio content"
git push
```

## 7. Good GitHub structure
- Put the Django project at the repo root.
- Include a README with project purpose and setup steps.
- Add screenshots later if you want a polished portfolio feel.
- Keep sensitive files out of the repo.
