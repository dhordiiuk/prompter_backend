from rest_framework import viewsets
import django_filters.rest_framework as filters
from .serializers import ModeSerializer, WordSerializer
from .models import Mode, Word


class ModeView(viewsets.ModelViewSet):
    serializer_class = ModeSerializer
    queryset = Mode.objects.all()


class WordView(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = WordSerializer
    queryset = Word.objects.all()
    filterset_fields = ['mode']
