from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World')

class HelloLahore(View):
    def get(self, request):
        return HttpResponse('Hello Lahore')
    
def home(request):
    # form = ReservationForm()

    # if request.method == 'POST':
    #     form = ReservationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("Success!")
        
    return render(request, 'index.html')

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def get_reservations(request, id=None):
#     if request.method == 'GET':
#         reservations = Reservation.objects.all()
#         serializer = ReservationSerializer(reservations, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ReservationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method == 'PUT':
#         reservation = Reservation.objects.get(id=id)
#         serializer = ReservationSerializer(reservation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method == 'DELETE':
#         reservation = Reservation.objects.get(id=id)
#         reservation.delete()
#         return Response({"message": "Deleted with success!"})
    
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['last_name']
    search_fields = ['last_name']