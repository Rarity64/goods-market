from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    try:
        context = { 'username' : request.user.username }
        return render(request, 'index.html', context)
    except AttributeError as e:
        return render(request, 'index.html')

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        # \n (терминальный n) - это перенос строки
        print('Логин: ', username, '\n', 'Пароль: ', password, sep='')

        # Авторизация: здесь ищется зарегистрированный пользователь
        user = authenticate(request, username=username, password=password)
        if user is not None: # Если пользователь есть
            print('Нашелся пользователь ', user.username)
            login(request, user)
            JsonResponse({'status' : 'success', 'message' : 'Пользователь авторизован'})
        else:
            JsonResponse({'status' : 'error', 'message' : 'Пользователь не найден'})
    return render(request, 'auth.html')

def reg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        birthday = request.POST.get('birthday')
        username = email

        print('Почта: ', email, '\n', 'Пароль: ', password, 'Имя: ', first_name, sep='')

        user = User.objects.create_user(username, email, password)

        login(request, user)

        return JsonResponse({'status': 'success'})

    return render(request, 'reg.html')

def logout_view(request):
    logout(request)
    return redirect('index')