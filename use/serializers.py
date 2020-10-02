from rest_framework import serializers
from . import models


class FishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Fish
        fields = ('name', 'active', 'created')
