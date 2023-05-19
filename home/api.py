from .models import Bot
import openai
import os
from home.serializer import BotSerializer,RegisterSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_chat_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'User: {message}\nChatbot:',
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()




class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            data = User.objects.all()
            serializer =RegisterSerializer(data,many = True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response( serializer.data,status=status.HTTP_400_BAD_REQUEST)  

class BotApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        messages = Bot.objects.all()
        serializer = BotSerializer(messages, many=True)
        return Response(serializer.data)



    def post(self, request, format=None):

        serializer = BotSerializer(data=request.data)

        if serializer.is_valid():
            
            id = request.user.id  # Get the user's ID
            serializer.save(chatbot_response=request.data['chatbot_response'],id=id)
            message = serializer.validated_data['chatbot_response']
            response_text = generate_chat_response(message)
            serializer.save(chatbot_response=response_text)

            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
