from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    messege = models.TextField()

    def __str__(self) -> str:
        return self.name