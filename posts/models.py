from django.db import models
from users.models import CustomUser

class feeling(models.Model):
    name=models.CharField(max_length=255,unique=True)
    emoji=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name
class activity(models.Model):
    name=models.CharField(max_length=255,unique=True)
    emoji=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name
class sub_activity(models.Model):
    activity = models.ForeignKey(activity,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,unique=True)
    emoji=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    
    # Optional relation to Feeling and Activity
    feeling = models.ForeignKey(feeling, on_delete=models.SET_NULL, null=True, blank=True)
    activity = models.ForeignKey(activity, on_delete=models.SET_NULL, null=True, blank=True)
    sub_activity = models.ForeignKey(sub_activity, on_delete=models.SET_NULL, null=True, blank=True)

    # Text content
    content = models.TextField()

    # Optional image and video fields
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)


    # Likes and shares
    # share_post = models.ForeignKey(post)
    
    share_count = models.PositiveIntegerField(default=0)

    # Timestamp for the post
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post by {self.user.username} - {self.content[:30]}..."  # Short preview of content

 