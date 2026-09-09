from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Deandra Yudasswara",
        "npm": "2506592743",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Also known as srzgy. EDM enthusiast. Sometimes reads visual novels. Rank #21k global on osu!std. Supports Tottenham Hotspur. Oh, and also somewhat a computer scientist."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Deandra Yudasswara",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
