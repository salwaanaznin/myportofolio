from django.shortcuts import render

from main.models import Experience
from main.models import Education


def show_main(request):
    context = {
        "name": "Salwa Alyani Naznin",
        "npm": "2506622802",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "find me at midnight"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salwa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

#education

def show_education(request):
    context = {
        "name": "Salwa",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)