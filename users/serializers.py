from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from django.core.exceptions import ValidationError
from datetime import datetime
from django.db.models import Q
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):

    gender = serializers.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    date_of_birth = serializers.DateField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'gender', 'date_of_birth']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_date_of_birth(self, value):
        """Validate the user's date of birth (optional: minimum age)"""
        today = datetime.today().date()
        if value >= today:
            raise ValidationError("Date of birth cannot be in the future.")
        
        # Optional: Check if the user is at least 13 years old
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 13:
            raise ValidationError("You must be at least 13 years old to register.")
        
        return value

    def validate_gender(self, value):
        """Validate the gender field"""
        if value not in ['male', 'female', 'others']:
            raise ValidationError("Gender must be one of 'male', 'female', or 'others'.")
        return value

    def create(self, validated_data):
        # Pop the gender and date_of_birth from validated_data
        gender = validated_data.pop('gender')
        date_of_birth = validated_data.pop('date_of_birth')

        # Create the user
        user = User.objects.create_user(**validated_data)

        # Create the profile with gender and date_of_birth
        profile.objects.create(user=user, gender=gender, date_of_birth=date_of_birth)

        return user
class loginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField()
class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','first_name', 'last_name', 'email','profile_image','cover_image']
class bioSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['bio']
class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model=images
        fields = ['image','id']
class photoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=images
        fields = ['image','user']
class workplace_serializer(serializers.ModelSerializer):
    class Meta:
        model = works_place
        fields = '__all__'
        read_only_fields = ['user']
class college_serializer(serializers.ModelSerializer):
    class Meta:
        model = college
        fields = '__all__'
        read_only_fields = ['user']



class places_serializer(serializers.ModelSerializer):
    class Meta:
        model = places_lived
        fields = '__all__'
        read_only_fields = ['user']
    def validate_type(self, value):
        if value not in [0, 1, 2]:
            raise serializers.ValidationError("Type must be 0, 1, or 2.")
        return value

    def validate(self, data):
        user = data.get('user')
        type = data.get('type')
        
        if type in [0, 1]:
            existing = places_lived.objects.filter(user=user, type=type).exclude(pk=self.instance.pk if self.instance else None)
            if existing.exists():
                raise serializers.ValidationError(f'User can only have one entry with type {type}.')
        
        return data
class profileContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= profile
        fields = '__all__'
        read_only_fields = ['user']
class genderSerializer(serializers.ModelSerializer):
    class Meta:
        model =profile
        fields = ['gender','gender_audience']
class bioSerializer(serializers.ModelSerializer):
    class Meta:
        model =profile
        fields = ['bio']
class dobSerializer(serializers.ModelSerializer):
    class Meta:
        model =profile
        fields = ['date_of_birth','date_of_birth_audience']
class relationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model =profile
        fields = ['relationship','relationship_audience']
class primarySerializer(serializers.ModelSerializer):
    class Meta:
        model =profile
        fields = ['primary_phone_number','primary_phone_number_audience']
class secondarySerializer(serializers.ModelSerializer):
    class Meta:
        model =profile
        fields = ['secondary_phone_number','secondary_phone_number_audience']

