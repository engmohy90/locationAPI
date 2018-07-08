# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Campaigns(models.Model):
    """
    model to save Campaigns Details

    """
    Custom_ID = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Status = models.CharField(
        choices=(('Enabled', 'Enabled'), ('Disabled', 'Disabled')),
        max_length=20)
    Type = models.CharField(
        choices=(
            ('Video', 'Video'), ('Native', 'Native'), ('Banner', 'Banner')),
        max_length=20)
    Stop_Date = models.DateField()
    Description = models.TextField()

class locations(models.Model):
    """
    model to save Campaigns Details

    """
    Name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    

