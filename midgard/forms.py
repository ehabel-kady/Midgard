# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import Profiles

# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = Profiles
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta(UserChangeForm):
#         model = Profiles
#         fields = ('username', 'email')
from django.contrib.auth import get_user_model

User = get_user_model()