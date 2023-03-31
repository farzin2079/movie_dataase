from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.db import IntegrityError
import requests
import json

from django.contrib.auth.models import User
from users.models import Profile

from .serializer import ProfileSerializer

# API key
key = 'k_9ibqo8d8'
# API URL
url = "https://imdb-api.com/en/API/"


@api_view(['GET'])
def others(request, goal):
    # req_url = f'{url}{goal}/{key}/'
    
    # payload = {}
    # headers= {}

    # response = requests.request("GET", req_url, headers=headers, data = payload) 

    # return Response(response.json())
    return Response('other')



@api_view(['GET'])
def title(request, id):
    # req_url = url + f"title/{key}/{id}"

    # payload = {}
    # headers= {}
    

    # response = requests.request("GET", req_url, headers=headers, data = payload)
    # return Response(response.json())
    return Response('title')


@api_view(['GET'])
def search(request, query):
    # req_url = url + f"searchAll/{key}/{query}"

    # payload = {}
    # headers= {}
    

    # response = requests.request("GET", req_url, headers=headers, data = payload)
    # return Response(response.json())
    return Response('search')


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def profile(request):

    profiles = Profile.objects.get(user=request.user)

    serialize = ProfileSerializer(profiles)
    return Response(serialize.data)

@api_view(['POST'])
def register(request):
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        
        if password != confirmation: 
            # Message
            return Response('faild')
        try:
            registered = User.objects.create_user(username, email, password )
            registered.save()
            return Response('success')
        except IntegrityError:
            return Response('Username already taked')
        