class FriendSerializer(serializers.ModelSerializer):

    details = serializers.SerializerMethodField()
    mutual_friends_count = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    class Meta:
        model=Friend
        fields=['id','details','mutual_friends_count','status']
    def get_mutual_friends_count(self, obj):
        request_user = self.context['request'].user

        # Get IDs of friends of the current user (user1 and user2)
        request_user_friends_user1 = set(Friend.objects.filter(user1=request_user).values_list('user2_id', flat=True))
        request_user_friends_user2 = set(Friend.objects.filter(user2=request_user).values_list('user1_id', flat=True))
        request_user_friends = request_user_friends_user1.union(request_user_friends_user2)
        
        # Get IDs of friends of the friend user (user1 and user2)
        friend_user = obj.user1 if obj.user1 != request_user else obj.user2
        friend_user_friends_user1 = set(Friend.objects.filter(user1=friend_user).values_list('user2_id', flat=True))
        friend_user_friends_user2 = set(Friend.objects.filter(user2=friend_user).values_list('user1_id', flat=True))
        friend_user_friends = friend_user_friends_user1.union(friend_user_friends_user2)

        # Calculate mutual friends
        mutual_friends = request_user_friends.intersection(friend_user_friends)
        return len(mutual_friends)  # Return the count of mutual friends
    def get_details(self, obj):
        request_user = self.context['request'].user
        # Determine which user is the friend based on the relationship
        friend_user = obj.user1 if obj.user2 == request_user else obj.user2
        
        # Serialize the friend's profile
        serializer = profileSerializer(friend_user,context={'request': self.context['request']})
        
        return serializer.data
    def get_status(self, obj):
        request_user = self.context['request'].user
        friend_user = obj.user1 if obj.user2 == obj else obj.user1
        # Check if the request_user and obj are friends
        if Friend.objects.filter(user1=request_user, user2=friend_user).exists() or Friend.objects.filter(user1=friend_user, user2=request_user).exists():
            return 'Friend'
        # Check if a friend request was sent by the request_user to obj
        elif FriendRequest.objects.filter(sender=request_user, receiver=friend_user).exists():
            return 'Request Sent'
        # Check if a friend request was received from obj by the request_user
        elif FriendRequest.objects.filter(sender=friend_user, receiver=request_user).exists():
            return 'Request Received'
        else:
            return 'Not Friends'
        
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'created_at', 'is_read']
class SearchSerializer(serializers.ModelSerializer):
    mutual_friend_count = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'mutual_friend_count', 'status','profile_image']

    def get_mutual_friend_count(self, obj):
        request_user = self.context['request'].user

        
        # Get IDs of friends of the current user (user1 and user2)
        request_user_friends_user1 = set(Friend.objects.filter(user1=request_user).values_list('user2_id', flat=True))
        request_user_friends_user2 = set(Friend.objects.filter(user2=request_user).values_list('user1_id', flat=True))
        request_user_friends = request_user_friends_user1.union(request_user_friends_user2)
        
        # Get IDs of friends of the searched user (user1 and user2)
        searched_user_friends_user1 = set(Friend.objects.filter(user1=obj).values_list('user2_id', flat=True))
        searched_user_friends_user2 = set(Friend.objects.filter(user2=obj).values_list('user1_id', flat=True))
        searched_user_friends = searched_user_friends_user1.union(searched_user_friends_user2)
        
        # Calculate mutual friends
        mutual_friends = request_user_friends.intersection(searched_user_friends)
        return len(mutual_friends)  # Return the count of mutual friends

    def get_status(self, obj):
        request_user = self.context['request'].user
        # Check if the request_user and obj are friends
        if Friend.objects.filter(user1=request_user, user2=obj).exists() or Friend.objects.filter(user1=obj, user2=request_user).exists():
            return 'Friend'
        # Check if a friend request was sent by the request_user to obj
        elif FriendRequest.objects.filter(sender=request_user, receiver=obj).exists():
            return 'Request Sent'
        # Check if a friend request was received from obj by the request_user
        elif FriendRequest.objects.filter(sender=obj, receiver=request_user).exists():
            return 'Request Received'
        else:
            return 'Not Friends'
