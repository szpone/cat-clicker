from django.shortcuts import render
from rest_framework import viewsets
from .models import Click
from rest_framework.response import Response
from .serializers import ClickSerializer
# Create your views here.


class ClickViewSet(viewsets.ModelViewSet):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
