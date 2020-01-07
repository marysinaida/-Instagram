from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.caption

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_photo = models.ImageField(upload_to = 'posts/')
    bio = models.TextField(max_length=255)
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    def updateProfile(sender, **kwargs):
        if kwargs['created']:
            profile = Profile.objects.created(user=kwargs['instance'])
            post_save.connect(Profile, sender=User)



