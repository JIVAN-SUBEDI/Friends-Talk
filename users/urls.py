from django.urls import path

from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', loginView.as_view(), name='login'),
    path('profile/', profileView.as_view(), name='profile'),
    path('profile/update/<int:id>', changeProfileImageFromPhoto.as_view(), name='profile'),
    path('bio/update/', updateBio.as_view(), name='profile'),
    path('cover/update/', changeCoverImage.as_view(), name='profile'),
    path('cover/update/<int:id>', changeCoverImageFromPhoto.as_view(), name='profile'),
    path('photo/upload/',uploadPhoto.as_view()),
    path('workplace/',addWorkPlace.as_view()),
    path('workplace/<int:pk>/',editDeleteListworkplace.as_view()),
    path('college/',addCollege.as_view()),
    path('college/<int:pk>/',editDeleteListCollege.as_view()),
    path('places/',addPlaces.as_view()),
    path('places/<int:pk>/',editDeleteListPlaces.as_view()),
    path('basic-info/',profileContactView.as_view()),
    path('gender/update/',updateGenderView.as_view()),
    path('dob/update/',updateDobView.as_view()),
    path('relationship/update/',updateRelationshipView.as_view()),
    path('primary/update/',updatePrimaryView.as_view()),
    path('secondary/update/',updateSecondaryView.as_view()),
    path('images/',getImageView.as_view()),
    path('forgot-password/<str:email>', forgotPasswordView.as_view(), name='forgot-password'),
    path('verify-otp/<str:email>/<int:otp>', verifyForgotOtpView.as_view(), name='verify-otp'),
    path('resend/verification-link/<str:email>', resendVerificationlink.as_view(), name='resend'),
    path('friend-request/send/<int:receiver_id>/', SendFriendRequest.as_view(), name='send-friend-request'),
    path('friend-request/accept/<int:request_id>/', AcceptFriendRequest.as_view(), name='accept-friend-request'),
    path('friend-request/reject/<int:request_id>/', RejectFriendRequest.as_view(), name='reject-friend-request'),
    path('friend-request/delete/<int:request_id>/', deleteFriendRequest.as_view(), name='delete-friend-request'),
    path('search/<str:search>/', UsersSearchList.as_view(), name='search-user'),
    path('friends/search/<str:search>/', SearchFriendView.as_view(), name='search-friends'),
    path('friends/',friendview.as_view(),name='friend'),
    path('friends/unfriend/<int:id>/',unfriendView.as_view(),name='friend'),
    path('notifications/', NotificationList.as_view(), name='notifications'),
    path('profile/view/<int:pk>/',profileViewUser.as_view()),
    path('friend-request/',friendRequestView.as_view(),name='friend-request'),
    path('people-you-may-know/', PeopleYouMayKnowView.as_view(), name='people_you_may_know'),

    # path('reset-password/<str:token>/', ResetPasswordView.as_view(), name='reset-password'),

]
