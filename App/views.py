from django.shortcuts import render
from django.db.models import F
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileListCreateView(generics.ListCreateAPIView):
    
    queryset = UserProfile.objects.annotate(ProfilePicture=F('profile__ProfilePicture'))
    serializer_class = UserProfileSerializer

    
    

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
