from django.test import TestCase
from django.urls import reverse

from .models import ProjectPhoto, Progets, Skills


class ProjectDetailViewTests(TestCase):
    def setUp(self):
        self.skill = Skills.objects.create(skill='Django')
        self.project = Progets.objects.create(
            name='Portfolio site',
            deskrp='A short project summary.',
            all_deskrp='A longer project description.',
            url='https://example.com/',
        )
        self.project.skills.add(self.skill)

    def test_detail_page_shows_project_information(self):
        response = self.client.get(
            reverse('project_detail', args=[self.project.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Portfolio site')
        self.assertContains(response, 'A short project summary.')
        self.assertContains(response, 'A longer project description.')
        self.assertContains(response, 'Django')
        self.assertContains(response, 'href="https://example.com/"')

    def test_project_card_links_to_detail_page(self):
        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertContains(
            response,
            reverse('project_detail', args=[self.project.pk]),
        )

    def test_main_page_displays_all_skills_in_one_list(self):
        Skills.objects.create(skill='Python')

        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django')
        self.assertContains(response, 'Python')
        self.assertEqual(len(response.context['skills']), 2)

    def test_detail_page_shows_multiple_project_photos(self):
        ProjectPhoto.objects.create(
            project=self.project,
            image='projects/gallery/screenshot-one.png',
            caption='Main screen',
        )
        ProjectPhoto.objects.create(
            project=self.project,
            image='projects/gallery/screenshot-two.png',
        )

        response = self.client.get(
            reverse('project_detail', args=[self.project.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/media/projects/gallery/screenshot-one.png')
        self.assertContains(response, '/media/projects/gallery/screenshot-two.png')
        self.assertContains(response, 'Main screen')
