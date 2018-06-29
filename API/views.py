# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from rest_framework import generics
from rest_framework import viewsets

from .models import Campaigns
from .serializer import CampaignsSerializer


class ListCampaigns(viewsets.ModelViewSet):
    queryset = Campaigns.objects.all()
    serializer_class = CampaignsSerializer
