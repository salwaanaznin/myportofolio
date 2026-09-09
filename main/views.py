from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Salwa",
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