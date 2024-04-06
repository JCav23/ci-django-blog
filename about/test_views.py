from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        """
        Creates about me content
        """
        self.content = About(
            title="About Me", 
            content="This is about me.",
        )
        self.content.save()

    def test_render_about_page_with_collaborate_form(self):
        """
        Verifies get request for about me containing a collaboration form
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collab_submission(self):
        """
        test for posting a collab request
        """
        collab_data = {
            'name': 'Mr Test',
            'email': 'test@test.com',
            'message': 'collab request'
        }
        response = self.client.post(reverse('about'), collab_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request recieved! I endeavor to respond within 2 working days.',
            response.content
        )