from rest_framework import serializers
from .models import *

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
        model= postImage
        fields = '__all__'
class postSerializer(serializers.ModelSerializer):
    activity_details = activitySerializer(source="activity", read_only=True)
    sub_activity_details = subActivitySerializer(source="sub_activity", read_only=True)
    feeling_details = feelingSerilizer(source="feeling", read_only=True)
    images = postImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

        
