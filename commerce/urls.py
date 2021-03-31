from django.urls import path
from commerce.views import ProductListView, ProductDetailView, BlogListView, BlogDetailView
app_name= "commerce"
urlpatterns = [
    path('', ProductListView.as_view(), name = 'productlist'),
    path('<slug:slug>' ,ProductDetailView.as_view()),
    path('blogs/', BlogListView.as_view(), name = 'bloglist'),  
    path('blogs/<slug:slug>' ,BlogDetailView.as_view()),

]
