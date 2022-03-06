
import django
from django.utils import timezone
from django.shortcuts import redirect, render
from main.models import Menu
from .models import Post
from django.contrib.auth.decorators import login_required


menu= Menu.objects.all()



def index(request):
    inner = Menu.objects.get(name = "board")
    global menu
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'menu' : menu,
        'body' : inner.body,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)  


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

        post = Post(user=user, subject = subject, body=body, image=image, created_at=timezone.now())
        post.save()
        
        return redirect('posts:detail', post_id=post.id)

    elif request.method =="GET" :

        return render(request, 'posts/create.html',context)
   
    

def detail(request,post_id):
    post = Post.objects.get(id = post_id)
    inner = Menu.objects.get(name = "board")
    global menu

    context = {
        'menu' : menu,
        'body' : inner.body,
        'post' : post,
    }
    return render(request, "posts/detail.html", context)  

@login_required
def edit(request,post_id):
    inner = Menu.objects.get(name = "board")
    global menu

    if request.method == "POST":
        try:
            post = Post.objects.get(id=post_id, user=request.user)
        except Post.DoesNotExist :
            redirect('posts:list')
        
        post.subject = request.POST.get('subject')
        post.body =request.POST.get('body')
        image = request.FILES.get('image')
        
        if image :
            post.image = image
        post.save()

        return redirect('posts:detail', post_id = post.id) 

    elif request.method == "GET" :
        try:
            post = Post.objects.get(id=post_id, user=request.user)

        except Post.DoesNotExist :
            return redirect('posts:list')

        context ={
            'post': post,
            'menu': menu,
            'body': inner.body,}
        return render(request, 'posts/edit.html',context)



@login_required
def delete(request,post_id) :
    try :
        post = Post.objects.get(id=post_id, user=request.user)
    except:
        redirect('posts:list')
    
    post.delete()
    return redirect('posts:list')

    
def search(request,keyword) :
    post =Post.objects.filter(user_text__search='Cheese')
    inner = Menu.objects.get(name = "board")
    global menu
    context = {
        'menu' : menu,
        'body' : inner.body,
        'post' : post,
    }

    return render(request, 'posts/index.html', context) 


