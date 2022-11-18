from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Project

class ProjectTests(TestCase):
    #Test the Project Model
    def setUp(self):
        self.User=  get_user_model()
        self.user = self.User.objects.create_user(name='Maria da Silva',username='myusername', password='foo')
        
        self.project = Project(
            title = 'First Project',
            zip_code = '88010400',
            cost = '9500',
            done = False,
            deadline = '2022-12-31T00:00:00.000Z',
            username =  self.user
        )
    
    def test_create_project(self):
        self.assertIsInstance(self.project, Project)

    def test_str_representation(self):
        self.assertEquals(str(self.project), "First Project")


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(name='Maria da Silva',username='myusername', password='foo')
        self.assertEqual(user.name, 'Maria da Silva')
        self.assertEqual(user.username, 'myusername')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_admin)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username='')
        with self.assertRaises(ValueError):
            User.objects.create_user(name='Maria da Silva',username='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(name='Super',username='superusername', password='foo')
        self.assertEqual(admin_user.name, 'Super')
        self.assertEqual(admin_user.username, 'superusername')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_admin)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(name='Super',
                username='superusername', password='foo', is_admin=False)