from django.urls import path, include
from frontend.api.views import formView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('form', formView)

urlpatterns = [
    path('', include(router.urls)),
]