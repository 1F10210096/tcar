from django.db import models
from rest_framework import serializers

class Device(models.Model):
    device = models.CharField(max_length=100)
    state = models.CharField(max_length=16, default='stop')
    next_state = models.CharField(max_length=16, default='stop')
    
    def __str__(self):
        return self.device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('next_state',)