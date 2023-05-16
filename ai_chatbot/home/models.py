from django.db import models
from django.contrib.auth.models import User

class Bot(models.Model):
    user_chatbot = models.ForeignKey(User, on_delete=models.CASCADE)
    user_input = models.CharField(max_length=255)
    chatbot_response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_input


class Profile(models.Model):
    user_details=models.ForeignKey(User,on_delete=models.CASCADE)
    user_mob=models.IntegerField(unique=True,blank=True)
    user_address=models.TextField()
    user_img=models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.user_details.username