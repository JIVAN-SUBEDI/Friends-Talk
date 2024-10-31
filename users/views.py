from rest_framework import status, generics
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth import get_user_model,authenticate
from django.core.mail import send_mail
from django.conf import settings
from .serializers import *
import uuid
from .models import *
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
import random
import pytz
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from django.utils.encoding import force_str


User = get_user_model()
timezone = pytz.timezone('UTC') 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token is None:
            return Response({'detail': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Use the refresh token to create a new access token
            refresh = RefreshToken(refresh_token)
            new_access_token = refresh.access_token

            return Response({
                'access': str(new_access_token),
            }, status=status.HTTP_200_OK)
        
        except TokenError:
            return Response({'detail': 'Invalid or expired refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
class UserRegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()

            # Email verification process
            verification_link = f'http://localhost:8000/users/verify-email/{user.email}/{user.verification_token}'
            subject = "Verify Your Email Address"
            html_message = render_to_string('email/verification.html', {'user': user, 'verification_link': verification_link})
            plain_message = strip_tags(html_message)  # Plain text fallback
            from_email = 'subedijiwan5@gmail.com'
            to = user.email
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)

            # Set token expiry time (5 minutes)
            user.expires_in = datetime.now(timezone) + timedelta(minutes=5)
            user.save()

            return Response(
                {'message': 'Please check your inbox and follow the instructions provided to verify your email address. '
                            'If you do not receive the email within a few minutes, please check your spam or junk folder.'}, 
                status=status.HTTP_201_CREATED
            )

        return Response({'field_errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

def verifyEmailRegistration(request,email,token):
    try:
        user = User.objects.get(email=email,verification_token = token)
        if user.expires_in >= datetime.now(timezone):
            user.verification_token = None
            user.is_active = True
            user.save()
            return render(request,"email_verified.html")
        return render(request,"invalid.html")
    except User.DoesNotExist:
        return render(request,"invalid.html")
class forgotPasswordView(APIView):

    def get(self,request,email):
        try:
            user = User.objects.get(email = email)
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            user.otp = otp
            user.otp_expires = datetime.now(timezone) + timedelta(minutes=5)
            user.save()
            subject = "OTP"
            html_message = render_to_string('email/otp.html',{'user':user,'otp': otp})     
            plain_message = strip_tags(html_message)  # Plain text fallback
            from_email = 'subedijiwan5@gmail.com'
            to = user.email
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            return Response({'message':'Please check your inbox for OTP. If you do not receive the email within a few minutes, please check your spam or junk folder.'} ,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message':"We could not find an account associated with this email address. Please ensure that you have entered the correct email address. If you continue to experience issues, please contact our support team."} ,status=status.HTTP_404_NOT_FOUND)  
class verifyForgotOtpView(APIView):
    def get(self,request,email,otp):
        try:
            user = User.objects.get(email=email)
            if user.otp == otp and user.otp_expires >= datetime.now(timezone):
                password = User.objects.make_random_password()
                user.otp = None
                user.set_password(password)
                user.otp_expires = None
                user.save()
                subject = "Reset Password"
                html_message = render_to_string('email/password.html',{'user':user,'new_password': password})     
                plain_message = strip_tags(html_message)  # Plain text fallback
                from_email = 'subedijiwan5@gmail.com'
                to = user.email
                send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                return Response({'message':'Please check your inbox for new password. If you do not receive the email within a few minutes, please check your spam or junk folder.'},status=status.HTTP_200_OK)
            return Response({'message':'Your OTP is either invalid or has expired. Please request a new OTP by clicking the Resend OTP button below.'},status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message':"We could not find an account associated with this email address. Please ensure that you have entered the correct email address. If you continue to experience issues, please contact our support team."} ,status=status.HTTP_404_NOT_FOUND)  
class resendVerificationlink(APIView):
    def get(self,request,email):
        try:
            user = User.objects.get(email=email)
            token = uuid.uuid4()
            verification_link = f'http://localhost:8000/users/verify-email/{user.email}/{token}'
            subject = "Verify Your Email Address"
            html_message = render_to_string('email/verification.html',{'user':user,'verification_link': verification_link})     
            plain_message = strip_tags(html_message)  # Plain text fallback
            from_email = 'subedijiwan5@gmail.com'
            to = user.email
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            user.verification_token = token
            user.expires_in = datetime.now(timezone) + timedelta(minutes=5)
            user.save()       
            return Response({'message':'Please check your inbox and follow the instructions provided to verify your email address. If you do not receive the email within a few minutes, please check your spam or junk folder.'} ,status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'message':"We could not find an account associated with this email address. Please ensure that you have entered the correct email address. If you continue to experience issues, please contact our support team."} ,status=status.HTTP_404_NOT_FOUND)       
class loginView(APIView):
    def post(self,request):
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'non_field_errors': "Email or password is not valid!"}, status=status.HTTP_404_NOT_FOUND)

            if not user.is_active:
                
                return Response({'non_field_errors': 'Your email is not verified. Please verify your email before login.','email':email}, status=status.HTTP_403_FORBIDDEN)
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'message':'Login success ','token':token},status=status.HTTP_200_OK)
            return Response({'non_field_errors':"Email or password is not valid!"},status=status.HTTP_404_NOT_FOUND)
        return Response({"field_errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
class profileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        email = request.user.email
        user = User.objects.get(email=email)
        serializer = profileSerializer(user,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
class updateBio(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        user = request.user
        data = request.data
        serializer = bioSerializer(data=data)
        if serializer.is_valid():
            profiles = profile.objects.get(user=user)
            profiles.bio = serializer.validated_data['bio']
            profiles.save()
            return Response({"message":"Bio updated successfully."},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class changeCoverImage(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        user = request.user
        cover_image = request.FILES.get('cover_image')

        if cover_image:
            # Save the cover image to the User model (assuming User has a cover_image field)
            user.cover_image.save(cover_image.name, cover_image)
            user.save()

            # Create an entry in the Photo model referencing the already uploaded image
            images.objects.create(
                user=user,
                image=user.cover_image  # No need to re-upload, just reference the existing cover image
            )

            return Response({"message": "Cover photo updated and linked to Photo model successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
class getImageView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = photoSerializer
    def get_queryset(self):
        return  images.objects.filter(user=self.request.user) 
class changeCoverImageFromPhoto(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        user = request.user
        try:
            photo = images.objects.get(pk=id)
            user.cover_image = photo.image
            user.save()
            return Response({"message": "Cover photo updated successfully."}, status=status.HTTP_200_OK)
        except images.DoesNotExist:
            return Response({"error": "Photo you selected doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
class changeProfileImageFromPhoto(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        user = request.user
        try:
            photo = images.objects.get(pk=id)
            user.profile_image = photo.image
            user.save()
            return Response({"message": "Profile photo updated successfully."}, status=status.HTTP_200_OK)
        except images.DoesNotExist:
            return Response({"error": "Photo you selected doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
class uploadPhoto(generics.CreateAPIView):
    queryset = images.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class = photoSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class addWorkPlace(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = workplace_serializer
    def get_queryset(self):
        user = self.request.user
        return works_place.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class editDeleteListworkplace(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = workplace_serializer
    def get_queryset(self):
        user = self.request.user
        return works_place.objects.filter(user=user)
    def perform_update(self, serializer):
        instance = self.get_object()
        # Check if the instance belongs to the authenticated user
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this workplace.")
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        # Check if the instance belongs to the authenticated user
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this workplace.")
        instance.delete()  # Delete the instance if the check passes
class addCollege(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = college_serializer
    def get_queryset(self):
        user = self.request.user
        return college.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class editDeleteListCollege(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = college_serializer
    def get_queryset(self):
        user = self.request.user
        return college.objects.filter(user=user)
    def perform_update(self, serializer):
        instance = self.get_object()
        # Check if the instance belongs to the authenticated user
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this workplace.")
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        # Check if the instance belongs to the authenticated user
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this workplace.")
        instance.delete()  # Delete the instance if the check passes
class addPlaces(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = places_serializer
    def get_queryset(self):
        user = self.request.user
        return places_lived.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class editDeleteListPlaces(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = places_serializer
    def get_queryset(self):
        user = self.request.user
        return places_lived.objects.filter(user=user)
    def perform_update(self, serializer):
        instance = self.get_object()
        # Check if the instance belongs to the authenticated user
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this workplace.")
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        # Check if the instance belongs to the authenticated user
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this workplace.")
        instance.delete()  # Delete the instance if the check passes

class profileContactView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=profileContactSerializer
    def get_queryset(self):
        return profile.objects.filter(user=self.request.user)
class updateGenderView(APIView):
    def post(self,request):
        user = request.user
        data = request.data
        serializer = genderSerializer(data=data)
        if serializer.is_valid():
            profiles = profile.objects.get(user=user)
            profiles.gender = serializer.validated_data['gender']
            profiles.gender_audience = serializer.validated_data['gender_audience']
            profiles.save()
            return Response({'message': 'Gender updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class updateDobView(APIView):
    def post(self,request):
        user = request.user
        data = request.data
        serializer = dobSerializer(data=data)
        if serializer.is_valid():
            profiles = profile.objects.get(user=user)
            profiles.date_of_birth = serializer.validated_data['date_of_birth']
            profiles.date_of_birth_audience = serializer.validated_data['date_of_birth_audience']
            profiles.save()
            return Response({'message': 'Dob updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class updateRelationshipView(APIView):
    def post(self,request):
        user = request.user
        data = request.data
        serializer = relationshipSerializer(data=data)
        if serializer.is_valid():
            profiles = profile.objects.get(user=user)
            profiles.relationship = serializer.validated_data['relationship']
            profiles.relationship_audience = serializer.validated_data['relationship_audience']
            profiles.save()
            return Response({'message': 'Relationship updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class updatePrimaryView(APIView):
    def post(self,request):
        user = request.user
        data = request.data
        serializer = primarySerializer(data=data)
        if serializer.is_valid():
            profiles = profile.objects.get(user=user)
            profiles.primary_phone_number = serializer.validated_data['primary_phone_number']
            profiles.primary_phone_number_audience = serializer.validated_data['primary_phone_number_audience']
            profiles.save()
            return Response({'message': 'Primary phone number updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class updateSecondaryView(APIView):
    def post(self,request):
        user = request.user
        data = request.data
        serializer = secondarySerializer(data=data)
        if serializer.is_valid():
            profiles = profile.objects.get(user=user)
            profiles.secondary_phone_number = serializer.validated_data['secondary_phone_number']
            profiles.secondary_phone_number_audience = serializer.validated_data['secondary_phone_number_audience']
            profiles.save()
            return Response({'message': 'Secondary phone number updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class SendFriendRequest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, receiver_id):
        receiver = User.objects.get(id=receiver_id)
        sender = request.user

        # Check if a request already exists
        if FriendRequest.objects.filter(sender=sender, receiver=receiver).exists():
            return Response({"error": "Friend request already sent"}, status=status.HTTP_400_BAD_REQUEST)

        friend_request = FriendRequest.objects.create(sender=sender, receiver=receiver)

        # Create notification for the receiver
        Notification.objects.create(
            recipient=receiver,
            message=f"You have a new friend request from {sender.first_name} {sender.last_name}"
        )

        return Response({"message": "Friend request sent"}, status=status.HTTP_201_CREATED)

class NotificationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
class AcceptFriendRequest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, request_id):
        try:
            friend_request = FriendRequest.objects.get(sender=request_id, receiver=request.user)
        except FriendRequest.DoesNotExist:
            return Response({"error": "Friend request not found or already handled"}, status=status.HTTP_404_NOT_FOUND)

        # Accept the friend request
        friend_request.delete()

        # Create a friendship relationship
        Friend.objects.create(user1=friend_request.sender, user2=friend_request.receiver)

        # Notify the sender that the request was accepted
        Notification.objects.create(
            recipient=friend_request.sender,
            message=f"{request.user.first_name} {request.user.last_name} accepted your friend request"
        )

        return Response({"message": "Friend request accepted"}, status=status.HTTP_200_OK)

class RejectFriendRequest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, request_id):
        try:
            friend_request = FriendRequest.objects.get(sender=request_id, receiver=request.user)
        except FriendRequest.DoesNotExist:
            return Response({"error": "Friend request not found or already handled"}, status=status.HTTP_404_NOT_FOUND)


        friend_request.delete()

        # Notify the sender that the request was rejected
        Notification.objects.create(
            recipient=friend_request.sender,
            message=f"{request.user.first_name} {request.user.last_name} rejected your friend request"
        )

        return Response({"message": "Friend request rejected"}, status=status.HTTP_200_OK)
class deleteFriendRequest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, request_id):
        try:
            friend_request = FriendRequest.objects.get(receiver=request_id, sender=request.user)
        except FriendRequest.DoesNotExist:
            return Response({"error": "Friend request not found or already handled"}, status=status.HTTP_404_NOT_FOUND)


        friend_request.delete()

      
        return Response({"message": "Friend request deleted"}, status=status.HTTP_200_OK) 
class UsersSearchList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, search):
        search_query = search.strip()
        request_user = request.user

        # Extract query params from the request
        city = request.query_params.get('city', None)
        college_name = request.query_params.get('education', None)
        work_name = request.query_params.get('work', None)

        if search_query:
            search_parts = search_query.split()

            if len(search_parts) == 2:
                first_name_query = search_parts[0]
                last_name_query = search_parts[1]
                users = User.objects.filter(
                    Q(first_name__icontains=first_name_query) & Q(last_name__icontains=last_name_query)
                ).exclude(id=request_user.id)  # Exclude current user
            else:
                users = User.objects.filter(
                    Q(email__icontains=search_query) |
                    Q(first_name__icontains=search_query) |
                    Q(last_name__icontains=search_query)
                ).exclude(id=request_user.id)  # Exclude current user

             # Filter by city if provided
            if city:
   
                users = users.filter(
                    Q(places_lived__city__icontains=city)
                )

            # # Filter by college if provided
            if college_name:
                users = users.filter(
                    Q(college__name__icontains=college_name)
                )

            # Filter by workplace if provided
            if work_name:
                users = users.filter(
                    Q(works_place__name__icontains=work_name)
                )
            
            users = users.distinct()
            # Apply Pagination
            paginator = PageNumberPagination()
            paginator.page_size = 5  # Set the page size here or globally in settings
            paginated_users = paginator.paginate_queryset(users, request)

            # Serialize paginated data
            serializer = SearchSerializer(paginated_users, many=True, context={'request': request})

            # Sort based on status and mutual friends
            sorted_data = sorted(
                serializer.data,
                key=lambda user: (
                    user['status'] == 'Friend',  # Friends come first
                    user['status'] == 'Request Sent' or user['status'] == 'Request Received',
                    user['mutual_friend_count'] > 0 
                ),
                reverse=True
            )

            # Return paginated and sorted data
            return paginator.get_paginated_response(sorted_data)
        else:
            return Response([], status=status.HTTP_200_OK)

class SearchFriendView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, search):
        search_query = force_str(search.strip())  # Ensure search query is a properly decoded string
        print(search_query)
        request_user = request.user

        if search_query:
        #     # Get the friend IDs of the authenticated user in a single query
            friends = Friend.objects.filter(
                Q(user1=request_user) | Q(user2=request_user)
            )
            friend_ids = {friend.user2.id if friend.user1.id == request_user.id else friend.user1.id for friend in friends}

        #     # Prepare search queries
            search_parts = search_query.split()
            if len(search_parts) == 2:
              
        #         # Filter only friends based on search query
                users = User.objects.filter(
                    Q(first_name__icontains=search_parts[0]) &
                    Q(last_name__icontains=search_parts[1]) &
                    Q(id__in=friend_ids)
                )
            else:
                # Filter only friends based on search query
                users = User.objects.filter(
                    (Q(email__icontains=search_query) |
                     Q(first_name__icontains=search_query) |
                     Q(last_name__icontains=search_query)) &
                    Q(id__in=friend_ids)
                )

            # Prepare the response data
            
            

            return Response(profileSerializer(users,many=True,context={'request':request}).data, status=status.HTTP_200_OK)

        # # If no search query, return an empty response
        return Response( [], status=status.HTTP_200_OK)
    
class profileViewUser(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = profileViewSerializer

class friendview(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendSerializer
    def get_queryset(self):
        request = self.request
        return Friend.objects.filter(Q(user1=request.user) | Q(user2=request.user))
    
class unfriendView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Friend.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        # Ensure only the user's friend relationships are available for deletion
        request_user = self.request.user
        return Friend.objects.filter(Q(user1=request_user) | Q(user2=request_user))

    def perform_destroy(self, instance):
        # Optionally perform any logic before deletion
        instance.delete()
        return Response({"message": "Friendship successfully removed."}, status=status.HTTP_204_NO_CONTENT)
class friendRequestView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendRequestSerializer
    def get_queryset(self):
        request_user = self.request.user
        return FriendRequest.objects.filter(receiver= request_user)
class PeopleYouMayKnowView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SearchSerializer

    def get_queryset(self):
        request_user = self.request.user

        # Get IDs of the user's friends
        friends_of_user = Friend.objects.filter(
            Q(user1=request_user) | Q(user2=request_user)
        ).values_list('user1_id', 'user2_id')

        # Flatten the list of friend IDs
        friends_ids = set()
        for friend1, friend2 in friends_of_user:
            if friend1 != request_user.id:
                friends_ids.add(friend1)
            if friend2 != request_user.id:
                friends_ids.add(friend2)

        # Start with mutual friends suggestions
        user_ids = set(Friend.objects.filter(
            Q(user1__in=friends_ids) | Q(user2__in=friends_ids)
        ).exclude(
            Q(user1=request_user) | Q(user2=request_user) | Q(user1__in=friends_ids) | Q(user2__in=friends_ids)
        ).values_list('user1_id', 'user2_id'))

        # Get the current user's places, colleges, and workplaces
        current_user_places = places_lived.objects.filter(user=request_user).values_list('city', flat=True)
        current_user_colleges = college.objects.filter(user=request_user).values_list('name', flat=True)
        current_user_workplaces = works_place.objects.filter(user=request_user).values_list('name', flat=True)

        # Suggest users based on places lived
        for city in current_user_places:
            similar_users = places_lived.objects.filter(city__icontains=city).exclude(user=request_user).values_list('user_id', flat=True)
            user_ids.update(similar_users)

        # Suggest users based on college
        for collage in current_user_colleges:
            similar_users = college.objects.filter(name__icontains=collage).exclude(user=request_user).values_list('user_id', flat=True)
            user_ids.update(similar_users)

        # Suggest users based on workplace
        for workplace in current_user_workplaces:
            similar_users = works_place.objects.filter(name__icontains=workplace).exclude(user=request_user).values_list('user_id', flat=True)
            user_ids.update(similar_users)

        # Exclude users who have already received a friend request from the current user
        sent_friend_requests = FriendRequest.objects.filter(receiver=request_user).values_list('sender_id', flat=True)
        print(sent_friend_requests)

        # Return User queryset and exclude friends and those who have received a friend request
        return User.objects.filter(id__in=user_ids).exclude(id__in=friends_ids).exclude(id__in=sent_friend_requests).distinct()
