from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer
  permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [permissions.IsAuthenticated]

def index(request):
  return render(request, 'index.html', {})
