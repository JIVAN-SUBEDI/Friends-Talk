from django.urls import path
from .views import *
urlpatterns = [
path('feeling/',fellingView.as_view(),name='feeling'),
path('activity/',activityView.as_view(),name='activity'),
path('posts/',PostView.as_view(),name='Add post'),
path('post/<int:pk>/',getPost.as_view(),name='retrive post'),
path('posts/<int:post_id>/like/',likeUnlikePost.as_view(),name='like post'),
path('posts/<int:post_id>/comment/', CommentPostView.as_view(), name='comment_post'),
path('comments/<int:comment_id>/', CommentPostView.as_view(), name='delete_comment'),
    
]
