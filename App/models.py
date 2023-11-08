from django.db import models

class UserProfile(models.Model):
    FirstName = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)
    Email = models.CharField(max_length=100,unique=True)
    Phone = models.CharField(max_length=10,unique=True)
    
    
    def __str__(self):
        return self.FirstName
    

class Profile(models.Model):
    user_id=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    ProfilePicture = models.ImageField(upload_to='profile_pictures/')
    
    def __str__(self) -> str:
        return self.user_id.FirstName
    
