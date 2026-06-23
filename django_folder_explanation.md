# Folder questions

Yes — for a Django project, step 1 and step 2 are usually **folders**, but they are different kinds of folders.

## Step 1: Main project folder
This is the top-level folder for the whole portfolio.
Example:
- `carlsen-portfolio/`

## Step 2: Django project folder inside it
This is the folder created by `django-admin startproject`.
Example:
- `config/`

## Then inside that
You create the app folders:
- `core/`
- `services/`
- `portfolio/`
- `learning/`

## Simple structure
```text
carlsen-portfolio/
├── manage.py
├── config/
├── core/
├── services/
├── portfolio/
├── learning/
├── templates/
├── static/
└── media/
```

## So the answer is
- **Folder 1** = the outer project folder on your computer.
- **Folder 2** = the Django project package folder inside it.

They are both folders, but they serve different purposes.
