from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_active = models.BooleanField(default=False)  # User is inactive until they verify their email
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False,null=True,blank=True)
    expires_in = models.DateTimeField(null=True,blank=True)
    otp = models.IntegerField(null=True,blank=True)
    otp_expires = models.DateTimeField(null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name', 'last_name']

    def __str__(self):
        return self.email
class images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)


class works_place(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    works_from = models.CharField(max_length=255)
    works_to = models.CharField(max_length=255,null=True,blank=True)
    position = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    audience = models.IntegerField(default=0)
    current = models.BooleanField(default=False)
    desc = models.CharField(max_length=255,null=True,blank=True)
class college(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    attend_from = models.DateField(max_length=255)
    attend_to = models.DateField(max_length=255)
    address = models.CharField(max_length=255)
    audience = models.IntegerField(default=0)
    desc = models.CharField(max_length=255,null=True,blank=True)
class places_lived(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    type = models.IntegerField()    
    moved = models.CharField(max_length=255,null=True,blank=True)
    audience = models.IntegerField(default=0)
class profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]
    RELATIONSHIP_CHOICES = [
        ('single','Single'),
        ('married','Married'),
        ('in a relationship','In a relationship'),
        ('divorced','Divorced'),
        ('widowed','Widowed'),
        ('seprated','Seprated')
   
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,unique=True)
    date_of_birth = models.DateField()
    date_of_birth_audience = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    gender_audience = models.IntegerField(default=0)
    primary_phone_number = models.CharField(max_length=15, blank=True, null=True)
    primary_phone_number_audience = models.IntegerField(default=0)
    secondary_phone_number = models.CharField(max_length=15, blank=True, null=True)
    secondary_phone_number_audience = models.IntegerField(default=0)
    bio = models.TextField(max_length=255, blank=True)
    relationship = models.CharField(max_length=255,blank=True,null=True, choices=RELATIONSHIP_CHOICES)
    relationship_audience = models.IntegerField(default=0)
class Friend(models.Model):
    user1 = models.ForeignKey(CustomUser, related_name='friends1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(CustomUser, related_name='friends2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f'Friendship: {self.user1} & {self.user2}'

class FriendRequest(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')

    def __str__(self):
        return f'Friend request from {self.sender} to {self.receiver}'

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.recipient} - {self.message[:20]}'



    
    