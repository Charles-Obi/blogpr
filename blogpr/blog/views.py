from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, CustomUser
from .forms import PostCreateForm, UserLoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

@login_required
def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5, orphans=4, allow_empty_first_page=True)
    page = request.GET.get('page')
    user = request.user
    print(user)

    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': paginated_posts, 'user': user})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PostCreateForm()
    return render(request, 'blog/post_create.html', {'form': form})

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostCreateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PostCreateForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form})

def post_delete(request, id):

    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    
    return render(request, 'blog/post_delete.html', {'post': post})

def user_login(request):
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                try:
                    Custom_User=CustomUser.objects.get(user=user)
                except CustomUser.DoesNotExist:
                    Custom_User=None

                if Custom_User and Custom_User.role == 'admin':
                    return redirect('list')
                else:
                    return redirect('index')
            else:
                print('Invalid username or password')
    else:
        form = UserLoginForm()

    return render(request, 'blog/login.html', {'login_form': form})

