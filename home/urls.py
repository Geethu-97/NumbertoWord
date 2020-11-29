from django.urls import path,include
from .views import home,convert
urlpatterns = [
    path('', home),
    path('convert',convert)
]