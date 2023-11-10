from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from flight.models import Schedule, Route
from amonic.models import Office, User
from amonic.serializers import EditRoleSerializer
from tickets.models import Tickets
from tickets.serializers import TicketsSerializer, TicketsListSerializer
from flight.serializers import SchedulesListSerializer
from rest_framework.response import Response
import datetime
from operator import itemgetter

from django.utils import timezone
# Create your views here.
from rest_framework.decorators import api_view
@api_view(['GET'])
def FlightView(request):
  now = timezone.now()
  
  delta = datetime.timedelta(30)

  schedule = Schedule.objects.filter(date__range=[now - delta, now], confirmed=1)
  scheduleRouteIds = Schedule.objects.filter(date__range=[now - delta, now], confirmed=1).values_list('route', flat=True)
  scheduleIds = Schedule.objects.filter(date__range=[now - delta, now], confirmed=1).values_list('id', flat=True)
  schedule2 = Schedule.objects.filter(date__range=[now - delta, now], confirmed=0)
  
  routesTime = Route.objects.filter(id__in=scheduleRouteIds).values_list('flight_time', flat=True)
  tickets = TicketsSerializer(Tickets.objects.filter(schedule__in=scheduleIds), many=True).data
  ticketsUsersIds = Tickets.objects.filter(schedule__in=scheduleIds).values_list('user', flat=True)
  office = {}
  for userId in ticketsUsersIds:
    userData = EditRoleSerializer(User.objects.get(pk=userId)).data
    if userData.get('office_id') in office:
      office[userData.get('office_id')] += 1
    else:
      office[userData.get('office_id')] = 1
      
  data = {}
  
  for i in tickets:
    key = f"{i.get('passport_country')} {i.get('passport_number')}/{i.get('first_name')} {i.get('last_name')}"
    if key in data:
      data[key] += 1
    else:
      data[key] = 1
  
  sort = sorted(data.items(), key=itemgetter(1), reverse=True)  
  top_three_values = sort[:3]

  sortOffice = sorted(office.items(), key=itemgetter(1), reverse=True)  
  top_three_office = sortOffice[:3]

  

  sum = 0
  for i in routesTime:
    sum += i
  sum = sum / len(routesTime)

  scheduleSerializer = SchedulesListSerializer(schedule, many=True).data
  countFlight = {}

  max = {
    "date": None,
    "count": -1
  }
  min = {
    "date": None,
    "count": 1000000000
  }


  for i in scheduleSerializer:
    if i.get('date') in countFlight:
      countFlight[i.get('date')] += 1
    else:
      countFlight[i.get('date')] = 1

  for i in countFlight:
    if countFlight.get(i) < min.get("count"):
      min = {
        "date": i,
        "count": countFlight.get(i)
      }
    
    if countFlight.get(i) > max.get("count"):
      max = {
        "date": i,
        "count": countFlight.get(i)
      }

  # доходы
  yesterdaySchedule = SchedulesListSerializer(Schedule.objects.filter(date=now - datetime.timedelta(1)), many=True).data
  tooDaysSchedule = SchedulesListSerializer(Schedule.objects.filter(date=now - datetime.timedelta(2)), many=True).data
  threeDaysSchedule = SchedulesListSerializer(Schedule.objects.filter(date=now - datetime.timedelta(3)), many=True).data

  yesterdayTickets = TicketsListSerializer(Tickets.objects.filter(schedule__in=list(map(lambda x: x.get('id'), yesterdaySchedule))), many=True).data
  tooDaysTickets = TicketsListSerializer(Tickets.objects.filter(schedule__in=list(map(lambda x: x.get('id'), tooDaysSchedule))), many=True).data
  threeDaysTickets = TicketsListSerializer(Tickets.objects.filter(schedule__in=list(map(lambda x: x.get('id'), threeDaysSchedule))), many=True).data
  
  ticketsSave = {
    "yesterday": 0,
    "tooDays": 0,
    "threeDays": 0,
  }

  for i in yesterdayTickets:
    if i["cabin_type"]['id'] == 1:
      ticketsSave['yesterday'] += i['schedule']['economy_price']
    elif i["cabin_type"]['id'] == 2:
      ticketsSave['yesterday'] += i['schedule']['business_price']
    else:
      ticketsSave['yesterday'] += i['schedule']['first_class_price']
  
  for i in tooDaysTickets:
    if i["cabin_type"]['id'] == 1:
      ticketsSave['tooDays'] += i['schedule']['economy_price']
    elif i["cabin_type"]['id'] == 2:
      ticketsSave['tooDays'] += i['schedule']['business_price']
    else:
      ticketsSave['tooDays'] += i['schedule']['first_class_price']
  
  for i in threeDaysTickets:
    if i["cabin_type"]['id'] == 1:
      ticketsSave['threeDays'] += i['schedule']['economy_price']
    elif i["cabin_type"]['id'] == 2:
      ticketsSave['threeDays'] += i['schedule']['business_price']
    else:
      ticketsSave['threeDays'] += i['schedule']['first_class_price']

  thisWeekSchedule = SchedulesListSerializer(Schedule.objects.filter(date__range=[now - datetime.timedelta(7), now]), many=True).data
  lastWeekSchedule = SchedulesListSerializer(Schedule.objects.filter(date__range=[now - datetime.timedelta(14), now - datetime.timedelta(7)]), many=True).data
  tooWeekSchedule = SchedulesListSerializer(Schedule.objects.filter(date__range=[now - datetime.timedelta(21), now - datetime.timedelta(14)]), many=True).data

  emptySeats = {
    'this': {
      "allSeats": 0,
      "countTicket": 0
    },
    'last': {
      "allSeats": 0,
      "countTicket": 0
    },
    'too': {
      "allSeats": 0,
      "countTicket": 0
    },
  }

  for i in thisWeekSchedule:
    emptySeats['this']['allSeats'] += i.get('aircraft').get('total_seats')
    emptySeats['this']['countTicket'] += len(Tickets.objects.filter(schedule=i.get('aircraft').get('id')))
  for i in lastWeekSchedule:
    emptySeats['last']['allSeats'] += i.get('aircraft').get('total_seats')
    emptySeats['last']['countTicket'] += len(Tickets.objects.filter(schedule=i.get('aircraft').get('id')))
  for i in tooWeekSchedule:
    emptySeats['too']['allSeats'] += i.get('aircraft').get('total_seats')
    emptySeats['too']['countTicket'] += len(Tickets.objects.filter(schedule=i.get('aircraft').get('id')))

  return Response({
    "confirmed": len(SchedulesListSerializer(schedule, many=True).data),
    "notConfirmed": len(SchedulesListSerializer(schedule2, many=True).data),
    "average": sum,
    "min": min,
    "max": max,
    "top_three_values": top_three_values,
    "top_three_office": top_three_office,
    'ticketsSave': ticketsSave,
    # "thisWeekSchedule": thisWeekSchedule,
    "emptySeats": emptySeats
  })
