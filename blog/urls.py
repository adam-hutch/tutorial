from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.createBlogPost, name='create_post'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('<slug:slug>', views.viewBlogPost),

]