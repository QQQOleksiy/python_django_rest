from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=25)
    year = serializers.IntegerField()
    number_of_seats = serializers.IntegerField()
    type_body = serializers.CharField(max_length=25)
    engine = serializers.FloatField()

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for k,v in validated_data.items():
            setattr(instance, k, v)

        instance.save()

        return instance


class CarsSerializerAll(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=25)
    year = serializers.IntegerField()