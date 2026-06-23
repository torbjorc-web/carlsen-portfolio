# Carlsen Portfolio – Web & Data Science

> Full-stack portfolio demonstrating **Python/Django web development**, **AI/ML projects**, and **data analysis**. Built for employers seeking developers with diverse technical depth across web, automation, and analytics.

---

## 1. Profil: Hvem og hva jeg søker

**Torbjørn Carlsen** – Utvikler i karriere endring med fokus på:

- **Python & Django** web-development
- **AI/ML** (LLM, chatbots, bildeklassifisering, nevrale nettverk)
- **Data Science** (analyse, visualisering, insights)
- **IT-støtte** og systemoptimalisering
- **Digitalisering** av prosesser

**Søker etter roller som:**
- Junior Full-Stack Developer / Web Developer
- AI/ML-interessert Ingeniør eller Assistent
- Data Analyst eller Junior BI-spesialist
- IT-konsulent eller System Support med webforståelse

---

## 2. Teknologistack

| Område | Teknologi |
|--------|-----------|
| **Backend** | Python 3, Django 5.0, Django ORM |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla & Templates) |
| **Templates** | Django Template Engine, static file management |
| **Database** | SQLite (local), PostgreSQL-ready |
| **Deployment** | WhiteNoise (static files), WSGI/ASGI-compatible |
| **DevOps** | Environment-based settings (dev/prod), migrations |
| **Bonus Skills** | Python, NumPy, Pandas, TensorFlow/Keras, Git |

---

## 3. Hva denne appen viser

**Carlsen Portfolio** er en Django-basert porteføljeapp som demonstrerer moderne webutviklingsstruktur:

### 📄 Core Pages
- **Home**: Introduksjon og navigasjon
- **About**: Profil og bakgrunn
- **Contact**: Kontaktskjema med admin-integrasjon
- **Dashboard**: Meldingsoversikt

### 🛠️ Tjenester & Prosjekter
- **Services**: Listevisning og detalj-sider for konsulttjenester
- **Portfolio**: Dynamisk prosjekt-galeri med beskrivelser
- **Learning**: Sertifikat, kurs og kompetansehighlights

### 🏗️ Arkitektur-Highlights
- **Modulær appstruktur**: Hvert område (core, services, portfolio, learning) er en selvstandi Django-app
- **Proper Django patterns**: Models, Views, URLs, Templates, Admin-integrasjon
- **Static files**: CSS og JavaScript organisert per beste praksis
- **Database migrations**: Versjonskontroll av datamodeller
- **Settings-separasjon**: Distinkte dev/prod-konfigurasjoner

---

## 4. Utvalgte prosjekter (best på CV)

Prosjektene under viser kompetanse på tvers av flere domener og passer til ulike stillinger:

