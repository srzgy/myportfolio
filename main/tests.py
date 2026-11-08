from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


class ExperienceTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="Fasilkom UI",
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
        self.assertEqual(self.experience.category, "Fasilkom UI")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, reverse("api:experience-list"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        api_response = self.client.get(reverse("api:experience-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.data[0]["title"], self.experience.title)
        self.assertEqual(api_response.data[0]["description"], self.experience.description)
        self.assertEqual(api_response.data[0]["category"], "Fasilkom UI")
        self.assertTrue(api_response.data[0]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experiences have been added or found yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        self.assertFalse(self.experience.is_ongoing)
        api_response = self.client.get(reverse("api:experience-list"))
        self.assertFalse(api_response.data[0]["is_ongoing"])


class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="S1 Ilmu Komputer",
            description="Currently surviving the 8 AM classes and the heavy organizational workload."
        )

    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_page_contains_data(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("api:education-list"))

        api_response = self.client.get(reverse("api:education-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.data[0]["institution"], "Universitas Indonesia")
        self.assertEqual(api_response.data[0]["degree"], "S1 Ilmu Komputer")
        self.assertTrue(api_response.data[0]["is_ongoing"])

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))
        self.assertContains(response, "No education history added or found yet.")
