from django.conf.urls import url,include
from django.contrib import admin

from api.views import shopping_car,auth
urlpatterns = [
    url(r"shoppingcar/",shopping_car.ShoppingCar.as_view({"get":"list","post":"create","put":"update","delete":"dd"})),

    url(r"auth/",auth.AuthView.as_view({"post":"login"}))
]