| Prosjekt | Hva det viser | Best for | Stack |
|----------|--------------|----------|-------|
| **[carlsen-portfolio](https://github.com/torbjorc-web/carlsen-portfolio)** | Full Django web-app, struktur, templates, migrations | Junior Web Developer, IT-konsulent | Django, Python, HTML/CSS |
| **[BenchmarkLLM](https://github.com/torbjorc-web/BenchmarkLLM)** | LLM-evaluering, AI-eksperimenter, prompt-testing | AI Support, AI/ML Junior | Python, LLM APIs |
| **[Echo-Chatbot](https://github.com/torbjorc-web/Echo-Chatbot)** | Chatbot-mekanikk, conversational AI, automatisering | AI-assistent, Support-automatisering | Python, NLP, Chatbot |
| **[RecipeblogAI](https://github.com/torbjorc-web/RecipeblogAI)** | AI + web/app-ide, praktisk LLM-integrasjon | Junior Full-Stack + AI | Django/Flask, Python, AI API |
| **[image_classification_ai](https://github.com/torbjorc-web/image_classification_ai)** | Maskinlæring, CNN, bildeklassifisering | Data Scientist, ML Engineer | TensorFlow, Python, OpenCV |
| **[Neural-Networks-for-Classifying-Digits-and-Time-Series-Predictions](https://github.com/torbjorc-web/Neural-Networks-for-Classifying-Digits-and-Time-Series-Predictions)** | Nevrale nettverk, klassifisering, tidsserier | ML Engineer, Data Analyst | NumPy, TensorFlow, Keras |
| **[spotify_analysis](https://github.com/torbjorc-web/spotify_analysis)** | Dataanalyse, visualisering, insights | Junior Data Analyst, BI | Pandas, Matplotlib, SQL |
| **[fastfoodie](https://github.com/torbjorc-web/fastfoodie)** | Frontend-logikk, JavaScript-interaksjon, UX | Junior Frontend/Web | JavaScript, HTML/CSS |

---

## 5. Relevans for arbeidsgiver

### ✅ Du får en utvikler som:

- **Forstår web fra begge sider**: Backend (Django ORM, views, migrations) og frontend (templates, static assets, CSS)
- **Kan håndtere flere teknologier**: Python, AI/ML, web, data – fleksibel i problemløsning
- **Tar initiativ**: Har bygget multiple prosjekter fra ide til kode, viser selvstyring
- **Dokumenterer**: README-filer, struktur, migrations – tenker på maintainability
- **Er villig til å lære**: Karrierevendingen viser motivasjon og evne til rask opplæring
- **Leverer struktur**: Alle prosjekter følger best practices (modularitet, versjonskontroll, settings-håndtering)

### 🎯 For spesifikke stillinger:

| Stilling | Relevant kompetanse fra repo |
|----------|-----|
| **Junior Web Developer** | Django-struktur, templates, static files, migrations, forms |
| **IT-konsulent / Support** | Systemforståelse, dokumentasjon, problem-solving tvers av stack |
| **AI/ML-interessent** | BenchmarkLLM, Echo-Chatbot, image_classification_ai, Neural Networks |
| **Data Analyst / BI** | spotify_analysis, Pandas/NumPy, data-driven insights |
| **Full-Stack Generalist** | Web + AI + Data kombinert – ferdighetene er bredspektret |

---

## 6. Status & videre plan

### ✅ Ferdig nå
- ✔️ Django-appstruktur (core, services, portfolio, learning)
- ✔️ Template-system med base.html og app-spesifikke templates
- ✔️ Static files (CSS, JavaScript) organisert
- ✔️ Admin-integrasjon for content management
- ✔️ Contact form med database-lagring
- ✔️ Migrasjoner og database-versjonskontroll

### 🚀 Planlagte forbedringer
- [ ] Deploy til live (Render / Railway / Heroku)
- [ ] API-endpoints for mobil/ekstern integrasjon
- [ ] User authentication & dashboard-expansion
- [ ] Testing (unit + integration tests)
- [ ] Responsiv design (mobile-first CSS)
- [ ] SEO-optimisering og analytics

---

## Rask oppstart

### 1. Clone & setup
```bash
git clone https://github.com/torbjorc-web/carlsen-portfolio.git
cd carlsen-portfolio
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Database & server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3. Åpne i browser
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/  (innlogging med superuser)
```

---

## Filstruktur

```
carlsen-portfolio/
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── config/                    # Django config root
│   ├── settings/
│   │   ├── base.py           # Shared settings
│   │   ├── dev.py            # Development overrides
│   │   ├── prod.py           # Production overrides
│   ├── urls.py               # Site-level routing
│   ├── wsgi.py               # Production server entry
│   └── asgi.py               # Async server entry
├── core/                      # Home, About, Contact, Dashboard
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/core/
├── services/                  # Service listings
├── portfolio/                 # Project showcase
├── learning/                  # Credentials & highlights
├── templates/                 # Site-wide templates
│   └── base.html             # Master template
├── static/                    # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
└── media/                     # User uploads (gitignored)
```

---

## Database-notat

`db.sqlite3` er gitignored og committed ikke. Hver lokal klon genererer sin egen DB ved å kjøre migrasjoner.

---

**Spørsmål?** Se GitHub-repoer eller kontakt via [contact form](/).

**Ønskeliste til potensielle arbeidsgivere:** Gjerne test ut applikasjonen lokalt og gi feedback på kode, struktur eller features!
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
