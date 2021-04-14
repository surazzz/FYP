from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
     name= models.CharField(max_length= 128)
     url= models.SlugField()
     def __str__(self):
        return self.name

class Product(models.Model):
     name= models. CharField(max_length=128)
     image= models.ImageField(upload_to= 'upload')
     price= models.IntegerField()
     about= models.TextField()
     stock= models.BooleanField(default= True)
     slug= models.SlugField(max_length= 128, unique= True)
     category= models.ForeignKey(Category, on_delete= models.CASCADE)
     def __str__(self):
        return self.name

class Blog(models.Model):
     image= models.ImageField(upload_to= 'upload')
     name= models. CharField(max_length=128) 
     about= models.TextField()
     date = models.DateField()
     slug= models.SlugField(max_length= 128, unique= True)
     def __str__(self):
        return self.name

class Addtocart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Address(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address_line=models.TextField()
    phone_number=models.IntegerField()

    def __str__(self):
        return self.user.username

class Cartdetail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(Addtocart)
    address=models.ForeignKey(Address, on_delete=models.CASCADE )
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Contactus(models.Model):
    name= models. CharField(max_length=120) 
    email = models.EmailField()
    message= models.TextField()

    def __str__(self):
        return self.name