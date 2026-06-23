from datetime import date

from django.core.management.base import BaseCommand

from portfolio.models import Project


PROJECTS = [
    {
        "slug": "carlsen-portfolio",
        "title": "Carlsen Portfolio",
        "short_description": "Django portfolio platform with multilingual support, contact workflows, and structured app architecture.",
        "problem": "Need one professional hub to present web, AI, and data competencies to employers.",
        "solution": "Built a modular Django solution with dedicated apps, templates, admin workflows, and dynamic content sections.",
        "outcome": "Clear employer-facing portfolio with maintainable structure and deploy-ready setup.",
        "github_url": "https://github.com/torbjorc-web/carlsen-portfolio",
        "client_type": "Personal flagship project",
    },
    {
        "slug": "benchmarkllm",
        "title": "BenchmarkLLM",
        "short_description": "LLM benchmarking project focused on prompt testing, quality checks, and practical AI evaluation workflows.",
        "problem": "Needed a practical way to compare and evaluate LLM output quality across tasks.",
        "solution": "Implemented structured benchmark scenarios and repeatable evaluation flows for model behavior testing.",
        "outcome": "Improved confidence in AI output quality and decision support for AI feature selection.",
        "github_url": "https://github.com/torbjorc-web/BenchmarkLLM",
        "client_type": "AI evaluation project",
    },
    {
        "slug": "spotify-analysis",
        "title": "Spotify Analysis",
        "short_description": "Data analysis project transforming Spotify datasets into understandable trends and insights.",
        "problem": "Raw music data lacked clear patterns for decision-making and storytelling.",
        "solution": "Used Python-based analysis to clean data, explore trends, and present key findings visually.",
        "outcome": "Readable analytics output suited for junior data analyst and BI-oriented discussions.",
        "github_url": "https://github.com/torbjorc-web/spotify_analysis",
        "client_type": "Data analysis project",
    },
]


class Command(BaseCommand):
    help = "Seed or update the three featured projects used on the home page"

    def handle(self, *args, **options):
        for item in PROJECTS:
            defaults = {k: v for k, v in item.items() if k != "slug"}
            defaults.update(
                {
                    "status": "published",
                    "is_featured": True,
                    "published_at": date.today(),
                }
            )
            project, created = Project.objects.update_or_create(
                slug=item["slug"], defaults=defaults
            )
            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action}: {project.title}"))

        count = Project.objects.filter(status="published").count()
        self.stdout.write(self.style.NOTICE(f"Published project count: {count}"))
