from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from django.db.models import Q


class CityAPIList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityStreetAPIList(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Street.objects.filter(city_id=city_id)


class ShopAPI(generics.ListCreateAPIView):
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        street = self.request.GET.get('street')
        city = self.request.GET.get('city')
        open = self.request.GET.get('open')
        shops = Shop.objects.all()
        if street:
            shops = shops.filter(street_id=street)
        if city:
            shops = shops.filter(city_id=city)
        if open:
            open = int(open)
            time = datetime.now().time()
            if open == 0:
                shops = shops.filter(~(Q(open_time__lt=time)&Q(close_time__gte=time)))
            if open == 1:
                shops = shops.filter(Q(open_time__lt=time)&Q(close_time__gte=time))
        return shops


    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        res = []
        for i in serializer.data:
            res.append({
                "city": i["city"]["name"],
                "street": i["street"]["name"]
            })
        return Response(res)