class profileViewSerializer(serializers.ModelSerializer):
    lived = serializers.SerializerMethodField()
    basicInfo = serializers.SerializerMethodField()
    work = serializers.SerializerMethodField()
    collage = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    friends = serializers.SerializerMethodField()
    latestCollage = serializers.SerializerMethodField()
    latestWorkplace = serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=['id','first_name','last_name','cover_image','profile_image','lived','basicInfo','collage','work','status','friends','latestCollage','latestWorkplace']
    def get_lived(self, obj):
        request_user = self.context['request'].user

        # Check if the users are friends
        check_friend = Friend.objects.filter(user1=request_user, user2=obj).exists() or \
                       Friend.objects.filter(user1=obj, user2=request_user).exists()

        # If they are friends, return both public and friend (audience=0 and audience=1)
        if check_friend:
            cities = places_lived.objects.filter(user=obj, audience__in=[0, 1])
        else:
            # If not friends, return only public (audience=0)
            cities = places_lived.objects.filter(user=obj, audience=0)

        # Ensure the queryset is distinct
        cities = cities.distinct()

        # Serialize the data and return
        serializer = places_serializer(cities, many=True)
        return serializer.data
    def get_basicInfo(self, obj):
        request_user = self.context['request'].user

        # Check if the users are friends
        check_friend = Friend.objects.filter(user1=request_user, user2=obj).exists() or \
                       Friend.objects.filter(user1=obj, user2=request_user).exists()

        try:
            # Fetch the profile of the viewed user (obj)
            basic_info = profile.objects.get(user=obj)

            # Prepare the response dictionary
            basic_info_data = {}

            # Add data based on the audience and friendship status
             # Date of Birth
            if basic_info.date_of_birth_audience == 0 or (check_friend and basic_info.date_of_birth_audience == 1):
                basic_info_data['date_of_birth'] = basic_info.date_of_birth
            else:
                basic_info_data['date_of_birth'] = ''

            # Gender
            if basic_info.gender_audience == 0 or (check_friend and basic_info.gender_audience == 1):
                basic_info_data['gender'] = basic_info.gender
            else:
                basic_info_data['gender'] = ''

            # Primary Phone Number
            if basic_info.primary_phone_number_audience == 0 or (check_friend and basic_info.primary_phone_number_audience == 1):
                basic_info_data['primary_phone_number'] = basic_info.primary_phone_number
            else:
                basic_info_data['primary_phone_number'] = ''

            # Secondary Phone Number
            if basic_info.secondary_phone_number_audience == 0 or (check_friend and basic_info.secondary_phone_number_audience == 1):
                basic_info_data['secondary_phone_number'] = basic_info.secondary_phone_number
            else:
                basic_info_data['secondary_phone_number'] = ''

            # Relationship Status
            if basic_info.relationship_audience == 0 or (check_friend and basic_info.relationship_audience == 1):
                basic_info_data['relationship'] = basic_info.relationship
            else:
                basic_info_data['relationship'] = ''

            # Bio: Assuming bio is public for all (you can add an audience field for it if needed)
            basic_info_data['bio'] = basic_info.bio

            return basic_info_data

        except profile.DoesNotExist:
            # Handle the case where no profile exists for the user
            return {}
    def get_work(self,obj):
        request_user = self.context['request'].user

        # Check if the users are friends
        check_friend = Friend.objects.filter(user1=request_user, user2=obj).exists() or \
                       Friend.objects.filter(user1=obj, user2=request_user).exists()

        # If they are friends, return both public and friend (audience=0 and audience=1)
        if check_friend:
            workPlace = works_place.objects.filter(user=obj, audience__in=[0, 1])
        else:
            # If not friends, return only public (audience=0)
            workPlace = works_place.objects.filter(user=obj, audience=0)

        # Ensure the queryset is distinct
        workPlace = workPlace.distinct()

        # Serialize the data and return
        serializer = workplace_serializer(workPlace, many=True)
        return serializer.data
    def get_latestCollage(self,obj):
        request_user = self.context['request'].user

        # Check if the users are friends
        check_friend = Friend.objects.filter(user1=request_user, user2=obj).exists() or \
                       Friend.objects.filter(user1=obj, user2=request_user).exists()

        # If they are friends, return both public and friend (audience=0 and audience=1)
        if check_friend:
            collage = college.objects.filter(user=obj, audience__in=[0, 1])
        else:
            # If not friends, return only public (audience=0)
            collage = college.objects.filter(user=obj, audience=0)

        # Ensure the queryset is distinct
        collage = collage.distinct()

        # Serialize the data and return
        # Find the current college or the most recent past college
        current_college = collage.filter(attend_to__isnull=True).first()
    
        if not current_college:
            # Check if there are any future dates
            current_college = collage.filter(attend_to__gt=datetime.today()).first()
        
        if current_college:
            return {
                'message': f'Currently studying at {current_college.name}',
                'data': college_serializer(current_college).data
            }
        else:
            # Find the most recent past college (where attend_to is not null and in the past)
            latest_past_college = collage.filter(attend_to__lte=datetime.today()).order_by('-attend_to').first()
            if latest_past_college:
                return {
                    'message': f'Studied at {latest_past_college.name}',
                    'data': college_serializer(latest_past_college).data
                }

        # Return null if no college information is found
        return {'message': None, 'data': None}
    def get_collage(self,obj):
        request_user = self.context['request'].user

        # Check if the users are friends
        check_friend = Friend.objects.filter(user1=request_user, user2=obj).exists() or \
                       Friend.objects.filter(user1=obj, user2=request_user).exists()

        # If they are friends, return both public and friend (audience=0 and audience=1)
        if check_friend:
            collage = college.objects.filter(user=obj, audience__in=[0, 1])
        else:
            # If not friends, return only public (audience=0)
            collage = college.objects.filter(user=obj, audience=0)

        # Ensure the queryset is distinct
        collage = collage.distinct()

        # Serialize the data and return
        serializer= college_serializer(collage,many=True)
        return serializer.data

    def get_status(self,obj):
        request_user = self.context['request'].user
   
        # Check if the request_user and obj are friends
        if Friend.objects.filter(user1=request_user, user2=obj).exists() or Friend.objects.filter(user1=obj, user2=request_user).exists():
            return 'Friend'
        # Check if a friend request was sent by the request_user to obj
        elif FriendRequest.objects.filter(sender=request_user, receiver=obj).exists():
            return 'Request Sent'
        # Check if a friend request was received from obj by the request_user
        elif FriendRequest.objects.filter(sender=obj, receiver=request_user).exists():
            return 'Request Received'
        else:
            return 'Not Friends'
    def get_friends(self,obj):
          request_user = self.context['request'].user
          friends = Friend.objects.filter(Q(user1=obj) | Q(user2=obj)).exclude(Q(user1=request_user) | Q(user2=request_user))
          serializer = FriendSerializer(friends,many=True, context=self.context)
          return serializer.data
    def get_latestWorkplace(self, obj):
        request_user = self.context['request'].user

        # Check if the users are friends
        check_friend = Friend.objects.filter(user1=request_user, user2=obj).exists() or \
                       Friend.objects.filter(user1=obj, user2=request_user).exists()

        # Filter workplaces based on friendship and audience settings
        if check_friend:
            workplaces = works_place.objects.filter(user=obj, audience__in=[0, 1])
        else:
            workplaces = works_place.objects.filter(user=obj, audience=0)

        # Ensure the queryset is distinct
        workplaces = workplaces.distinct()

        # Find the current workplace (where current is True or works_to is null)
        current_workplace = workplaces.filter(Q(current=True) | Q(works_to__isnull=True)).first()

        if current_workplace:
            # Return the current workplace
            return workplace_serializer(current_workplace).data
        else:
            # Get the most recent past workplace (where works_to is not null and sort by works_from)
            latest_past_workplace = workplaces.filter(works_to__isnull=False).order_by('-works_from').first()

            # Return the latest past workplace or null
            return workplace_serializer(latest_past_workplace).data if latest_past_workplace else None
