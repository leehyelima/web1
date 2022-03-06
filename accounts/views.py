from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from main.models import Menu





# Create your views here.
menu= Menu.objects.all()

def sign_up(request):
    global menu
    context = {'menu' : menu,
        } 
    if User.is_anonymous :
        if request.method == 'POST':
            if (request.POST.get('username') and
                request.POST.get('password') and
                request.POST.get('password') == request.POST.get('password_check')):

                new_user = User.objects.create_user(
                    username = request.POST.get('username'),
                    password = request.POST.get('password'),
                )

                auth.login(request, new_user)
                return redirect('posts:index')

            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
            return render(request, 'accounts/sign_up.html', context)
        elif request.method == 'GET' : 
            return render(request, 'accounts/sign_up.html', context)

    else :
        return redirect('main:index')
        

def login(request):
    global menu
    context = {'menu' : menu,
        } 
    if User.is_anonymous :
        if request.method == 'POST':
            if request.method == 'POST' :
                if request.POST.get('username') and request.POST.get('password') :
                    user = auth.authenticate(
                        username = request.POST.get('username'),
                        password = request.POST.get('password')
                    )

                    if user is not None :
                        auth.login(request,user)
                        return redirect('main:index')
                    else: 
                        context['error'] = '아이디오 비밀번호를 다시 확인해주세요'
                else : 
                    context['error'] ='아이디와 비밀번호를 모두 입력해주세요.'
                    
            return render(request,'accounts/login.html', context)
        else: 
            return redirect('main:index')
        



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('main:index')

def dd(request) :
    HttpResponse('d')