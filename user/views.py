from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile, User


# Registration
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')

        form = RegisterForm()
        context = {
            'title': 'Registration',
            'form': form,
        }
        return render(request, 'user/user_register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')
        context = {
            'title': 'Registration',
            'form': form,
        }
        return render(request, 'user/user_login.html', context)


# Login
class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = LoginForm()
        context = {
            'title': 'User',
            'form': form,
        }
        return render(request, 'user/user_login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')

        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=email, password=password)  # True, False

            if user:
                login(request, user)
                return redirect('blog:list')

        # form.add_error(None, '아이디가 없습니다.')

        context = {
            'form': form
        }

        return render(request, 'user/user_login.html', context)


# Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')


# Profile작성
class ProfileWrite(LoginRequiredMixin, View):

    def get(self, request):
        profile = Profile.objects.get(user=request.user.pk)
        form = ProfileForm(initial={
            'profile_img': profile.profile_img,
            'user': profile.user,
            'about_me': profile.about_me
        })
        context = {
            'title': 'Profile_Update',
            'form': form,
        }
        return render(request, 'user/user_profile.html', context)

    def post(self, request):
        user = User.objects.get(pk=request.user.pk)
        profile = Profile.objects.get(user=user)
        about_me = request.POST['about_me']

        try:
            profile_img = request.FILES['profile_img']
        except:
            profile.about_me = about_me
        else:
            profile.profile_img = profile_img
            profile.about_me = about_me

        profile.save()
        return redirect('blog:list')
