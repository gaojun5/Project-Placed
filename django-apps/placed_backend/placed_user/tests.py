from django.test import TestCase
from django.db import IntegrityError
from placed_user.models import PlacedUser
from rest_framework import status
from rest_framework.test import APITestCase


class PlaceUserModelTestCase(TestCase):
    fixtures = ['data/course.json', 'data/group.json', 'data/skill.json']

    def test_create_user_academics(self):
        user = PlacedUser.objects.create_user('jgarcia@gmail.com', 'Javier', 'Garcia', group="Academics Project Coordinator", institution="Iberzal")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, 'jgarcia@gmail.com')
        self.assertEqual(user.first_name, 'Javier')
        self.assertEqual(user.last_name, 'Garcia')
        self.assertEqual(user.institution, 'Iberzal')
        self.assertFalse(user.is_active)
        self.assertEqual(user.group.name, 'Academics Project Coordinator')

    def test_duplicate_email(self):
        PlacedUser.objects.create_user('jgarcia@gmail.com', 'Javier', 'Garcia', group="Academics Project Coordinator", institution="Iberzal")
        with self.assertRaises(IntegrityError):
            PlacedUser.objects.create_user('jgarcia@gmail.com', 'Javier', 'Garcia', group="Academics Project Coordinator", institution="Iberzal")


class PlacedUserAPITestCase(APITestCase):
    fixtures = ['data/course.json', 'data/group.json', 'data/skill.json', 'data/user.json']

    def test_register_user(self):
        data = {
            "email": "jgarcia@gmail.com",
            "first_name": "Javier",
            "last_name": "Garcia",
            "institution": "Iberzal",
            "group": "Academics Project Coordinator"
        }
        response = self.client.post('/api/1/users/register', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        try:
            user = PlacedUser.objects.get(id=response.data['id'])
            self.assertEqual(user.email, 'jgarcia@gmail.com')
        except Exception as e:
            self.fail(e)

    def test_duplicate_email(self):
        data = {
            "email": "jgarcia@gmail.com",
            "first_name": "Javier",
            "last_name": "Garcia",
            "institution": "Iberzal",
            "group": "Academics Project Coordinator"
        }
        self.client.post('/api/1/users/register', data, format="json")
        response = self.client.post('/api/1/users/register', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Email already registered')

    def test_signin(self):
        data = {
            "username": "jgarcia@iberzal.com",
            "password": "12345",
        }
        response = self.client.post('/api/1/users/api-token-auth/', data, format="json")
        self.assertTrue('token' in response.data)

    def test_bad_signin(self):
        data = {
            "username": "jgarcia@iberzal.com",
            "password": "123456",
        }
        response = self.client.post('/api/1/users/api-token-auth/', data, format="json")
        self.assertTrue(response.status_code == status.HTTP_400_BAD_REQUEST)

    def test_get_my_user(self):
        data = {
            "username": "jgarcia@iberzal.com",
            "password": "12345",
        }
        response = self.client.post('/api/1/users/api-token-auth/', data, format="json")
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/1/users/me')
