from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# def home_page(request):
#     return render(request,"pages/home.html",{})
# def blog_page(request):
#     return render(request,"pages/blog.html",{})
# def post_page(request):
#     return render(request,"pages/post.html",{})
# def about_page(request):
#     return render(request,"pages/about.html",{})
# def blog_page(request):
#     return render(request,"pages/blog.html",{})

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'