# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render
from .models import Campaigns
from .serializer import CampaignsSerializer
from .serializer import locationSerializer
from .models import locations

class ListCampaigns(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer
class ListLocations(viewsets.ModelViewSet):
    queryset = locations.objects.all()
    serializer_class = locationSerializer





def push_test(request):
    return render(request, 'index.html')
