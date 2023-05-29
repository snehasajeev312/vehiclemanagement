from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category,Vehicles,VehiclePics,WishList,Questions,Answer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Category
        fields="__all__"

class VehiclePicSerializer(serializers.ModelSerializer):
    class Meta:
        model=VehiclePics
        fields=["image"]



class WishListSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    vehicle=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=WishList
        fields=["user","vehicle","date"]

class AnswerSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    add=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)
    class Meta:
        model=Answer
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    add=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    question_answer=AnswerSerializer(read_only=True,many=True)
    class Meta:
        model=Questions
        fields=["id","user","add","date","question","question_answer"]



class VehicleSerializer(serializers.ModelSerializer):
     owner=serializers.CharField(read_only=True)
     category=serializers.CharField(read_only=True)
     vehicle_images=VehiclePicSerializer(many=True)
     querys=QuestionSerializer(read_only=True,many=True)
     class Meta:
         model=Vehicles
         fields="__all__"

     def create(self,validated_data):
         print(validated_data)
         return super().create(validated_data)