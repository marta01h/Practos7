from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
import logging


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

logger = logging.getLogger(__name__)


# Авторизация пользователя с редиректом на разные страницы
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Логика для редиректа на разные страницы
            if user.username == 'user1':  # Например, для пользователя с именем user1
                return redirect('user1_page')  # Редирект на страницу user1
            elif user.username == 'user2':  # Для пользователя user2
                return redirect('user2_page')  # Редирект на страницу user2
            else:
                return redirect('default_page')  # Если ни одно условие не подходит, редирект на страницу по умолчанию
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
def home(request):
    return render(request, 'home.html')  # Создайте шаблон home.html

