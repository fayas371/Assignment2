from django.urls import path
from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path('users/', UserProfileListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserProfileDetailView.as_view(), name='user-detail'),
]
