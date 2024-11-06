
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


class PostView(APIView):
    permission_classes = [IsAuthenticated] 

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
            # Apply Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Set the page size here or globally in settings
        paginated_posts = paginator.paginate_queryset(posts, request)
            # Serialize paginated data
        serializer = postSerializer(paginated_posts, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    def post(self, request):
        # Create a mutable copy of request data to modify it
        data = request.data.copy()
        data['user'] = request.user.id

        # Extract the images list from request.FILES before initializing the serializer
        images = request.FILES.getlist('images')

        # Initialize the serializer with the modified data (don't pass request.FILES directly to it)
        serializer = postSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            # Save the post and retrieve the instance
            post_instance = serializer.save()

            # Handle multiple images upload
            for image in images:
                # Create postImage directly with each image file
                postImage.objects.create(post=post_instance, image=image)

            # Refetch the post instance to include images (avoiding file serialization issues)
            updated_post = Post.objects.get(id=post_instance.id)
            
            # Serialize the post without including the raw file objects
            serialized_post = postSerializer(updated_post, context={'request': request})

            return Response(serialized_post.data, status=status.HTTP_201_CREATED)

        # Return errors if serialization fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class likeUnlikePost(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        
        if not created:  # If the like already exists, it means the user wants to unlike
            like.delete()
            return Response({"message": "Post unliked",'liked':False}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"message": "Post liked",'liked':True}, status=status.HTTP_201_CREATED)
    
class CommentPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        # post = Post.objects.get(id=post_id)
        data = request.data.copy()
        data['user'] = request.user.id
        data['post'] = post_id
        serializer = commentsSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id, user=request.user)  # Ensure user can only delete their own comment
        comment.delete()
        return Response({"message": "Comment deleted"}, status=status.HTTP_204_NO_CONTENT)
