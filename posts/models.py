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
    content = models.TextField(null=True,blank=True)
    share_count = models.PositiveIntegerField(default=0)
    shared_post = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='shares'
    )

    # Timestamp for the post
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.shared_post:
            return f"{self.user.username} shared a post"
        return f"{self.user.username}: {self.content[:30]}"

    def is_shared(self):
        return self.shared_post is not None
    
class postImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # Ensure a user can only like a post once
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


 
