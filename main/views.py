from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience, Education

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ExperienceForm


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
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Deandra Yudasswara",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Deandra Yudasswara",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience added!")
        return redirect("main:show_experience")

    context = {
        "name": "Deandra Yudasswara",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted.")
        return redirect("main:show_experience")

    return redirect("main_show_experience")


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type = "application/json")