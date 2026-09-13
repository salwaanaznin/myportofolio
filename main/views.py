from django.shortcuts import render

from main.models import Experience
from main.models import Education


def show_main(request):
    context = {
        "name": "Salwa Alyani Naznin",
        "npm": "2506622802",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Currently navigating my tech journey as a university student, passionate about software engineering, problem-solving, and technology. Beyond coding, I am committed to supporting diversity in STEM and building space for women to thrive in technology."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salwa's portofolio",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

#education

def show_education(request):
    context = {
        "name": "Salwa's portofolio",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)