from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project, Education
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


class EducationForm(ModelForm):
    """Form tambah dan edit pendidikan dengan validasi berdasarkan model Education."""
    class Meta:
        model = Education
        fields = [
            "title",
            "description",
            "major",
            "degree",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Institusi",
            "description": "Deskripsi",
            "major": "Jurusan",
            "degree": "Jenjang Pendidikan",
            "thumbnail": "URL Logo Institusi",
        }

        # Widget mengatur tampilan input; validasi tetap mengikuti field form/model.
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pendidikan dan kegiatanmu",
                    "rows": 3,
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "Sistem Informasi",
                    "maxlength": 255,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/logo.png",
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(
            self.cleaned_data["title"]
        ).strip()

        if not title:
            raise ValidationError(
                "Nama institusi tidak boleh hanya berisi tag HTML."
            )

        return title

    def clean_description(self):
        return strip_tags(
            self.cleaned_data["description"]
        ).strip()

    def clean_major(self):
        major = (
            self.cleaned_data.get("major")
            or ""
        )

        return strip_tags(
            major
        ).strip()