from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Person

people = Person.objects.all()

def person_phonenumber(req, number):
    person = get_object_or_404(Person, phonenumber=number)
    return render(req, 'person_phonenumber.html', {'person': person})

def person_name(req, person_name):
    person = get_object_or_404(Person, name=person_name)
    return render(req, 'person_name.html', {'person': person})

