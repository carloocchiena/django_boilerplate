from django.test import TestCase
from django.test import TransactionTestCase
from django.contrib.auth import get_user_model

from . import models

# Create your tests here.

# testing the model

TEST_USER = {
    'username': 'caxthetyx',
    'password': 'bvQ7%rpxz2*4o2',
}

class ProfileTests(TransactionTestCase):

    def test_whether_user_profile_created_on_user_creation_signal(self):
        django_user_model = get_user_model().objects.create_user(
            TEST_USER['username'], TEST_USER['password']
        )
        custom_profile = models.Profile.objects.get(user=django_user_model)
        self.assertEqual(custom_profile.user, django_user_model)
        