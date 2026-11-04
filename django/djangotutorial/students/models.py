from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    std_number = models.CharField(unique=True)
    bio = models.TextField(null=True, blank=True)
    age = models.SmallIntegerField(default=18)
    is_married = models.BooleanField(default=False)
