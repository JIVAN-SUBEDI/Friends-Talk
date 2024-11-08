from rest_framework import serializers
from .models import *
from users.serializers import profileSerializer
from django.utils.timesince import timesince
from django.utils import timezone


class feelingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = feeling
        fields = '__all__'
class subActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = sub_activity
        fields = '__all__'       
class activitySerializer(serializers.ModelSerializer):
    subActivity = serializers.SerializerMethodField()
    class Meta:
        model = feeling
        fields = '__all__'
    def get_subActivity(self,obj):
        subActivity = sub_activity.objects.filter(activity=obj.id)
        return subActivitySerializer(subActivity,many=True).data
class postImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = postImage
        fields = '__all__'

class commentsSerializer(serializers.ModelSerializer):
    user_details=profileSerializer(source='user',read_only=True)
    class Meta:
        model = Comment
        fields=['id','post','user','user_details','content']
class sharePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id,content,images,user_details']
class postSerializer(serializers.ModelSerializer): 
    user_details = profileSerializer(source="user",read_only=True)
    activity_details = activitySerializer(source="activity", read_only=True)
    sub_activity_details = subActivitySerializer(source="sub_activity", read_only=True)
    feeling_details = feelingSerilizer(source="feeling", read_only=True)
    images = postImageSerializer(many=True, read_only=True)  # This should now pull in related images
    time_ago = serializers.SerializerMethodField(read_only=True)  # Custom field to display time since published
    liked = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    comments = commentsSerializer(many=True,read_only=True)
    shared_post_details = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
    def get_time_ago(self, obj):
        # Calculate the time since the post was created
        return timesince(obj.created_at, timezone.now()) + " ago"
    def get_liked(self,obj):
        user = self.context['request'].user
        liked = Like.objects.filter(post=obj.id,user=user).exists()
        return liked
    def get_likes_count(self,obj):
        like = Like.objects.filter(post=obj.id).count()
        return like
    def get_shared_post_details(self, obj):
        # Use recursion but limit depth by checking if it's a shared post of a shared post
        if obj.shared_post:
            return postSerializer(obj.shared_post, context=self.context).data
        return None