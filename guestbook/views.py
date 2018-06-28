from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list': guestbook_list}

    return render(request, 'guestbook/list.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.message = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    print(request)
    return render(request, 'guestbook/deleteform.html')


def delete(request):
    pass