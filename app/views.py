# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.template import loader
from django.http import HttpResponse
from django import template

from .forms import itemForm, smsForm, stationForm, paymentForm, smsForm
from .models import itemModel, stationModel, paymentModel, smsModel


@login_required(login_url="/login/")
def index(request):
    dataItems = itemModel.objects.all()
    # Count Entries
    countItems = itemModel.objects.all().filter(status='On Fleet').count()
    couriers = itemModel.objects.all().filter(status='On Fleet',itemType='Courier').count()
    parcels  = itemModel.objects.all().filter(status='On Fleet',itemType='Parcel').count()
    countStations = stationModel.objects.all().count()
    countPayments = paymentModel.objects.all().count()
    countSMS = smsModel.objects.all().count()

    context = {"couriers":couriers, "parcels":parcels, "countItems": countItems, "countStations": countStations, "countPayments": countPayments,
               "countSMS": countSMS, "dataItems": dataItems, 'segment': 'index'}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    # Station Form
    station_Form = stationForm()
    if request.method == "POST":
        station_Form = stationForm(request.POST)
        if station_Form.is_valid():
            station_Form.save()
    context = {
        "station_Form": station_Form
    }

    # Payment Form
    payment_Form = paymentForm()
    if request.method == "POST":
        payment_Form = paymentForm(request.POST)
        if payment_Form.is_valid():
            payment_Form.save()
    context = {
        "payment_Form": payment_Form
    }

    # SMS Form
    sms_Form = smsForm()
    if request.method == "POST":
        sms_Form = smsForm(request.POST)
        if sms_Form.is_valid():
            sms_Form.save()
    context = {"sms_Form": sms_Form, "dataItems": itemModel.objects.all(), "dataStations": stationModel.objects.all(),
               "dataPayments": paymentModel.objects.all(), "dataSms": smsModel.objects.all()}

    # List Data

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


# Item Register form
def createItemForm(request):
    # Item Form
    item_Form = itemForm()
    if request.method == "POST":
        item_Form = itemForm(request.POST)
        if item_Form.is_valid():
            item_Form.save()
        return HttpResponseRedirect("/getAllItems.html")
    context = {
        "item_Form": item_Form
    }

    return render(request, "createItem.html", context)


# Station Register form
def createStationForm(request):
    # Item Form
    station_Form = stationForm()
    if request.method == "POST":
        station_Form = stationForm(request.POST)
        if station_Form.is_valid():
            station_Form.save()
    context = {
        "station_Form": station_Form
    }

    return render(request, "createStation.html", context)


# Station Register form
def createStationForm(request):
    # Item Form
    station_Form = stationForm()
    if request.method == "POST":
        station_Form = stationForm(request.POST)
        if station_Form.is_valid():
            station_Form.save()
    context = {
        "station_Form": station_Form
    }

    return render(request, "createStation.html", context)


# Payment Register form
def createPaymentForm(request):
    # Item Form
    payment_Form = paymentForm()
    if request.method == "POST":
        payment_Form = paymentForm(request.POST)
        if payment_Form.is_valid():
            payment_Form.save()
    context = {
        "payment_Form": payment_Form
    }

    return render(request, "createPayment.html", context)


# SMS Register form
def createSMSForm(request):
    # Item Form
    sms_Form = smsForm()
    if request.method == "POST":
        sms_Form = smsForm(request.POST)
        if sms_Form.is_valid():
            sms_Form.save()
            return HttpResponseRedirect("/getSMSlogs.html")
    context = {
        "sms_Form": sms_Form
    }

    return render(request, "createSMS.html", context)


def resendSMS(request):
    # Item Form
    if request.method == "POST":
        sms_Form = smsForm(request.POST)
        sms_Form.save()
        return HttpResponseRedirect("/getSMSlogs.html")
    context = {
        "sms_Form": sms_Form
    }


# Detailed Data
def showItem(request, id):
    # dictionary for initial data with 
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["item"] = itemModel.objects.get(id=id)

    return render(request, "showItem.html", context)


# Update Data

def editItem(request, id):
    # dictionary for initial data with 
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(itemModel, id=id)

    # pass the object as instance in form
    item_Form = itemForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if item_Form.is_valid():
        item_Form.save()
        return HttpResponseRedirect("/getAllItems.html")

    # add form dictionary to context
    context["item_Form"] = item_Form

    return render(request, "editItem.html", context)


# Update Data

# Delete Data

# delete view for details
# def deleteItem(request, id):
#     context ={}

#     item = get_object_or_404(itemModel, id = id)

#     if request.method =="POST":
#         item.delete()
#         return HttpResponseRedirect("/")

#     return render(request, "getAllItems.html", context)


# delete view for details
def deleteItem(request, id):
    # dictionary for initial data with 
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(itemModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/getAllItems.html")

    return render(request, "deleteItem.html", context)
