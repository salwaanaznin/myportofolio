from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.forms import ProjectForm
from main.models import Project

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render



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

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Salwa",
        "form": form,
    }
    return render(request, "project_form.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Salwa's portofolio",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")