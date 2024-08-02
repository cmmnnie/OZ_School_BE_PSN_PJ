from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm

# 로그인 뷰
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_list')     # 로그인 성공 시 유저 리스트 페이지로 리다이렉트
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# 회원가입 뷰
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')       # 로그인 페이지로 리다이렉트
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# 유저 리스트 뷰
def user_list_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


# 로그아웃 뷰
def logout_view(request):
    logout(request)
    return redirect('login')         # 로그아웃 후 로그인 페이지로 리다이렉트