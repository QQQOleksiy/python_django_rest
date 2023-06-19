from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from .filters import car_filter_queryset
from .models import CarModel
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter_queryset(self.request.query_params)

    # def get(self, *args, **kwargs):
    #     cars = CarModel.objects.all()
    #
    #     serializer = CarSerializer(cars, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()