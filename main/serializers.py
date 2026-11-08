from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Education

class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

#ModelSerializer memvalidasi Education, sedangkan star_count dan 
#is_starred dihitung server. Field degree_display adalah improvisasi 
#agar UI menampilkan nama jenjang yang mudah dibaca. Email dan password 
#pengguna tidak diekspos.
class EducationSerializer(serializers.ModelSerializer):
    """Representasi Education dengan data star yang aman untuk publik."""

    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    degree_display = serializers.CharField(
        source="get_degree_display", read_only=True
    )

    class Meta:
        model = Education
        fields = [
            "id",
            "title",
            "description",
            "major",
            "degree",
            "degree_display",
            "thumbnail",
            "star_count",
            "is_starred",
        ]
        read_only_fields = ["id"]

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.starred_by.filter(pk=request.user.pk).exists()

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Nama institusi tidak boleh kosong."
            )
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Deskripsi tidak boleh kosong."
            )
        return value

    def validate_major(self, value):
        if value is None:
            return value
        return strip_tags(value).strip()
