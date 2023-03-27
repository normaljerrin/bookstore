from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=222)
    author = models.CharField(max_length=222)
    description = models.CharField(max_length= 555)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2222, blank=True)
    follow_author = models.CharField(max_length=2222, blank=True)
    book_available = models.BooleanField()
    star = models.FloatField()


    def __str__(self):
        return self.title



class Reggister(models.Model):
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)


class Loggin(models.Model):
    username = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=150, blank=True)


class Order(models.Model):
    product = models.ForeignKey(Book,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.product.title