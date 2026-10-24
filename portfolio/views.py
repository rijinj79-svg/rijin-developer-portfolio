import io
import os
import qrcode
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render

LINKS = {
    "github": "https://github.com/rijin79-svg",
    "linkedin": "https://www.linkedin.com/in/rijin-john-786884316",
    "instagram": "https://www.instagram.com/rijin_jo/",
    "whatsapp": "https://wa.me/917994069644",
    "email": "mailto:rijinj79@gmail.com",
    "phone": "tel:+917994069644",
}

def home(request):
    portfolio_url = os.getenv("PORTFOLIO_PUBLIC_URL", "").strip()
    clinic_url = os.getenv("CLINIC_WEBSITE_URL", "").strip()
    context = {
        "links": LINKS,
        "portfolio_url": portfolio_url,
        "clinic_url": clinic_url,
        "qr_services": [
            {"key": "linkedin", "label": "LinkedIn", "description": "Connect professionally"},
            {"key": "github", "label": "GitHub", "description": "Explore my code"},
            {"key": "whatsapp", "label": "WhatsApp", "description": "Start a conversation"},
            {"key": "instagram", "label": "Instagram", "description": "Follow my journey"},
        ],
    }
    return render(request, "portfolio/home.html", context)

def qr_code(request, service):
    destinations = dict(LINKS)
    destinations["portfolio"] = os.getenv("PORTFOLIO_PUBLIC_URL", "").strip()
    destinations["clinic"] = os.getenv("CLINIC_WEBSITE_URL", "").strip()
    destination = destinations.get(service, "")
    if not destination:
        raise Http404("This QR destination has not been configured yet.")
    image = qrcode.make(destination)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")
