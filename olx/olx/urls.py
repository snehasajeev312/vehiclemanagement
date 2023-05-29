"""olx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from VehicleFrst import views as vehicle_views
from rest_framework.routers import DefaultRouter
from myapp import views as myapp_views
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("categories",views.CategoriesView,basename="categories")
router.register("users",views.UsersView,basename="users")
router.register("api/v2/users",myapp_views.RegistrationView,basename="accounts")
router.register("api/v2/categories",myapp_views.CategoriesView,basename="categories")
router.register("api/v2/vehicles",myapp_views.VehiclesView,basename="vehicles")
router.register("api/v2/wishlist",myapp_views.WishListView,basename="wishlist")
router.register("api/v2/question",myapp_views.QuestionView,basename='questions')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",vehicle_views.SignUpView.as_view(),name="signup"),
    path("",vehicle_views.SignInView.as_view(),name="signin"),
    path("vehicle/add",vehicle_views.VehicleCreateView.as_view(),name="vehicle-add"),
    path("logout",vehicle_views.signout_view,name="signout"),
    path("home",vehicle_views.IndexView.as_view(),name="home"),
    path("api/vehicles/",views.VehiclesView.as_view()),
    path("api/vehicles/<int:pk>/",views.VehicleDetailView.as_view()),
    path("api/v2/token/",ObtainAuthToken.as_view())
]+router.urls
