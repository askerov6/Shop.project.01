import django_filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


class LaptopFilter(django_filters.FilterSet):
    class Meta:
        model = Laptop
        fields = ['model']


class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LaptopFilter


class LaptopPhotoViewSet(viewsets.ModelViewSet):
    queryset = LaptopPhoto.objects.all()
    serializer_class = LaptopPhotoSerializer
