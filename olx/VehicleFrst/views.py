from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from VehicleFrst.forms import RegistrationForm,LoginForm,VehicleForm
from django.views.generic import View,CreateView,FormView,TemplateView
from django.urls import reverse_lazy
from api.models import Vehicles

class IndexView(TemplateView):
    template_name="index.html"
   
class SignUpView(CreateView):
    model=User
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")

class SignInView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
         form=LoginForm(request.POST)
         if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd) 
            if usr:
                login(request,usr)
                return redirect("home")      
            else:
                return render(request,self.template_name,{"form":form})
            
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


class VehicleCreateView(CreateView):
    model=Vehicles
    form_class=VehicleForm
    template_name="vehicle-add.html"
    success_url=reverse_lazy("home")