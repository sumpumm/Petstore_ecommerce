from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    picture=models.ImageField(null=True,blank=False,upload_to="static/images/")
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    price=models.FloatField()
    
    def __str__(self) :
        return self.name

class Customer(models.Model):
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    GENDER_CHOICES=[
        (MALE_CHOICE,'MALE'),
        (FEMALE_CHOICE,'FEMALE'),
        (OTHER_CHOICE,'OTHER')
    ]
    f_name=models.CharField(max_length=255,blank=True,null=True)
    m_name=models.CharField(max_length=255,blank=True,null=True)
    l_name=models.CharField(max_length=255,blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True        
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    
    def __str__(self):
        return self.f_name
    
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    
class CartItems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    
    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    PENDING_CHOICE='P'
    CANCEL_CHOICE='C'
    COMPLETED_CHOICE='CP'
    STATUS_CHOICES=[
        (PENDING_CHOICE,'PENDING'),
        (CANCEL_CHOICE,'CANCEL'),
        (COMPLETED_CHOICE,'COMPLETED'),
    ]
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    status=models.CharField(choices=STATUS_CHOICES,default=PENDING_CHOICE,max_length=2)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    shipping_address=models.CharField(max_length=255)
    
    def __str__(self):
        return self.customer.f_name
    
    
class BillCheckout(models.Model):
    PENDING_CHOICE='P'
    CANCEL_CHOICE='C'
    COMPLETED_CHOICE='CP'
    STATUS_CHOICES=[
        (PENDING_CHOICE,'PENDING'),
        (CANCEL_CHOICE,'CANCEL'),
        (COMPLETED_CHOICE,'COMPLETED'),
    ]
    ESEWA_CHOICE='E'
    COD_CHOICE='C'
    PAYMENT_CHOICES=[
        (ESEWA_CHOICE,'ESEWA'),
        (COD_CHOICE,'COD')
    ]
    payment_method=models.CharField(max_length=1,choices=PAYMENT_CHOICES,default=ESEWA_CHOICE)
    status=models.CharField(choices=STATUS_CHOICES,default=PENDING_CHOICE,max_length=2)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    price=models.FloatField()
    