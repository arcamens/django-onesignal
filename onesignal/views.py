from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
from django.conf import settings

# Create your views here.
class UpdateUuid(View):
    def get(self, request):
        Device = apps.get_model(settings.ONE_SIGNAL_DEVICE_APP, 
        settings.ONE_SIGNAL_DEVICE_MODEL)

        device = Device.objects.get(id=request.GET.get('device_id'))
        device.onesignal_id = request.GET.get('onesignal_id')
        device.save()

        print('Uuid updated  successfully!')
        return HttpResponse(status=200)


