from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from user.models import User

# Create your views here.


def joinform(request):
    return render(request, 'user/joinform.html')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save()

    return HttpResponseRedirect('/user/joinsuccess')


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    resutl = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password'])

    # 로그인 실패
    if len(resutl) == 0:
        return HttpResponseRedirect('/user/loginform?result=false')

    # 로그인 처리
    authuser = resutl[0]
    request.session['authuser'] = model_to_dict(authuser)

    return HttpResponseRedirect('/')


def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')