from rest_framework import serializers
from .models import UserProfile,Profile
from rest_framework.response import Response
from rest_framework import status
from django import forms  

class UserProfileSerializer(serializers.ModelSerializer):
    
    FirstName = serializers.CharField(max_length=100)
    Password = serializers.CharField(max_length=200, write_only=True)
    Email = serializers.CharField(max_length=100)
    Phone = serializers.CharField(max_length=10)
    ProfilePicture = serializers.ImageField(write_only=True)
    
    class Meta:
        model = UserProfile  # Specify the model associated with the serializer
        fields = '__all__'


    def create(self, validated_data):
        email = validated_data.get('Email')
        phone = validated_data.get('Phone')
        
        if UserProfile.objects.filter(Email=email).exists() or UserProfile.objects.filter(Phone=phone).exists():
            return Response({"message": "User with this email or phone already exists."}, status=status.HTTP_400_BAD_REQUEST)
        user_profile_data = {k: validated_data[k] for k in UserProfile._meta.get_fields()}
        profile_data = {k: validated_data[k] for k in Profile._meta.get_fields()}

        user_profile = UserProfile(**user_profile_data)
        user_profile.save()

        profile_data['user_id'] = user_profile
        profile = Profile(**profile_data)
        profile.save()

        return user_profile


    def create(self, request, *args, **kwargs):
        # Check if a user with the same email or phone exists
        email = request.data.get('Email')
        phone = request.data.get('Phone')
        
        if UserProfile.objects.filter(Email=email).exists() or UserProfile.objects.filter(Phone=phone).exists():
            return Response({"message": "User with this email or phone already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
    
    def __init__(self, *args ,**kwargs):
        super(UserProfileSerializer,self).__init__(*args, **kwargs)
    
        self.fields['Password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        