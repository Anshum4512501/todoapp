from unittest.main import main
from django.contrib.auth.models import User
from django.test import TestCase
from .models import ToDo
from django.utils import timezone
from django.urls import reverse
from .forms import ToDoForm
from django.test import Client

# models test
class ToDoTest(TestCase):

    def setUp(self) -> None:
        user = User(username="testuser")
        user.set_password("Anshoo@123")
        user.save()
        todo = ToDo(title="test title",description="test description",important=True)
        # print(User.objects.filter(username="sachin"))
        users = User.objects.all()
        # user = User.objects.get(username="sachin")
        todo.user = user
        print(users)
        todo.save()

    # def create_ToDo(self, title="only a test", body="yes, this is only a test"):
    #     return ToDo.objects.create(title=title, body=body, created_at=timezone.now())

    def test_ToDo_creation(self):
        instance = ToDo.objects.get(id=1)
        print(instance)
        self.assertTrue(isinstance(instance, ToDo))
        # self.assertEqual(w.__unicode__(), w.title)

    def test_login_test(self):
        c = Client()
        response = c.post('/signin/', {'username': 'anshum45', 'password': 'Anshoo12@#',"csrftoken":"MuaKA6jR9vS0yk4Wp0O1mbWMCJaMw5dL3kQao1gxhbzSt24erVB8sHxSZBSnGFYn"})
        self.assertEqual(response.status_code,200)



        




# Create your tests here.
