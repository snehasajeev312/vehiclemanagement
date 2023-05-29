from django.shortcuts import render
from django.contrib.auth.models import User
from api.models import Category,Vehicles,VehiclePics,WishList,Questions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from myapp.serializers import UserSerializer,CategorySerializer,VehicleSerializer,VehiclePicSerializer,WishListSerializer,QuestionSerializer,AnswerSerializer
from rest_framework import status
# Create your views here.

class RegistrationView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CategoriesView(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


 #localhost:8000/api/2/add_vehicle   
    @action(methods=["post"],detail=True)
    def add_vehicle(self,request,*args,**kwargs):
        cat=self.get_object()
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user,category=cat)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
#localhost:8000/categories/2/add_vehicle

class VehiclesView(viewsets.ModelViewSet):
    serializer_class=VehicleSerializer
    queryset=Vehicles.objects.all()
    http_method_names=["get","put","delete","post"]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Vehicles.objects.all()
        if "category" in request.query_params:
            cat=request.query_params.get("category")
            qs=qs.filter(category__name=cat)
        serializer=VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)
    
#localhost:8000/api/v2/vehicles/add_image
    @action(methods=["post"],detail=True)
    def add_image(self,request,*args,**kwargs):
        serializer=VehiclePicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vehicle=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    

#localhost:8000/api/v2/vehicles/2/wish_list

    @action(methods=["post"],detail=True)
    def wish_list(self,request,*args,**kwargs):
        veh=self.get_object()
        usr=request.user
        WishList.objects.create(vehicle=veh,user=usr)
        return Response(data="item has been added",status=status.HTTP_201_CREATED)
    
    @action(methods=["post"],detail=True)
    def ask_question(self,request,*args,**kwargs):
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,add=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
class WishListView(viewsets.ModelViewSet):
    serializer_class=WishListSerializer
    queryset=WishList.objects.all()
    http_method_names=["put","get","patch","delete"]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=WishList.objects.filter(user=request.user)
        serializer=WishListSerializer(qs,many=True)
        return Response(data=serializer.data)
    

#localhost:8000/api/v2/vehicles/2/ask_question


class QuestionView(viewsets.ModelViewSet):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

#localhost:8000/api/v2/questions/qid/add_answer/
    @action(methods=["post"],detail=True)
    def add_answer(self,request,*args,**kwargs):
        serializer=AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,question=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)