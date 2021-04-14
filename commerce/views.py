from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from commerce.models import Product, Blog, Cartdetail
from django.utils import timezone
from django.conf import settings
from commerce.forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as log, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Addtocart, Address, Contactus
import datetime
# Create your views here.

class ProductListView(ListView):
     template_name='commerce/productList.html'
     paginate_by=6 
     model= Product

class ProductDetailView(DetailView):
      template_name='commerce/productdetail.html'
      model= Product
      
      def post(self, request, slug, *args, **kwargs):
        if request.POST.get('quantity')!= None :
            username = request.user
            item = get_object_or_404(Product, slug = slug)
            quantity = request.POST.get('quantity')
            if Addtocart.objects.filter(item = item).exists():
                obj = get_object_or_404(Addtocart, user =username, item=item)
                obj.quantity = obj.quantity+ int(quantity)
                obj.save()
            else:
                s = Addtocart(user = username, item = item, quantity = quantity)
                s.save()
            return redirect('commerce:address')
        return render(request, 'commerce/cart.html')

      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class BlogListView(ListView):
     template_name='blog/blogs.html'
     paginate_by=6
     model= Blog
class CartListView(ListView):
     template_name='commerce/cart.html'
     model= Addtocart

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

def address(request):
    if request.POST.get('address-line') is not None:
        username = request.user
        address_line = request.POST.get('address-line')
        phone_number = request.POST.get('phone-number')

        s = Address(user= username, address_line= address_line, phone_number= phone_number)
        s.save()
        return redirect('commerce:payment')


    cart_data = Addtocart.objects.filter(user=request.user)
    return render(request, 'commerce/address.html', {'data': cart_data})



class ContactusListView(ListView):
     template_name='commerce/contactus.html'
     model= Contactus

     def post(self, request, *args, **kwargs):
         name=request.POST.get('name')
         email=request.POST.get('email')
         message=request.POST.get('message')
         c= Contactus(name=name, email=email, message=message)
         c.save()
         return render(request, 'commerce/contactus.html')

class Payment(DetailView):
    template_name ='commerce/payment.html'
    model=Addtocart

def payment(request):
    if request.POST.get('payment_method') is not None:
        username = request.user
        item= Addtocart.objects.filter(user =username)
        address= Address.objects.filter(user=username).order_by('-id')[0]
        #address =Address.objects.get(user =username)
        s = Cartdetail(user =username, address = address, ordered_date =datetime.datetime.now(), ordered = True)
        s.save()
        s.item.set =item
        s.save()
        return redirect('commerce:productlist')
    return render(request, 'commerce/payment.html') 
    
