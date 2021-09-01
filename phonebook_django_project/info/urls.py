from django.urls import path
from .views import person_phonenumber, person_name

urlpatterns = [
    path('persons/phonenumber/<str:number>/', person_phonenumber),
    path('persons/name/<str:person_name>/', person_name),
]