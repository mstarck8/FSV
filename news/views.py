from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import PostForm
from .models import NewsPost


def index(request):
    return render(request, 'news/index.html')


def timeline_view(request):
    post_form = PostForm()
    posts = NewsPost.objects.order_by('-created_at')
    return render(request, 'news/timeline.html', {'posts': posts, 'post_form': post_form})


@login_required
@require_POST
def create_view(request):
    post_form = PostForm(request.POST)
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.user = request.user
        post.save()
    return redirect('news:timeline')


@login_required
@require_POST
def delete_view(request, post_id):
    post = get_object_or_404(NewsPost, id=post_id, user=request.user)
    post.delete()
    return redirect('news:timeline')


def artikel_view(request, post_id):
    post = get_object_or_404(NewsPost, id=post_id)
    return render(request, 'news/artikel.html', {'post': post})
