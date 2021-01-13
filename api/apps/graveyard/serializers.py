from rest_framework import serializers
from .models import Graveyard

class GraveyardSerializer(serializers.HyperlinkedModelSerializer):
    """
    API endpoint that allows User's Graveyard to be viewed or edited.
    """
    class Meta:
        model = Graveyard
        fields = ['plant_name']
