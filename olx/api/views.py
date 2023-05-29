from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Vehicles,Category
from api.serializers import VehicleSerializer,CategorySerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User
# Create your views here.
#localhost/8000/api/vehicles/
#method:get
#method:post


class VehiclesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        print(request.query_params)
        if "fuel_type" in request.query_params:
            cat=request.query_params.get("fuel_type")
            qs=qs.filter(fuel_type=cat)
        if "location" in request.query_params:
            loc=request.query_params.get("location")
            qs=qs.filter(location=loc)
        serializer=VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

#localhost:8000/api/vehicles/{id}
class VehicleDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicles.objects.get(id=id)
        serializer=VehicleSerializer(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Vehicles.objects.get(id=id)       
        serializer=VehicleSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Vehicles.objects.get(id=id) 
        obj.delete()
        return Response(data="deleted")


class CategoriesView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Category.objects.all()
        serializer=CategorySerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    #localhost:api/categories/1
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Category.objects.get(id=id)
        serializer=CategorySerializer(qs,many=False)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Category.objects.get(id=id)
        serializer=CategorySerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.get(id=id).delete()
        return Response(data="deleted")
    
class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    model=User
    queryset=User.objects.all()
