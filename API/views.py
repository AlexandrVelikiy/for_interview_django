from django.shortcuts import render
from rest_framework import viewsets

from API.serializers import PizzaSerializer
from pizza.models import Pizza


# Create your views here.
class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer