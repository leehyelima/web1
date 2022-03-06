from django.shortcuts import render

# Create your views here.


from django.utils import timezone
from django.shortcuts import redirect, render
from main.models import Menu
from .models import Board
from django.contrib.auth.decorators import login_required


menu= Menu.objects.all()



def index(request):
    inner = Menu.objects.get(name = "board")
    global menu
    posts = Board.objects.all().order_by('-created_at')
    context = {
        'menu' : menu,
        'body' : inner.body,
        'posts': posts,
    }
    return render(request, 'board/index.html', context)  


@login_required
def create(request): 
    inner = Menu.objects.get(name = "board")
    global menu
    context = {
        'menu' : menu,
        'body' : inner.body,
    }

    if request.method =="POST" :
        user = request.user
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        image = request.FILES.get('image')

        post = Board(user=user, subject = subject, body=body, image=image, created_at=timezone.now())
        post.save()
        
        return redirect('board:detail', post_id=post.id)

    elif request.method =="GET" :

        return render(request, 'board/create.html',context)
   
    

def detail(request,post_id):
    post = Board.objects.get(id = post_id)
    inner = Menu.objects.get(name = "board")
    global menu

    context = {
        'menu' : menu,
        'body' : inner.body,
        'post' : post,
    }
    return render(request, "board/detail.html", context)  

@login_required
def edit(request,post_id):
    inner = Menu.objects.get(name = "board")
    global menu

    if request.method == "POST":
        try:
            post = Board.objects.get(id=post_id, user=request.user)
        except Board.DoesNotExist :
            redirect('board:list')
        
        post.subject = request.POST.get('subject')
        post.body =request.POST.get('body')
        image = request.FILES.get('image')
        
        if image :
            post.image = image
        post.save()

        return redirect('board:detail', post_id = post.id) 

    elif request.method == "GET" :
        try:
            post = Board.objects.get(id=post_id, user=request.user)

        except Board.DoesNotExist :
            return redirect('board:list')

        context ={
            'post': post,
            'menu': menu,
            'body': inner.body,}
        return render(request, 'board/edit.html',context)



@login_required
def delete(request,post_id) :
    try :
        post = Board.objects.get(id=post_id, user=request.user)
    except:
        redirect('board:list')
    
    post.delete()
    return redirect('board:list')

    
def search(request,keyword) :
    post =Board.objects.filter(user_text__search='Cheese')
    inner = Menu.objects.get(name = "board")
    global menu
    context = {
        'menu' : menu,
        'body' : inner.body,
        'post' : post,
    }

    return render(request, 'board/index.html', context) 


