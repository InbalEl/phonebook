from django.db import models
from django.db.models.fields import CharField, EmailField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    name = CharField(max_length=50)
    email = EmailField(unique=True, default='no email provided')
    phonenumber = PhoneNumberField()
    address = CharField(max_length=100)

    def __str__(self):
        return self.name
