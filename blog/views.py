from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.template.loader import get_template
from django.shortcuts import render
from .models import Post


def about(request):
    # t = get_template("about.html")
    c = {}
    # return HttpResponse(t.render(c, request))
    return render(request, "about.html", c)


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "posts.html", {'posts': posts})


