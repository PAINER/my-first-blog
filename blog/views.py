from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.http import HttpResponse
from django.template import Context, loader

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
 
def index(request):
    entries = BlogEntry.objects.all()
    template = loader.get_template('blog/index.html')
    context = Context({'entries': entries})
    return HttpResponse(template.render(context))

def edit(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/edit.html', {'questionName': edit})