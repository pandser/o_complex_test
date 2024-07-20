from rest_framework import serializers

from app.models import City


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = City
        fields = (
            'name',
            'count',
        )
