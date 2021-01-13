from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .serializers import GraveyardSerializer, Graveyard


class GraveyardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User's Graveyard to be viewed or edited.
    """
    queryset = Graveyard.objects.all()
    serializer_class = GraveyardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
