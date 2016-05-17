from django.conf.urls import url
from blog import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    
    url(r'^$', views.index, name='index'),

    url(r'^$', views.edit, name='edit'),

]
