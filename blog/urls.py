from django.conf.urls import url
from blog import views
from . import views
from django.conf.urls.static import static
import blog


urlpatterns = [
    url(r'^edit/', views.articles),
    url(r'^contacts/', views.contacts),
    url(r'^services/', views.services),
    url(r'^galerey/', views.galerey),
    url(r'^', views.post_list),
]
