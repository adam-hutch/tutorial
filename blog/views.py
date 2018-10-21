from django.shortcuts import render,redirect
from .models import BlogPost
from django.shortcuts import get_object_or_404
from .forms import CreateBlogPostForm
from slugify import slugify
import string
import random
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Create your views here.
def home(request):
    query = request.GET.get('s')
    presearch = ''
    if query:
        presearch = query
        posts = BlogPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) ).order_by('-timestamp')
    else:
        posts = BlogPost.objects.filter(active=True).order_by('-timestamp')
    context = {'posts': posts,'presearch':presearch}
    return render(request, 'blog/home.html', context)

def viewBlogPost(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post.html', context) 

@login_required
def createBlogPost(request):
    
    if request.method == "POST":

        title = request.POST.get('title')
        quick_description = request.POST.get('quick_description')
        content = request.POST.get('content')
        img_url = request.POST.get('image_url')
        author = request.user
        slug = id_generator()
        post = BlogPost.objects.create(
                                    title=title,
                                    quick_description=quick_description,
                                    content=content,
                                    img_url=img_url,
                                    author=author,
                                    slug=slug,
                                    )
        post.save()
        return redirect('/blog/' + slug)
    else:   
        form = CreateBlogPostForm()
        return render(request, 'blog/create_post.html', {'form': form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'