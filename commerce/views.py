from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from commerce.models import Product, Blog
from django.utils import timezone
from django.conf import settings
from commerce.forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as log, logout
from django.core.paginator import Paginator
# Create your views here.

class ProductListView(ListView):
     template_name='commerce/productList.html'
     paginate_by=6 
     model= Product

class ProductDetailView(DetailView):
      template_name='commerce/productdetail.html'
      model= Product
      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class BlogListView(ListView):
     template_name='blog/blogs.html'
     paginate_by=6
     model= Blog


class BlogDetailView(DetailView): 
      template_name='blog/blogdetail.html'
      model= Blog
      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'commerce/signup.html'
    success_url=reverse_lazy('commerce:productlist')

def login(request):
    username1=request.POST.get('username')
    password1=request.POST.get('password')
    user=authenticate(request, username=username1, password=password1)
    if user is not None:
       log(request, user)
       return render(request, 'index.html')
    else:
        pass
    return render(request, 'commerce/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')
