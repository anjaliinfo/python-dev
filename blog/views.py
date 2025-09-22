from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def blog_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create.html', {'form': form})

def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/update.html', {'form': form})

def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog:list')
    return render(request, 'blog/delete.html', {'post': post})