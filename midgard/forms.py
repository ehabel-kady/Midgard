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

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=60, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # image = forms.ImageField(upload_to='midgard/static/img/profiles')

    class Meta:
        model = Profiles
        fields = ('username', 'full_name', 'email', 'password1', 'password2',)