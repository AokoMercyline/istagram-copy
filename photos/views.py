from django.shortcuts import render, redirect
from .forms import ProfileForm,ImageForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Profile,Comments,Likes

# def index(request):
   
#         return render(request, 'istagram/index.html')

# @login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.get_all_images()
    profile = Profile.get_all_profiles()
    comments=Comments.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('index')
    else:
        form=CommentForm
    context =  {
        "profile": profile,
        "form": form,
        "posts":posts ,
        "comments":comments,
    }
    return render(request, 'istagram/index.html', context)
    

def add_image(request):
        current_user = request.user
        if request.method == 'POST':
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('index')
        else:
                form = ImageForm()
                return render(request,'istagram/image.html', {"form":form})

def profile_info(request):
        posts = request.user.image_set.all()
        return render(request, 'istagram/profile.html', {"images": posts})