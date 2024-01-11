from django.shortcuts import render
from .models import Image
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# class LoginView(APIView):
#     def post(self,request):
#         username=request.data.get("username")
#         password=request.data.get("password")
#         user=authenticate(username=username,password=password)
#         refresh=RefreshToken.for_user(user)
#         return render(request,'home.html')


# class RestrictedView(APIView):
#     permission_classes=[IsAuthenticated]
def home(request):
    searchTerm = request.GET.get('searchImage')
    if searchTerm:
        images= Image.objects.filter(imagename__icontains=searchTerm)
    else:
        images=Image.objects.all()
    return render(request, 'home.html',	{'searchTerm':searchTerm, 'images':images})