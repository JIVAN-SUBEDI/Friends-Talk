
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class fellingView(generics.ListAPIView):
    serializer_class = feelingSerilizer
    queryset = feeling.objects.all()
class activityView(generics.ListAPIView):
    serializer_class = activitySerializer
    queryset = activity.objects.all()

class addPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user
        data['user'] = user.id
        
        # Initialize the serializer with data
        serializer = postSerializer(data=data)
        
        if serializer.is_valid():
            # Save post and retrieve the instance
            post_instance = serializer.save()
            
            # Handle multiple images
            images = request.FILES.getlist('images')  # Use getlist to get multiple files
            for image in images:
                # Create and save post images associated with the post instance
                postImage.objects.create(post=post_instance, image=image)
            
            # Return serialized post data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return errors if serialization fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

