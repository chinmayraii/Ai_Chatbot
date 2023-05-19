from rest_framework import serializers
from . models import Bot
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('email', 'password','username')

    def validate(self, attr):
       validate_password(attr['password'])
       return attr

    def create(self, validated_data):

        user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                

                )
        user.set_password(validated_data['password'])
        user.save()
        return user



class BotSerializer(serializers.ModelSerializer):
    user_chatbot = RegisterSerializer
    
    class Meta:
        model = Bot 
        fields = ('id','user_input','chatbot_response','created_at')

        def create(self, validated_data):

            return Bot.objects.create(**validated_data)