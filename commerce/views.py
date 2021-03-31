from django.shortcuts import render
from django.views.generic import ListView, DetailView
from commerce.models import Product, Blog
from django.utils import timezone
# Create your views here.

class ProductListView(ListView):
     template_name='commerce/productList.html'
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
     model= Blog


class BlogDetailView(DetailView): 
      template_name='blog/blogdetail.html'
      model= Blog
      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context