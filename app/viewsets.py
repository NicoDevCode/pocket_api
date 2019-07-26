from rest_framework import viewsets
from .models import Pocket, CurentSpend
from .serializers import PocketSerializer, CurentSpendSerializer


class PocketViewSet(viewsets.ModelViewSet):
    queryset = Pocket.objects.all()
    serializer_class = PocketSerializer


class CurentViewSet(viewsets.ModelViewSet):
    queryset = CurentSpend.objects.all()
    serializer_class = CurentSpendSerializer
