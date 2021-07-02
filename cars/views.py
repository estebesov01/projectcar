from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializers


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializers
    queryset = Car.objects.all()
