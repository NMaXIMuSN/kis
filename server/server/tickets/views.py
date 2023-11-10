from django.shortcuts import render
import json
import datetime
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from flight.serializers import SchedulesListSerializer
from flight.models import Schedule
from  .models import Tickets, AmenitiesTickets, Amenities, CabinTypes, AmenitiesCabinType
from  .serializers import TicketsSerializer, AmenitiesSerializer, AmenitiesTicketSerializer, TicketsListSerializer, CabinTypesSerializer, AmenitiesCabinTypeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class TicketsAddView(CreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TicketsListView(ListAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsListSerializer
    filterset_fields = ['booking_reference']

class AmenitiesGetListByPkView(ListCreateAPIView):
    queryset = AmenitiesTickets.objects.all()
    serializer_class = AmenitiesTicketSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return AmenitiesTickets.objects.filter(ticket=pk)

    def post(self, request, *args, **kwargs):
        req_body = json.loads(request.body)
        AmenitiesTickets.objects.filter(ticket=self.kwargs['pk']).delete()
        newAmenities = []

        for id in req_body:
            amenities = Amenities.objects.get(pk = id)
            amenitiesSerializer = AmenitiesSerializer(amenities).data
            amenitiesObj = {
                "price": amenitiesSerializer["price"],
                "amenity": amenitiesSerializer['id'],
                "ticket": self.kwargs['pk']
            }
            newAmenities.append(amenitiesObj)

        serializer = self.get_serializer(data=newAmenities, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        
        


class AmenitiesListView(ListAPIView):
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer

class AmenitiesCabinTypeListView(ListAPIView):
    queryset = AmenitiesCabinType.objects.all()
    serializer_class = AmenitiesCabinTypeSerializer

@api_view(["GET"])        
def amenitiesStats(request):
    params = request.query_params
    gg = {}
    if params.get('date') or params.get('flight_number'):
        amenitiesCabinType = CabinTypes.objects.all().values_list('id', flat=True)
        amenities = Amenities.objects.all().values_list('id','service')

        amenitiesIdKey = {}
        for (id, service) in amenities:
            amenitiesIdKey[id] = service
        
        res = {}
        for i in amenitiesCabinType:
            res[i] = []
            if i not in gg:
                gg[i] = {}

            for (id, service) in amenities:
                gg[i][service] = 0
        
        if params.get('date') and params.get('flight_number'):
            schedule = Schedule.objects.filter(date=params.get('date'), flight_number=params.get('flight_number')).values_list('id', flat=True).order_by("id")
        else:
            a = Schedule.objects.filter(date=params.get('date')) | Schedule.objects.filter(flight_number=params.get('flight_number'))
            schedule = a.values_list('id', flat=True).order_by("id")

        tickets = Tickets.objects.filter(schedule__in=schedule).values_list('id','cabin_type').order_by("id")
        for (i, j) in tickets:
            res[j].append(i)

        for i in res:
            amenitiesTickets = AmenitiesTicketSerializer(AmenitiesTickets.objects.filter(ticket__in=res[i]), many=True).data
            for j in amenitiesTickets:
                gg[i][amenitiesIdKey[j.get('amenity')]] = gg[i][amenitiesIdKey[j.get('amenity')]] + 1

    return Response(gg)
        

class TicketsAmenitiesView(CreateAPIView):
    queryset = AmenitiesTickets.objects.all()
    serializer_class = AmenitiesTicketSerializer