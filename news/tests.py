from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from .models import Article

class PodCastsTests(TestCase):
    def setUp(self):
        self.Article = Article.objects.create(
            title="My Awesome Podcast Episode",
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
        )

    def test_episode_content(self):
        self.assertEqual(self.Article.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.Article.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
        )


    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "My Awesome Podcast Episode")