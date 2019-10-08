from django.urls import path
from django.views.generic import TemplateView
from .views import about, PostView


# app_name = 'blog'
urlpatterns = [
    path('', TemplateView.as_view(template_name="base.html"), name='home'),
    path('about', about, name='about'),
    path('posts', PostView.as_view(), name='posts'),
]