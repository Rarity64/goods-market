from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Good, UserProfile
from django.core.mail import send_mail

def index(request):
    try:
        context = { 'username' : request.user.username }
        return render(request, 'index.html', context)
    except AttributeError:
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

        user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)

        login(request, user)

        return JsonResponse({'status': 'success'})

    return render(request, 'reg.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def catalog_view(request, food_type):
    food_type_name = ''

    if food_type == 'all':
        good = Good.objects.all()
        food_type_name = 'Всё'
    else:
        good = Good.objects.filter(food_type = food_type)

        food_types = Good.food_types
    
        for ft in food_types:
            if ft[0] == food_type:
                food_type_name = ft[1]
                break
            
    context = {
        'good_list' : good,
        'food_type' : food_type_name
    }
    return render(request, 'catalog.html', context)

def good_template(request, id):
    good = Good.objects.get(id = id) # конструктор класса
    context = { 
        'good' : good
    }
    return render(request, 'good-template.html', context)

def account(request):
    print(request.user.id)
    try:
        context = {
            'username' : request.user.username,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email,
        }
        return render(request, 'account.html', context)
    except AttributeError:
        return HttpResponse('<h1>401 Unauthorized</h1>', status=401)
    
def email(request):
    if request.method == 'POST' and request.POST.get('email'):
        email = request.POST.get('email')
        print('Получилось взять имейл: ', email)
        return JsonResponse({'status': 'success'})
    return HttpResponse(status=200)