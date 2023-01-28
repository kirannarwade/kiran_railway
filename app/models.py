from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Todo From " + str(self.user)

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Messege From " + str(self.user)




GENDER_CHOICES = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)

HOBBIES_CHOICES = (
    ('Dance','Dance'),
    ('Cycling','Cycling'),
    ('Reading','Reading'),
    ('Programming','Programming'),
    ('Others','Others'),
)


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10,10}$')])
    hobbies = models.CharField(choices=HOBBIES_CHOICES, max_length=30)
    messege = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
