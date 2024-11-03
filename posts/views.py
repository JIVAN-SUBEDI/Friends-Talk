
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
        data = request.data.copy()
        data['user'] = request.user.id

        # Initialize the serializer with post data
        serializer = postSerializer(data=data)

        if serializer.is_valid():
            # Save the post and retrieve the instance
            post_instance = serializer.save()

            # Handle multiple images upload
            images = request.FILES.getlist('images')
            for image in images:
                postImage.objects.create(post=post_instance, image=image)

            # Refetch the post instance to include images, activities, and feelings in response
            updated_post = Post.objects.get(id=post_instance.id)
            serialized_post = postSerializer(updated_post, context={'request': request})
            
            return Response(serialized_post.data, status=status.HTTP_201_CREATED)

        # Return errors if serialization fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)