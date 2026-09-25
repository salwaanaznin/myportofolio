from main.models import Experience
from main.models import Education
from main.forms import ProjectForm, EducationForm
from main.models import Project
import datetime

from django.contrib.auth.decorators import login_required   
from django.core.exceptions import PermissionDenied       

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods



def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Salwa Alyani Naznin",
        "npm": "2506622802",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Currently navigating my tech journey as a university student, passionate about software engineering, problem-solving, and technology. Beyond coding, I am committed to supporting diversity in STEM and building space for women to thrive in technology."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Salwa's portofolio",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

#education

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")


def show_education(request):
    json_response = get_education_json(request)
    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education_list = [entry.object for entry in education]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Salwa's portofolio",
        "education_list": education_list,
        "title_query": title_query,
    }
    return render(request, "education.html", context)

@require_http_methods(["GET", "POST"])
def create_education(request):
    form = EducationForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Salwa's portofolio",
        "form": form,
        "page_title": "Tambah Pendidikan",
        "submit_label": "Tambah Pendidikan",
    }
    return render(request, "education_form.html", context)


@require_http_methods(["GET", "POST"])
def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(
        request.POST if request.method == "POST" else None,
        instance=education,
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Salwa's portofolio",
        "form": form,
        "page_title": "Edit Pendidikan",
        "submit_label": "Simpan Perubahan",
    }
    return render(request, "education_form.html", context)


@require_http_methods(["GET", "POST"])
def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    context = {
        "name": "Salwa's portofolio",
        "education": education,
    }
    return render(request, "education_confirm_delete.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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
    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
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

@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")