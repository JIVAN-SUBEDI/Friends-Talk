
from rest_framework import generics
from .models import *
from .serializers import *

class fellingView(generics.ListAPIView):
    serializer_class = feelingSerilizer
    queryset = feeling.objects.all()
class activityView(generics.ListAPIView):
    serializer_class = activitySerializer
    queryset = activity.objects.all()
