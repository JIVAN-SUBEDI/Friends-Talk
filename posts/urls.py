from django.urls import path
from .views import *
urlpatterns = [
path('feeling/',fellingView.as_view(),name='feeling'),
path('activity/',activityView.as_view(),name='activity')
    
]
