
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


from .models import *
from .serializers import *
from users.models import Friend
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class fellingView(generics.ListAPIView):
    serializer_class = feelingSerilizer
    queryset = feeling.objects.all()
class activityView(generics.ListAPIView):
    serializer_class = activitySerializer
    queryset = activity.objects.all()

class FriendPostsPagination(PageNumberPagination):
    page_size = 10  # Number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100  # Maximum number of posts that can be requested

class PostView(APIView):
    permission_classes = [IsAuthenticated] 
    pagination_class = FriendPostsPagination
    def get(self,request):
        user = request.user
               # Use Q objects to filter friends, excluding the current user
        friends = Friend.objects.filter(Q(user1=user) | Q(user2=user))

        # Extract friend IDs, avoiding the current user's ID
        friend_ids = []
        for friend in friends:
            if friend.user1 != user:  # Only add user2 if not current user
                friend_ids.append(friend.user1.id)
            if friend.user2 != user:  # Only add user1 if not current user
                friend_ids.append(friend.user2.id)

        # Remove duplicates if necessary
        friend_ids = list(set(friend_ids))

        posts = Post.objects.filter(user__in=friend_ids).order_by('-created_at')
        paginator = self.pagination_class()
        paginated_posts = paginator.paginate_queryset(posts, request)

        return Response(postSerializer(paginated_posts, many=True, context={'request': request}).data, status=status.HTTP_200_OK)
    def post(self, request):
        
        data = request.data
        data['user'] = request.user.id

        # Initialize the serializer with post data
        serializer = postSerializer(data=data)

        if serializer.is_valid():
            # Save the post and retrieve the instance
            post_instance = serializer.save()

            # Handle multiple images upload
            images = request.FILES.getlist('images')
       

            for image in images:
                postImage.objects.create(post=post_instance, image=image)  # Create postImage directly with image

            # Refetch the post instance to include images
            updated_post = Post.objects.get(id=post_instance.id)
            serialized_post = postSerializer(updated_post, context={'request': request})

            return Response(serialized_post.data, status=status.HTTP_201_CREATED)

        # Return errors if serialization fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
