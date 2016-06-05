from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.http.response import HttpResponse
from jinja2 import Template
from django.template.loader import get_template
from django.template import context
import blog
from django.shortcuts import render_to_response

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/base.html', {'posts': posts})


def template(request):
   view = "template"
   t = get_template('base.html')
   html = t.render(context({'name': view}))
   return HttpResponse(html)

def articles(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts': posts})

def contacts(request):
  return render_to_response('edit.html')

def services(request):
  return render_to_response('services.html') 

def galerey(request):
  return render_to_response('galerey.html') 