class FriendRequestSerializer(serializers.ModelSerializer):
    sender = profileSerializer()
    mutual_friend_count = serializers.SerializerMethodField()
    class Meta:
        model = FriendRequest
        fields = ['id', 'sender', 'created_at','mutual_friend_count']
    def get_mutual_friend_count(self, obj):
        # Get the user who received the friend request (assumed to be in the context)
        request_user = self.context['request'].user

        # Get the sender of the friend request
        sender_user = obj.sender

        # Get the IDs of friends of the request user (user1 and user2)
        request_user_friends_user1 = set(Friend.objects.filter(user1=request_user).values_list('user2_id', flat=True))
        request_user_friends_user2 = set(Friend.objects.filter(user2=request_user).values_list('user1_id', flat=True))
        request_user_friends = request_user_friends_user1.union(request_user_friends_user2)

        # Get the IDs of friends of the sender user (user1 and user2)
        sender_user_friends_user1 = set(Friend.objects.filter(user1=sender_user).values_list('user2_id', flat=True))
        sender_user_friends_user2 = set(Friend.objects.filter(user2=sender_user).values_list('user1_id', flat=True))
        sender_user_friends = sender_user_friends_user1.union(sender_user_friends_user2)

        # Calculate mutual friends
        mutual_friends = request_user_friends.intersection(sender_user_friends)

        return len(mutual_friends)  # Return the count of mutual friends