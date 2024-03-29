from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm


def blog_index(request):
    blogs = Post.objects.all().order_by('-created_on')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
    cats = Post.objects.get(pk=pk).categories.all()
    coms = Comment.objects.filter(cos=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                cos=blog
            )
            comment.save()
    comments = Comment.objects.filter(cos=blog)
    context = {
        'blog': blog,
        'cats': cats,
        'coms': coms,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog_detail.html', context)


def blog_category(request, category):
    blogs = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "blogs": blogs
    }
    return render(request, "blog_category.html", context)

