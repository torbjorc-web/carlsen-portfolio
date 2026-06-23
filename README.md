# Carlsen Portfolio – Web & Data Science

> Full-stack portfolio demonstrating **Python/Django web development**, **AI/ML projects**, and **data analysis**. Built for employers seeking developers with diverse technical depth across web, automation, and analytics.

**📖 Languages / Språk:**
- **[English (EN)](#english)** 
- **[Norsk (NO)](#norsk)**

---

## English

### 1. Profile: Who You Are & What You Seek

**Torbjørn Carlsen** – Developer in career transition with focus on:

- **Python & Django** web development
- **AI/ML** (LLM, chatbots, image classification, neural networks)
- **Data Science** (analysis, visualization, insights)
- **IT support** and system optimization
- **Process digitalization**

**Seeking roles such as:**
- Junior Full-Stack Developer / Web Developer
- AI/ML-interested Engineer or Assistant
- Data Analyst or Junior BI Specialist
- IT Consultant or System Support with web understanding

### 2. Technology Stack

| Category | Technologies |
|----------|---------------|
| **Backend** | Python 3, Django 5.0, Django ORM |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla & Templates) |
| **Templates** | Django Template Engine, static file management |
| **Database** | SQLite (local), PostgreSQL-ready |
| **Deployment** | WhiteNoise (static files), WSGI/ASGI-compatible |
| **DevOps** | Environment-based settings (dev/prod), migrations |
| **Bonus Skills** | NumPy, Pandas, TensorFlow/Keras, Git |

### 3. What This App Demonstrates

**Carlsen Portfolio** is a Django-based portfolio app showcasing modern web development structure:

#### 📄 Core Pages
- **Home**: Introduction and navigation
- **About**: Profile and background
- **Contact**: Contact form with admin integration
- **Dashboard**: Message overview

#### 🛠️ Services & Projects
- **Services**: Service listings and detail pages
- **Portfolio**: Dynamic project gallery with descriptions
- **Learning**: Course certificates, career paths, and skill highlights

#### 🖥️ IT Support & Systems
- **Microsoft 365 Administration**: User management, Exchange Online, SharePoint, Teams
- **IT Support Fundamentals**: System support, troubleshooting, helpdesk best practices
- **System Documentation**: Support workflows and knowledge base

#### 🏗️ Architecture Highlights
- **Modular app structure**: Each area is a standalone Django app
- **Proper Django patterns**: Models, Views, URLs, Templates, Admin integration
- **Static files**: CSS and JavaScript organized per best practices
- **Database migrations**: Version control of data models
- **Settings separation**: Distinct dev/prod configurations
- **Multi-language support**: English and Norwegian with language switcher

### 4. Featured Projects

Projects showcasing diverse competencies across different domains:

| Project | Demonstrates | Best For | Stack |
|---------|--------------|----------|-------|
| **[carlsen-portfolio](https://github.com/torbjorc-web/carlsen-portfolio)** | Full Django web-app, structure, templates, migrations | Junior Web Developer, IT Consultant | Django, Python, HTML/CSS |
| **[BenchmarkLLM](https://github.com/torbjorc-web/BenchmarkLLM)** | LLM evaluation, AI experiments, prompt testing | AI Support, Junior AI/ML | Python, LLM APIs |
| **[Echo-Chatbot](https://github.com/torbjorc-web/Echo-Chatbot)** | Chatbot mechanics, conversational AI, automation | AI Assistant, Support Automation | Python, NLP, Chatbot |
| **[RecipeblogAI](https://github.com/torbjorc-web/RecipeblogAI)** | AI + web/app idea, practical LLM integration | Junior Full-Stack + AI | Django/Flask, Python, AI API |
| **[image_classification_ai](https://github.com/torbjorc-web/image_classification_ai)** | Machine learning, CNN, image classification | Data Scientist, ML Engineer | TensorFlow, Python, OpenCV |
| **[Neural-Networks](https://github.com/torbjorc-web/Neural-Networks-for-Classifying-Digits-and-Time-Series-Predictions)** | Neural networks, classification, time series | ML Engineer, Data Analyst | NumPy, TensorFlow, Keras |
| **[spotify_analysis](https://github.com/torbjorc-web/spotify_analysis)** | Data analysis, visualization, insights | Junior Data Analyst, BI | Pandas, Matplotlib, SQL |
| **[fastfoodie](https://github.com/torbjorc-web/fastfoodie)** | Frontend logic, JavaScript interaction, UX | Junior Frontend/Web | JavaScript, HTML/CSS |

### 5. Employer Value Proposition

#### ✅ You Get a Developer Who:

- **Understands full-stack web**: Backend (Django ORM, views, migrations) and frontend (templates, static assets, CSS)
- **Works across technologies**: Python, AI/ML, web, data – flexible problem-solver
- **Takes initiative**: Built multiple projects from concept to code
- **Documents thoughtfully**: READMEs, structure, migrations – maintains code quality
- **Willing to learn**: Career transition demonstrates motivation and rapid skill acquisition
- **Delivers structure**: All projects follow best practices (modularity, version control, settings management)

#### 🎯 Role-Specific Competencies:

| Role | Relevant Skills |
|------|-----------------|
| **Junior Web Developer** | Django structure, templates, static files, migrations, forms |
| **IT Consultant / Support** | System understanding, documentation, cross-stack problem-solving |
| **AI/ML Developer** | BenchmarkLLM, Echo-Chatbot, image_classification_ai, Neural Networks |
| **Data Analyst / BI** | spotify_analysis, Pandas/NumPy, data-driven insights |
| **Full-Stack Generalist** | Web + AI + Data combined – diverse skill set |

### 6. Status & Future Plans

#### ✅ Completed
- ✔️ Django app structure (core, services, portfolio, learning)
- ✔️ Template system with base.html and app-specific templates
- ✔️ Static files (CSS, JavaScript) organized
- ✔️ Admin integration for content management
- ✔️ Contact form with database storage
- ✔️ Migrations and database version control
- ✔️ Multi-language support (English/Norwegian)

#### 🚀 Planned Improvements
- [ ] Deploy to production (Render / Railway / Heroku)
- [ ] API endpoints for mobile/external integration
- [ ] User authentication & dashboard expansion
- [ ] Testing (unit + integration tests)
- [ ] Responsive design (mobile-first CSS)
- [ ] SEO optimization and analytics

### Quick Start

#### 1. Clone & Setup
```bash
git clone https://github.com/torbjorc-web/carlsen-portfolio.git
cd carlsen-portfolio
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### 2. Database & Server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### 3. Open in Browser
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/  (login with superuser)
```

#### Language Selection
Switch between English and Norwegian using the dropdown in the top navigation. URLs are automatically adjusted (e.g., `/en/`, `/no/`).

### File Structure

```
carlsen-portfolio/
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── config/                    # Django config root
│   ├── settings/
│   │   ├── base.py           # Shared settings
│   │   ├── dev.py            # Development overrides
│   │   ├── prod.py           # Production overrides
│   ├── urls.py               # Site-level routing with i18n
│   ├── wsgi.py               # Production server entry
│   └── asgi.py               # Async server entry
├── core/                      # Home, About, Contact, Dashboard
├── services/                  # Service listings
├── portfolio/                 # Project showcase
├── learning/                  # Course certificates & highlights
├── templates/                 # Site-wide templates (with i18n)
├── static/                    # CSS, JS, images
├── locale/                    # Translation files (i18n)
└── media/                     # User uploads (gitignored)
```

### Database Note

`db.sqlite3` is gitignored. Each local clone generates its own database by running migrations.

---

## Norsk

### 1. Profil: Hvem og hva du søker

**Torbjørn Carlsen** – Utvikler i karrierewending med fokus på:

- **Python & Django** webutvikling
- **AI/ML** (LLM, chatbots, bildeklassifisering, nevrale nettverk)
- **Data Science** (analyse, visualisering, insights)
- **IT-støtte** og systemoptimalisering
- **Digitalisering** av prosesser

**Søker etter roller som:**
- Junior Full-Stack Developer / Webutvikler
- AI/ML-interessert Ingeniør eller Assistent
- Data Analyst eller Junior BI-spesialist
- IT-konsulent eller System Support med webforståelse

### 2. Teknologistack

| Område | Teknologi |
|--------|-----------|
| **Backend** | Python 3, Django 5.0, Django ORM |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla & Templates) |
| **Templates** | Django Template Engine, static file management |
| **Database** | SQLite (lokalt), PostgreSQL-klar |
| **Deployment** | WhiteNoise (static files), WSGI/ASGI-kompatibel |
| **DevOps** | Miljø-baserte innstillinger (dev/prod), migrations |
| **Bonusferdigheter** | NumPy, Pandas, TensorFlow/Keras, Git |

### 3. Hva denne appen viser

**Carlsen Portfolio** er en Django-basert porteføljeapp som demonstrerer moderne webutviklingsstruktur:

#### 📄 Kjerneside
- **Home**: Introduksjon og navigasjon
- **About**: Profil og bakgrunn
- **Contact**: Kontaktskjema med admin-integrasjon
- **Dashboard**: Meldingsoversikt

#### 🛠️ Tjenester & Prosjekter
- **Services**: Listevisning og detalj-sider for tjenester
- **Portfolio**: Dynamisk prosjektgaleri med beskrivelser
- **Learning**: Kursbevis, career paths og kompetansehighlights

#### 🖥️ IT-Support & Systemer
- **Microsoft 365 Administrasjon**: Brukerstyring, Exchange Online, SharePoint, Teams
- **IT Support Fundamentals**: Systemstøtte, feilsøking, helpdesk best practices
- **Systemdokumentasjon**: Støtteprosesser og kunnskapsbase

#### 🏗️ Arkitektur-Highlights
- **Modulær appstruktur**: Hvert område er en selvstending Django-app
- **Proper Django patterns**: Models, Views, URLs, Templates, Admin-integrasjon
- **Static files**: CSS og JavaScript organisert per beste praksis
- **Database migrations**: Versjonskontroll av datamodeller
- **Settings-separasjon**: Distinkte dev/prod-konfigurasjoner
- **Flerspråksstøtte**: Engelsk og norsk med språkbytter

### 4. Utvalgte prosjekter

Prosjektene viser kompetanse på tvers av flere domener:

| Prosjekt | Hva det viser | Best for | Stack |
|----------|--------------|----------|-------|
| **[carlsen-portfolio](https://github.com/torbjorc-web/carlsen-portfolio)** | Full Django web-app, struktur, templates, migrations | Junior Webutvikler, IT-konsulent | Django, Python, HTML/CSS |
| **[BenchmarkLLM](https://github.com/torbjorc-web/BenchmarkLLM)** | LLM-evaluering, AI-eksperimenter, prompt-testing | AI Support, Junior AI/ML | Python, LLM APIs |
| **[Echo-Chatbot](https://github.com/torbjorc-web/Echo-Chatbot)** | Chatbot-mekanikk, conversational AI, automatisering | AI-assistent, Support-automatisering | Python, NLP, Chatbot |
| **[RecipeblogAI](https://github.com/torbjorc-web/RecipeblogAI)** | AI + web/app-idé, praktisk LLM-integrasjon | Junior Full-Stack + AI | Django/Flask, Python, AI API |
| **[image_classification_ai](https://github.com/torbjorc-web/image_classification_ai)** | Maskinlæring, CNN, bildeklassifisering | Data Scientist, ML Engineer | TensorFlow, Python, OpenCV |
| **[Neural-Networks](https://github.com/torbjorc-web/Neural-Networks-for-Classifying-Digits-and-Time-Series-Predictions)** | Nevrale nettverk, klassifisering, tidsserier | ML Engineer, Data Analyst | NumPy, TensorFlow, Keras |
| **[spotify_analysis](https://github.com/torbjorc-web/spotify_analysis)** | Dataanalyse, visualisering, insights | Junior Data Analyst, BI | Pandas, Matplotlib, SQL |
| **[fastfoodie](https://github.com/torbjorc-web/fastfoodie)** | Frontend-logikk, JavaScript-interaksjon, UX | Junior Frontend/Web | JavaScript, HTML/CSS |

### 5. Relevans for arbeidsgiver

#### ✅ Du får en utvikler som:

- **Forstår web fra begge sider**: Backend (Django ORM, views, migrations) og frontend (templates, static assets, CSS)
- **Kan håndtere flere teknologier**: Python, AI/ML, web, data – fleksibel problemløser
- **Tar initiativ**: Har bygget multiple prosjekter fra idé til kode
- **Dokumenterer**: README-filer, struktur, migrations – tenker på vedlikehold
- **Villig til å lære**: Karrierevendingen viser motivasjon og rask læring
- **Leverer struktur**: Alle prosjekter følger best practices (modularitet, versjonskontroll, settings-håndtering)

#### 🎯 For spesifikke stillinger:

| Stilling | Relevant kompetanse |
|----------|-----|
| **Junior Webutvikler** | Django-struktur, templates, static files, migrations, forms |
| **IT-konsulent / Support** | Systemforståelse, dokumentasjon, problemløsning på tvers av stack |
| **AI/ML-utvikler** | BenchmarkLLM, Echo-Chatbot, image_classification_ai, Neural Networks |
| **Data Analyst / BI** | spotify_analysis, Pandas/NumPy, datadrevne insights |
| **Full-Stack Generalist** | Web + AI + Data kombinert – bredspektrert ferdighetssett |

### 6. Status & videre plan

#### ✅ Ferdig nå
- ✔️ Django-appstruktur (core, services, portfolio, learning)
- ✔️ Template-system med base.html og app-spesifikke templates
- ✔️ Static files (CSS, JavaScript) organisert
- ✔️ Admin-integrasjon for content management
- ✔️ Kontaktskjema med database-lagring
- ✔️ Migrations og database-versjonskontroll
- ✔️ Flerspråksstøtte (engelsk/norsk)

#### 🚀 Planlagte forbedringer
- [ ] Deploy til produksjon (Render / Railway / Heroku)
- [ ] API-endpoints for mobil/ekstern integrasjon
- [ ] User authentication & dashboard-utvidelse
- [ ] Testing (unit + integration tests)
- [ ] Responsivt design (mobile-first CSS)
- [ ] SEO-optimisering og analytics

### Rask oppstart

#### 1. Clone & Setup
```bash
git clone https://github.com/torbjorc-web/carlsen-portfolio.git
cd carlsen-portfolio
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### 2. Database & Server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### 3. Åpne i nettleser
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/  (innlogging med superuser)
```

#### Språkvalg
Bytt mellom engelsk og norsk ved hjelp av rullegardinmenyen i topppnavigasjonen. URL-er justeres automatisk (f.eks. `/en/`, `/no/`).

### Filstruktur

```
carlsen-portfolio/
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── config/                    # Django config root
│   ├── settings/
│   │   ├── base.py           # Delte innstillinger
│   │   ├── dev.py            # Development overstyringer
│   │   ├── prod.py           # Production overstyringer
│   ├── urls.py               # Site-level routing med i18n
│   ├── wsgi.py               # Production server entry
│   └── asgi.py               # Async server entry
├── core/                      # Home, About, Contact, Dashboard
├── services/                  # Service listings
├── portfolio/                 # Prosjekt showcase
├── learning/                  # Kursbevis & highlights
├── templates/                 # Site-wide templates (med i18n)
├── static/                    # CSS, JS, bilder
├── locale/                    # Oversettingsfiler (i18n)
└── media/                     # Brukeropplastet innhold (gitignored)
```

### Database-notat

`db.sqlite3` er gitignored. Hver lokal klon genererer sin egen database ved å kjøre migrations.

---

## Spørsmål?

Se GitHub-repoer eller kontakt via [kontaktskjema](/).

**Ønskeliste til potensielle arbeidsgivere:** Gjerne test ut applikasjonen lokalt og gi tilbakemelding på kode, struktur eller features!
