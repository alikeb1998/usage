from django.shortcuts import render
from rest_framework import viewsets
from . import models
from use import serializers


# Create your views here.
class FishViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = models.Fish.objects.all()
    serializer_class = serializers.FishSerializer
