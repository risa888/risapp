from django.shortcuts import render
from .models import Post,Comments
from .forms import PostForm,CommentsForm
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url='/admin/login/')
# def index(request):
#     return HttpResponse('')
    
#     return render(request, 'risapp/index.html', params)
def index(request):
    params = {
        'title':'HELLO/EVERYBODY',
        'who':'Who are you??',
    }
    return render(request, 'risapp/base.html', params)

def article_create_view(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()

    params = {
        'form': form
    }
    return render(request, "risapp/article_create.html", params)


def article_view(request):
    post = Post.objects.get(id=5)
    params = {
        'author': post.author,
        'caption': post.caption,
        'created_date': post.created_date,
        'tag_name': post.tag_name,
        'photo': post.photo
    }
    return render(request, "risapp/index.html", params)

def comments_create(request):
    com_form = CommentsForm(request.POST)
    if com_form.is_valid():
        com_form.save()

    params = {
        'com_form':com_form
    }
    return render(request,"risapp/comment_create.html",params)

def comments_view(request):
    com =  Comments.objects.get(id=1)
    params = {
        'user':com.user,
        'post':com.post,
        'posted_date':com.posted_date
    }
    return render(request, "risapp/comment_create.html",params)
