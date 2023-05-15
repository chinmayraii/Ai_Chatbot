from django.db import models
from django.contrib.auth.models import User

class Bot(models.Model):
    user_chatbot = models.ForeignKey(User, on_delete=models.CASCADE)
    user_input = models.CharField(max_length=255)
    chatbot_response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_input
