from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarModel

from .serializers import CarSerializer, CarsSerializerAll


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()

        serializer = CarsSerializerAll(cars, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()

        return Response(serializer.data)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not Found')

        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not Found')

        serializer = CarSerializer(car, data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not Found')

        serializer = CarSerializer(car, data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not Found')

        car.delete()

        return Response('deleted')
