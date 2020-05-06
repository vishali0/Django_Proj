from django.shortcuts import render

from.import views
# Create your views here.
from rest_framework import viewsets

from .serializers import membersSerializer
from .models import members


class membersViewSet(viewsets.ModelViewSet):
    queryset = members.objects.all().order_by('real_name')
    serializer_class = membersSerializer
