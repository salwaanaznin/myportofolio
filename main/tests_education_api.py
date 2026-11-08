
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from main.models import Education

User = get_user_model()


class EducationAPITest(APITestCase):
    """Memastikan API Education mematuhi empat peran pengguna."""

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner_edu",
            email="owner@example.com",
            password="TestPassword123!",
        )
        self.editor = User.objects.create_user(
            username="editor_edu",
            password="TestPassword123!",
        )
        self.visitor = User.objects.create_user(
            username="visitor_edu",
            password="TestPassword123!",
        )

        editor_group = Group.objects.create(name="Editor")
        self.editor.groups.add(editor_group)

        self.education = Education.objects.create(
            title="Universitas Indonesia",
            description="Pendidikan sarjana",
            major="Ilmu Komputer",
            degree="S1",
        )

        self.list_url = reverse("api:education-list")
        self.detail_url = reverse(
            "api:education-detail",
            kwargs={"education_id": self.education.id},
        )
        self.star_url = reverse(
            "api:education-star",
            kwargs={"education_id": self.education.id},
        )

        self.payload = {
            "title": "SMA Negeri 1 Jakarta",
            "description": "Pendidikan menengah",
            "major": "IPA",
            "degree": "SMA",
            "thumbnail": "",
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["title"],
            "Universitas Indonesia",
        )
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

        self.assertNotIn("email", response.data)
        self.assertNotIn("password", response.data)

    def test_search_and_empty_results(self):
        response = self.client.get(
            self.list_url,
            {"title": "universitas"},
        )
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url,
            {"title": "tidak-ada"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_anonymous_cannot_write(self):
        count_before = Education.objects.count()

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.patch(
            self.detail_url,
            {"title": "Hacked"},
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.title,
            "Universitas Indonesia",
        )
        self.assertEqual(Education.objects.count(), count_before)

    def test_regular_user_cannot_manage_education(self):
        self.client.force_authenticate(user=self.visitor)
        count_before = Education.objects.count()

        self.assertEqual(
            self.client.post(
                self.list_url,
                self.payload,
                format="json",
            ).status_code,
            403,
        )

        self.assertEqual(
            self.client.patch(
                self.detail_url,
                {"title": "Changed"},
                format="json",
            ).status_code,
            403,
        )

        self.assertEqual(
            self.client.delete(self.detail_url).status_code,
            403,
        )

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.title,
            "Universitas Indonesia",
        )
        self.assertEqual(Education.objects.count(), count_before)

    def test_editor_can_patch_and_put(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"title": "UI Updated"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertEqual(self.education.title, "UI Updated")

        response = self.client.put(
            self.detail_url,
            {
                "title": "Universitas Indonesia",
                "description": "Deskripsi terbaru",
                "major": "Sistem Informasi",
                "degree": "S1",
                "thumbnail": "",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.description,
            "Deskripsi terbaru",
        )

    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)
        count_before = Education.objects.count()

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        self.assertEqual(Education.objects.count(), count_before)
        self.assertTrue(
            Education.objects.filter(pk=self.education.pk).exists()
        )

    def test_owner_can_create_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 201)

        new_id = response.data["id"]
        self.assertEqual(Education.objects.count(), 2)

        response = self.client.patch(
            self.detail_url,
            {"major": "Teknik Informatika"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(
            Education.objects.filter(pk=self.education.id).exists()
        )

        self.assertTrue(
            Education.objects.filter(pk=new_id).exists()
        )

    def test_invalid_title_is_rejected(self):
        self.client.force_authenticate(user=self.owner)
        count_before = Education.objects.count()

        payload = self.payload.copy()
        payload["title"] = "<b>   </b>"

        response = self.client.post(
            self.list_url,
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.data)
        self.assertEqual(Education.objects.count(), count_before)

    def test_html_tags_are_removed(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.patch(
            self.detail_url,
            {
                "title": "<b>Universitas Indonesia</b>",
                "description": "<script>alert(1)</script>Belajar",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.education.refresh_from_db()
        self.assertEqual(
            self.education.title,
            "Universitas Indonesia",
        )
        self.assertNotIn("<script>", self.education.description)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)

        payload = {
            **self.payload,
            "star_count": 999,
            "is_starred": True,
            "degree_display": "Custom",
        }

        response = self.client.post(
            self.list_url,
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(
            response.data["degree_display"],
            "Senior High School",
        )

    def test_star_requires_login_and_toggles(self):
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.education.starred_by.count(), 0)

        self.client.force_authenticate(user=self.visitor)

        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["star_count"], 1)
        self.assertTrue(response.data["is_starred"])

        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_missing_education_and_wrong_method(self):
        missing_url = reverse(
            "api:education-detail",
            kwargs={
                "education_id": "00000000-0000-0000-0000-000000000000"
            },
        )
        self.assertEqual(
            self.client.get(missing_url).status_code,
            404,
        )
        self.client.force_authenticate(user=self.visitor)
        self.assertEqual(
            self.client.get(self.star_url).status_code,
            405,
        )

    def test_session_authentication_enforces_csrf(self):
        csrf_client = APIClient(enforce_csrf_checks=True)
        logged_in = csrf_client.login(
            username="owner_edu",
            password="TestPassword123!",
        )
        self.assertTrue(logged_in)

        count_before = Education.objects.count()

        response = csrf_client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Education.objects.count(), count_before)

    def test_session_authentication_with_csrf(self):
        csrf_client = APIClient(enforce_csrf_checks=True)

        logged_in = csrf_client.login(
            username="owner_edu",
            password="TestPassword123!",
        )
        self.assertTrue(logged_in)

        csrf_client.get(reverse("main:show_education"))
        token = csrf_client.cookies["csrftoken"].value

        response = csrf_client.post(
            self.list_url,
            self.payload,
            format="json",
            HTTP_X_CSRFTOKEN=token,
        )

        self.assertEqual(response.status_code, 201)
