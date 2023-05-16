from django.shortcuts import render,HttpResponse, redirect
import openai
import os
from . models import Bot,Profile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required



openai.api_key = os.getenv("OPENAI_API_KEY")


def chat(request):
    return render(request,'index.html')

@login_required
def chatbot(request):
    user=request.user
    data=Bot.objects.filter(user_chatbot=user)
    return render(request,'chatbot.html',{'data':data})

def chatbot_login(request):
    return render(request,'login.html')

def chatbot_register(request):
    return render(request,'register.html')


def profile(request):
    user=request.user
    details=Profile.objects.filter(user_details=user)
    return render(request,'profile.html',{'details':details})


@login_required
def history(request):
    user=request.user
    data=Bot.objects.filter(user_chatbot=user)
    return render(request,'history.html',{'data':data})

@csrf_exempt
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already exists')
            return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return render(request,'register.html')
        else:
            user=User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            messages.info(request,'Register successfully')
            return render(request,'login.html')
    else:
        return redirect('/register')    


@csrf_exempt
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Logged in Successfully !!')
            user=request.user
            data=Bot.objects.filter(user_chatbot=user)
            return render(request,'chatbot.html',{"data":data})
        else:
            messages.error(request, 'Invalid username or password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')



@login_required
def lgout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout ')
    return redirect('/') 



@login_required
@csrf_exempt
def chatapi(request):
    if request.method=='POST':
        user=request.user
        user_input= request.POST['message']


        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        chatbot_response = response.choices[0].text.strip()
        Bot.objects.create(user_chatbot=user,user_input=user_input,chatbot_response=chatbot_response)
        data=Bot.objects.filter(user_chatbot=user)
        
        return render(request,'chatbot.html',{'data':data})
    else:
        HttpResponse(" Bad Request")

        

@login_required
def delete_chat(request):
    user=request.user
    Bot.objects.filter(user_chatbot=user).delete()
    data=Bot.objects.filter(user_chatbot=user)
    return render(request,'history.html',{"data":data})  


@login_required
def delete_profile(request):
    user=request.user
    Profile.objects.filter(user_details=user).delete()
    details=Profile.objects.filter(user_details=user)
    return render(request,'profile.html',{"details":details})  
   

@csrf_exempt
def add_profile(request):
    if request.method == 'POST':
        user=request.user
        user_mob=request.POST['user_mob']
        user_address=request.POST['user_address']
        user_img=request.FILES['user_img']
        if Profile.objects.filter(user_mob=user_mob):
            messages.error(request,"Mobile number already used")
            return render(request,'profile.html')
        else:
            Profile.objects.create(user_details=user,user_mob=user_mob,user_address=user_address,user_img=user_img)
            details=Profile.objects.filter(user_details=user)
            return render(request,'profile.html',{'details':details})
    else:
        details=Profile.objects.filter(user_details=user)
        return render(request,'profile.html',{'details':details}) 


def deactivate(request):
    user=request.user
    user.delete()
    messages(request,"Account deactivated successfully ")
    return render(request,'register.html')








       
 