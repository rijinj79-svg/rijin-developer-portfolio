# Rijin John — Django Developer Portfolio

A standalone Django portfolio project. It does not modify or depend on the Mr.Teeth clinic project.

## Features
- Dark navy + electric-blue responsive portfolio
- About, skills, projects, and contact sections
- Social/contact links and QR-code tiles for LinkedIn, GitHub, WhatsApp, and Instagram
- Featured Mr.Teeth and Tourism projects
- Configurable clinic website URL and portfolio public URL via environment variables
- Django admin-ready project

## Local setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

If PowerShell blocks activation, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Configure links
Edit `.env`:
- `PORTFOLIO_PUBLIC_URL` — leave blank until deployed; then set the public URL to generate a QR for the portfolio itself.
- `CLINIC_WEBSITE_URL` — add the public URL of the Mr.Teeth clinic website when available.
- `DJANGO_SECRET_KEY` — replace before deployment.
- `DEBUG=False` and `ALLOWED_HOSTS` for production.

## Deploy
This is a starter app, not yet deployed. Choose a Django-compatible host, set environment variables, run migrations, and configure static files. Never put secrets in public GitHub repositories.

## Notes
QR codes are generated from the actual configured destinations. The portfolio QR is shown as a placeholder until `PORTFOLIO_PUBLIC_URL` is set. The clinic link is shown as a placeholder until `CLINIC_WEBSITE_URL` is set.
