from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path("blog/", views.index , name = 'blog-index'),
    path("about/", views.about , name = 'blog-about'),
    path("contact/", views.contact, name = 'blog-contact'),
    path('newpost/',views.create_post,name = 'blog-create_post'),
    

]