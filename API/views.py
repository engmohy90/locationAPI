# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
from .models import Temperature
from .serializer import TemperatureSerializer
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
class Filter(rest_framework.FilterSet):
    class Meta:
        model = Temperature
        fields = {'temp':['exact'], 'date': ['lte', 'gte', 'lt', 'gt']}


class TemperatureViewSet(ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_class = Filter
    search_fields = ['date','temp']

@csrf_exempt
def send_push(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        mobileID = body['id']
        temp = body['temp']
        url = "https://onesignal.com/api/v1/notifications"

        payload = "{\n\t\"app_id\": \"c2639284-4e16-44a4-9c87-df4ec30c547e\",\n   \"included_segments\": [\"All\"],\n    \"contents\": {\"en\": \"refrigerator1 Temperature: " + str(temp) + "\"}\n    }"
        headers = {
            'content-type': "application/json",
            'authorization': "Basic MzI4NTQzYjItYWU1OC00YWExLWFhNjQtYTM0ZGJkNTAxNWI5",
            'cache-control': "no-cache",
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        res = json.loads(response.text)
        print(res)
        if('errors' in res.keys()):
            return JsonResponse({'error': 'did not send'})
        else:
            return JsonResponse({'sent': 'ok'})