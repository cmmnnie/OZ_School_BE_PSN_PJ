# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# User = get_user_model()

# class SignupForm(UserCreationForm):
#   class Meta(UserCreationForm.Meta):
#     model = User


# class UserRegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
from django.contrib.auth import get_user_model
User = get_user_model()


from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)