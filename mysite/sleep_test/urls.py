from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('name/',StudentView,basename="student")


urlpatterns = [
    path('',include(router.urls)), 
]
