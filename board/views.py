from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board

# Create your views here.


def index(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}

    return render(request, 'board/list.html', context)


def write(request):
    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.name = request.session['authuser']['name']
    board.user_id = request.session['authuser']['id']

    board.save()

    return HttpResponseRedirect('/board')


def writeform(request):
    # 인증 체크
    # if request.session['authuser'] is None:
    #     return HttpResponseRedirect('/user/loginform')

    user_id = request.session['authuser']
    context = {'user_id': user_id}

    return render(request, 'board/write.html', context)


def view(request):
    id = request.GET['id']
    board = Board.objects.get(id=id)
    context = {'board': board}
    return render(request, 'board/view.html', context)


def modify(request):
    id = request.POST['id']
    board = Board.objects.get(id=id)
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()

    return HttpResponseRedirect('/board')


def modifyform(request):
    id = request.GET['id']
    board = Board.objects.get(id=id)
    user_id = request.session['authuser']['id']
    print(board.user_id)
    print(user_id)
    if board.user_id == user_id:
        context = {'board': board}
        return render(request, 'board/modify.html', context)
    else:
        return HttpResponseRedirect('/board')

def delete(request):
    id = request.GET['id']
    board = Board.objects.get(id=id)
    print(board.user_id)
    user_id = request.session['authuser']['id']
    print(user_id)
    Board.objects.filter(id=id).filter(user_id=user_id).delete()

    return HttpResponseRedirect('/board')