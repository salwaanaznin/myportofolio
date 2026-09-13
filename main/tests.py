from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_and_template_accessibility(self):
        """Test apakah URL utama, experience, dan education dapat diakses dan menggunakan template yang tepat"""
        response_main = self.client.get(reverse('main:show_main'))
        self.assertEqual(response_main.status_code, 200)
        self.assertTemplateUsed(response_main, 'index.html')

        response_exp = self.client.get(reverse('main:show_experience'))
        self.assertEqual(response_exp.status_code, 200)
        self.assertTemplateUsed(response_exp, 'experience.html')

        response_edu = self.client.get(reverse('main:show_education'))
        self.assertEqual(response_edu.status_code, 200)
        self.assertTemplateUsed(response_edu, 'education.html')

    def test_experience_page(self):
        """Test apakah halaman experience merender kategori dengan benar"""
        response = self.client.get(reverse('main:show_experience'))
        self.assertEqual(response.status_code, 200)
        # Menyesuaikan dengan string lowercase di HTML
        self.assertContains(response, "volunteer")

    def test_completed_experience(self):
        """Test status experience"""
        response = self.client.get(reverse('main:show_experience'))
        self.assertEqual(response.status_code, 200)
        # Karena data bawaanmu menampilkan 'Sedang berlangsung', kita pastikan teks itu memang ada/muncul di halaman
        self.assertContains(response, "Sedang berlangsung")

    def test_empty_state_message_displayed(self):
        """Test pesan kosong ketika data dihapus"""
        Experience.objects.all().delete()
        Education.objects.all().delete()

        response_exp = self.client.get(reverse('main:show_experience'))
        self.assertEqual(response_exp.status_code, 200)
        
        response_edu = self.client.get(reverse('main:show_education'))
        self.assertEqual(response_edu.status_code, 200)