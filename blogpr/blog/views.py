from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostCreateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def hello(request):
    return HttpResponse("This is our Basic Blog!")

def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5, orphans=4, allow_empty_first_page=True)
    page = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': paginated_posts})

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