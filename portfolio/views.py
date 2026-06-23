import json
import urllib.error
import urllib.request
from datetime import datetime
from functools import lru_cache

from django.db import OperationalError, ProgrammingError
from django.shortcuts import get_object_or_404, render

from .models import Project

GITHUB_USER = 'torbjorc-web'
GITHUB_REPOS_URL = f'https://api.github.com/users/{GITHUB_USER}/repos?sort=updated&per_page=12&type=public'


@lru_cache(maxsize=1)
def fetch_github_repos():
    headers = {
        'User-Agent': 'Torbjorn-Carlsen-Portfolio',
        'Accept': 'application/vnd.github.v3+json',
    }
    request = urllib.request.Request(GITHUB_REPOS_URL, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            repos = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError):
        return []

    parsed_repos = []
    for repo in repos:
        updated_at = repo.get('updated_at')
        try:
            updated_at = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ') if updated_at else None
        except ValueError:
            updated_at = None

        parsed_repos.append({
            'name': repo.get('name'),
            'html_url': repo.get('html_url'),
            'description': repo.get('description') or '',
            'language': repo.get('language'),
            'stars': repo.get('stargazers_count', 0),
            'homepage': repo.get('homepage'),
            'updated_at': updated_at,
        })

    return parsed_repos


def project_list(request):
    try:
        projects = list(
            Project.objects.filter(status='published').order_by('-is_featured', '-published_at')
        )
    except (OperationalError, ProgrammingError):
        projects = []

    github_repos = fetch_github_repos()
    return render(request, 'portfolio/project_list.html', {
        'projects': projects,
        'github_repos': github_repos,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, status='published')
    return render(request, 'portfolio/project_detail.html', {'project': project})
