# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

itemTypes = [
    ('Parcel','Parcel'),
    ('Courier','Courier'),
    ('Other','Other')
    ]

class stationModel(models.Model):
    
    stationName           = models.CharField(max_length = 200)
    stationLocation       = models.CharField(max_length = 200)
    stationStaff          = models.CharField(max_length = 200)
    stationPhone          = models.CharField(max_length = 200)
    status                = models.CharField(max_length = 200, null=True)
    createdAt             = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.stationName

class itemModel(models.Model):



    itemType               = models.CharField(max_length = 200, choices=itemTypes, default='Parcel')
    itemName               = models.CharField(max_length = 200)
    sendFrom               = models.CharField(max_length = 200)
    stationName            = models.CharField(max_length = 200)
    senderName             = models.CharField(max_length = 200)
    senderPhone            = models.CharField(max_length = 200)
    destination            = models.CharField(max_length = 200)
    destinationStaff       = models.CharField(max_length = 200)
    destinationStaffPhone  = models.CharField(max_length = 200)
    receiverName           = models.CharField(max_length = 200)
    receiverPhone          = models.CharField(max_length = 200)
    status                 = models.CharField(max_length = 200, default="On Fleet")
    createdAt              = models.DateTimeField(auto_now_add=True, null=True)

    destinantionStationKey = models.ForeignKey(stationModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName



class pricingModel(models.Model):
    
    fromStation          = models.CharField(max_length = 200)
    fromLocation         = models.CharField(max_length = 200)
    toStatation          = models.CharField(max_length = 200)
    toLocation           = models.CharField(max_length = 200)
    pricing              = models.CharField(max_length = 200)
    status               = models.CharField(max_length = 200, null=True)
    createdAt            = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fromStation



class paymentModel(models.Model):

    itemName              = models.CharField(max_length = 200)
    destination           = models.CharField(max_length = 200)
    amount                = models.CharField(max_length = 200)
    paid                  = models.CharField(max_length = 200)
    balance               = models.CharField(max_length = 200)
    phone                 = models.CharField(max_length = 200)
    paymentMeans          = models.CharField(max_length = 200)
    status                = models.CharField(max_length = 200, null=True)
    createdAt             = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.itemName

class smsModel(models.Model):

    receiver       = models.CharField(max_length = 200)
    receiverPhone  = models.CharField(max_length = 200)
    message        = models.TextField(max_length = 500)
    code           = models.CharField(max_length = 200, null=True)
    status         = models.CharField(max_length = 200, null=True)
    createdAt      = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.receiver