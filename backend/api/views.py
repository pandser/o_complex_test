from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import CitySerializer
from app.models import City


class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.values('name').annotate(
        count=Count('city__city')
    )
    serializer_class = CitySerializer
