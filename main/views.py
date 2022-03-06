
from django.shortcuts import render
from .models import Menu




menu= Menu.objects.all()

# Create your views here.
def index(request):
    inner = Menu.objects.get(name = "about")
    global menu
    context = {
        'menu' : menu,
        'body' : inner.body,
    }
    return render(request, 'main/index.html', context)  



def newmenu(request,newmenu) :
    
    global menu
    inner = Menu.objects.get(name = newmenu)
    try :
        
        context = {'menu' : menu, 'body' : inner.body,}
        return render(request, 'main/index.html', context) 
    except:
        context = {'menu' : menu, 
        'body' :  '<div id="about" class="resume_section"> <h1 class="section-title"><span class="highlight">NO</span> Page</h1> <div class="section-sub-desc">Page does not Exist</div> <p class="section-desc"> please check urls again. page does not exist</p> <ul class="section-icons"></div>'
        }
        return render(request, 'main/index.html', context) 
