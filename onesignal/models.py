from django.db import models
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
import requests
import random
import json

# Create your models here.
class GroupSignal(models.Model):
    class Meta:
        abstract = True

    # def push_all(self, data, devices):
        # """
        # This method pushes notification onto all devices that share
        # a common local user id. 
# 
        # This method uses device_id tag value
        # to identify the devices. It should be avoided due to not
        # allowing more than 99 fields.
        # """
# 
        # devices = list(devices)
        # assert len(devices) > 0, 'No devices to send!'
# 
        # SIZE    = 99
        # groups  = [devices[ind * SIZE:(ind + 1) * SIZE] 
            # for ind in range(0, len(devices)//SIZE + 1)]
# 
        # auth    = "Basic %s" % settings.ONE_SIGNAL_API_KEY
# 
        # headers = {
        # "Content-Type": "application/json; charset=utf-8",
        # "Authorization": auth}
# 
        # for ind in groups:
            # self.http_post(data, ind, headers)
# 
    # def http_post(self, data, devices, headers):
        # url = 'https://onesignal.com/api/v1/notifications'
        # targets = []
# 
        # for ind in range(0, len(devices) - 1):
            # targets.extend(({"field": "tag", "relation": "=", 'key': 'device_id', 
                # 'value':'device-%s' % devices[ind] }, {'operator':'OR'}))
# 
        # targets.append({"field": "tag", "relation": "=", 'key': 'device_id',
                # 'value':'device-%s' % devices[-1]})
# 
        # payload = {
        # 'app_id': settings.ONE_SIGNAL_APPID, 
        # "filters": targets}
# 
        # payload.update(data)
        # req = requests.post(url, data=json.dumps(payload), headers=headers)

    def push(self, data, devices):
        """
        """

        auth    = "Basic %s" % settings.ONE_SIGNAL_API_KEY

        headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": auth}

        url = 'https://onesignal.com/api/v1/notifications'

        payload = {
        'app_id': settings.ONE_SIGNAL_APPID, 
        "include_player_ids": list(devices)}

        payload.update(data)
        req = requests.post(url, data=json.dumps(payload), headers=headers)

class Device(GroupSignal):
    onesignal_id = models.CharField(null=False, blank=True, max_length=100)

    class Meta:
        abstract = True

    def reload_ui(self):
        url  = 'https://onesignal.com/api/v1/notifications'

        data = {'heading': {'en': 'Arcamens'},
        "contents": {"en": 'Organization switched successfully!'},
        'data': {'cmd': 'RELOAD-UI'}}

        auth    = "Basic %s" % settings.ONE_SIGNAL_API_KEY

        headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": auth}

        targets = [{"field": "tag", "relation": "=", 'key': 'device_id',
                'value':'device-%s' % self.id}]

        payload = {
        'app_id': settings.ONE_SIGNAL_APPID, 
        "filters": targets}

        payload.update(data)
        req = requests.post(url, data=json.dumps(payload), headers=headers)

    def init_onesignal(self):
        context = {
        'ONE_SIGNAL_APPID': settings.ONE_SIGNAL_APPID, 
        'device_id':  self.id}

        tmp     = get_template('onesignal/init_onesignal.html')
        html    = tmp.render(context)
        return html


