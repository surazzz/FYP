from django.urls import path
from commerce.views import ProductListView, ProductDetailView, BlogListView,CartListView, BlogDetailView, UserCreateView, login, logout_view
app_name= "commerce"
urlpatterns = [
    path('', ProductListView.as_view(), name = 'productlist'),
    path('<slug:slug>' ,ProductDetailView.as_view()),
    path('blogs/', BlogListView.as_view(), name = 'bloglist'), 
    path('cart/', CartListView.as_view(), name = 'cartlist'), 
    path('blogs/<slug:slug>' ,BlogDetailView.as_view()),
    path('signup/', UserCreateView.as_view(), name ='signup'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
]
