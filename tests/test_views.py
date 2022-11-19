from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from accounts.models import Project

from django.urls import reverse
from django.urls.base import resolve
from project_app.views import home
from project_app.forms import NewUserForm

class ProjectURLsTest(SimpleTestCase):
    "Test the catalogue URLs"

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resloves_to_homepage_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home)



class BaseTest(TestCase):
    def setUp(self) :
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.User=  get_user_model()
        self.user_created = self.User.objects.create_user(name='Maria da Silva',username='myusername', password='foo123456')
        
        
        self.user={
            'name':'Mario',
            'username':'mariousername',
            'password1':'##123456',
            'password2':'##123456'
        }

        
        return super().setUp()

        

class RegisterTest(BaseTest):
   def test_can_view_page_correctly(self):
       response=self.client.get(self.register_url)
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,'project_app/register.html')



   def test_can_register_user(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)
        invalid_data_dicts = [
            # Non-alphanumeric username.
            {
            'data':
            { 'username': 'foo/bar',
              'name': 'Foo',
              'password1': 'foo123456',
              'password2': 'foo123456' },
            'error':
            ('username', [u'Username must be Alpahnumeric or contain any of the following: ". @ + -" '])
            },
            # Already-existing username.
            {
            'data':
            { 'username': 'myusername',
              'name': 'Maria Dois',
              'password1': 'secret12',
              'password2': 'secret12' },
            'error':
            ('username', [u"Custom user com este Username já existe."])
            },
            # Mismatched passwords.
            {
            'data':
            { 'username': 'foo',
              'name': 'Foo',
              'password1': 'foo12345',
              'password2': 'bar12345' },
            'error':
            ('password2', [u"Os dois campos de senha não correspondem."])
            },
            #Short password 
            {
            'data':
            { 'username': 'abc',
              'name': 'Foo',
              'password1': 'foo',
              'password2': 'foo' },
            'error':
            ('password2', [u"Esta senha é muito curta. Ela precisa conter pelo menos 8 caracteres."])
            },
            ]

        for invalid_dict in invalid_data_dicts:
            form = NewUserForm(data=invalid_dict['data'])
            self.failIf(form.is_valid())
            self.assertEqual(form.errors[invalid_dict['error'][0]], invalid_dict['error'][1])

class LoginTest(BaseTest):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'project_app/login.html')
    def test_login_success(self):
        self.client.login(username=self.user_created.username, password='foo123456')
        response = self.client.post(self.login_url, {'username': self.user_created.username, 'password': 'foo123456'})
        self.assertEqual(response.status_code,302)
       
   
    def test_cantlogin_with_no_username(self):
        response= self.client.post(self.login_url,{'password':'passwped','username':''},format='text/html')
        self.assertEqual(response.status_code,401)
    def test_cantlogin_with_no_password(self):
        response= self.client.post(self.login_url,{'username':'passwped','password':''},format='text/html')
        self.assertEqual(response.status_code,401)
