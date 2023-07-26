from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile
User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'nickname']


class LoginForm(AuthenticationForm):
    # email = forms.EmailField(widget=forms.EmailInput(
    #     attrs={'placeholder': 'email을 입력해주세요.', 'style': 'border : 1px solid #ddd'}), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password를 입력해주세요.', 'style': 'border : 1px solid #ddd'}), label='Password')

    class Meta:
        model = User
        fields = ['email', 'password']


class ProfileForm(forms.ModelForm):

    nickname = forms.CharField(max_length=20)

    class Meta:
        model = Profile
        fields = ['profile_img', 'about_me']
