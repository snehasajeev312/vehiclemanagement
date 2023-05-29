from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import Vehicles

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        exclude=("status",)
        widgets={
            
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "number":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "owner_type":forms.TextInput(attrs={"class":"form-control"}),
            "km_driven":forms.TextInput(attrs={"class":"form-control"}),
            "date_of_purchase":forms.DateTimeInput(attrs={"class":"form-control","type":"date"}),
            "fuel_type":forms.Select(attrs={"class":"form-select"}),
            "owner":forms.Select(attrs={"class":"form-select"}),
            "category":forms.Select(attrs={"class":"form-select"}),
            "condition":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            
        }
