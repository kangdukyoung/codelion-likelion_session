from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username = username).exists():
            return render(request, 'signup.html', {'error':"이미 존재하는 사용자입니다."})

        if password == request.POST['passwordCheck']:
            user = User.objects.create_user(username=username, password=password)
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'error':"비밀번호가 일치하지 않습니다."})   
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':"id or pwd 다시확인해라"})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
