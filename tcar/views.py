from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404, HttpResponse
from rest_framework import generics
import time

from .models import Device, DeviceSerializer

class IndexView(ListView):
    template_name = 'tcar/index.html'
    model = Device

class DeviceAPIView(generics.RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

def api_tcar_controls(request, pk):    
    for _ in range(30):
        try:
            device = Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404("Device does not exist")
        
        if device.state != device.next_state:
            device.state = device.next_state
            device.save()
            return HttpResponse(device.state)
        time.sleep(0.1)
    return HttpResponse()