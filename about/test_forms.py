from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Mr Test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")


    def test_name_is_required(self):
        """ Test for valid name field """
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Yo my dude!'
        })
        self.assertFalse(form.is_valid(), msg="Name was not provided, but form is valid")


    def test_email_is_required(self):
        """ Test for valid email field """
        form = CollaborateForm({
            'name': 'Mr Test',
            'email': '',
            'message': 'dont forget to bring a test'
        })
        self.assertFalse(form.is_valid(), msg="Email was not provided, but form is valid")


    def test_message_is_required(self):
        """ Test for valid message field """
        form = CollaborateForm({
            'name': 'Mr Test',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message was not provided, but form is valid")
