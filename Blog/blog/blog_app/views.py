from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from blog_app.forms import AddPost,UpdatePost
from blog_app.models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import authenticate, login



def home(request):
    postlist=Post.objects.all().order_by('-date')
    paginator = Paginator(postlist, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    mydict={'contacts': contacts}
    return render(request,'blog_app/home.html',context=mydict)

@login_required(login_url='login')
def addpost(request):
    if request.method=="GET":
        postform=AddPost()
        mydict={"form":postform}
        return render(request,'blog_app/addpost.html',context=mydict)
    if request.method=="POST":
        postform=AddPost(request.POST ,request.FILES)
        if postform.is_valid():
            pitem=postform.save(commit=False)
            pitem.author=request.user
            pitem.save()
            # postform.save()  only works in model based forms not work on normal forms
            return HttpResponseRedirect(reverse('blog_app:home'))
            # return render(request,'blog_app/home.html',context=mydict)

@login_required
def viewpost(request):
    user = request.user
    user_posts = Post.objects.filter(author=request.user).order_by('-date')
    paginator = Paginator(user_posts, 3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    mydict={'contacts': contacts}
    return render(request,'blog_app/viewpost.html',context=mydict)

@login_required
def updatepost(request,id):
    post=Post.objects.get(id=id)
    if request.method=="POST":
        u_form=UpdatePost(request.POST,request.FILES,instance=post)
        if u_form.is_valid():
            pitem=u_form.save(commit=False)
            pitem.author=request.user
            pitem.date=timezone.now()
            pitem.save()
            return HttpResponseRedirect(reverse('blog_app:viewpost'))
    else:
        u_form=UpdatePost(instance=post)
        mydict={'U_FORM':u_form}
        return render(request,'blog_app/updatepost.html',context=mydict)

def detailview(request,id):
    post=Post.objects.get(id=id)
    return render(request,'blog_app/detailview.html',{'post':post})

@login_required
def deletepost(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return render(request,'blog_app/viewpost.html')

def signup(request):
    sform=UserCreationForm(request.POST or None)
    if sform.is_valid():
        new_user=sform.save()
        new_user = authenticate(username=sform.cleaned_data['username'],password=sform.cleaned_data['password1'],)
        login(request, new_user)
        return HttpResponseRedirect(reverse('blog_app:addpost'))

    return render(request,'blog_app/signup.html',{'sform':sform})
