

from django import forms
from .models import itemModel, stationModel, paymentModel, smsModel
  
  
# creating a form
class itemForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = itemModel
  
        # specify fields to be used
        fields = [

            "itemType",  
            "itemName",              
            "sendFrom",              
            "stationName",           
            "senderName",             
            "senderPhone",           
            "destination",           
            "destinationStaff",       
            "destinationStaffPhone",  
            "receiverName",           
            "receiverPhone", 

        ]

class stationForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = stationModel
  
        # specify fields to be used
        fields = [

            "stationName",
            "stationLocation",
            "stationStaff",         
            "stationPhone",        
        ]

class paymentForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = paymentModel
  
        # specify fields to be used
        fields = [

            "itemName",          
            "destination",          
            "amount",               
            "paid",                 
            "balance",              
            "phone",               
            "paymentMeans",         
        ]

class smsForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = smsModel
  
        # specify fields to be used
        fields = [
            
            "receiver",
            "receiverPhone",
            "message",
        ]

    

