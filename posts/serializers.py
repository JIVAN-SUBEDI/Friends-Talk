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
        # return 'df'