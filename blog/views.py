from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth import authenticate
from blog.forms import PostForm
# Create your views here.


@login_required
def index(request):
    auser = request.user
    return render(request,'blog/index.html',{
        "h_title" :"Home" ,  
        "h_posts": Post.objects.all().filter(author = auser),
        })

    
@login_required
def about(request):
    auser = request.user
    
    return render(request, 'blog/about.html',{
        "h_title": 'About',
        'auser':auser
    })

def contact(request):
    return render(request, 'blog/contact.html', {
        "h_title" :'contact',
    })

def create_post(request):
    auser = request.user
    if auser.is_authenticated:
        if request.method == 'POST':
            pform = PostForm(request.POST)
            
            if pform.is_valid():
                f_title = request.POST['title']
                f_content = request.POST['content']
                f_author = auser
                f = Post(title=f_title,content=f_content,author=f_author)
                f.save()
                return redirect('blog:blog-index')
            else:
                return redirect('blog:blog-about')
            
        else:
            return render(request,'blog/create_post.html',{
                'form_np': PostForm()
                })
        
    else:
        return redirect('accounts:accounts-login')





def edit_post(request):
    pass


def delete_post(request):
    pass