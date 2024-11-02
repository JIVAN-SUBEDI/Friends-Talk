from django.urls import path
from .views import *
urlpatterns = [
path('feeling/',fellingView.as_view(),name='feeling'),
path('activity/',activityView.as_view(),name='activity'),
path('post/add/',addPostView.as_view(),name='Add post')
    
]
