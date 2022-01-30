

from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.utils import timezone
# from PIL import Image

SIZE = (
    ("XS","XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL")
)

FAVORITE = (
        ("True", "True"),
        ("False", "False"),
    )




class Category(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    
    description = models.TextField(default=None, blank=True, null=True)
    image = models.CharField(max_length=5000, default=None, blank=True, null=True)
    # image = models.ImageField(default='avatar-1.png', upload_to='category_image', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

cat = [ item for item in Category.objects.all().values_list('name', 'name')] 
    


class Product(models.Model):
    
    # id = models.CharField('id', max_length=20, primary_key=True)
    name = models.CharField('Name', max_length=100)
    
    short_description = models.TextField(max_length=150, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    image = models.CharField(max_length=5000, default=None, blank=True, null=True)
    featured_image1 = models.CharField(max_length=2000, default=None, blank=True, null=True)
    featured_image2 = models.CharField(max_length=2000, default=None, blank=True, null=True)
    featured_image3 = models.CharField(max_length=2000, default=None, blank=True, null=True)
    # image = models.ImageField(default='avatar-1.png', upload_to='featured_images', blank=True, null=True)
    # featured_image1 = models.ImageField(default='avatar-1.png', upload_to='featured_images', blank=True, null=True)
    # featured_image2 = models.ImageField(default='avatar-1.png', upload_to='featured_images', blank=True, null=True)
    # featured_image3 = models.ImageField(default='avatar-1.png', upload_to='featured_images', blank=True, null=True)
    # slug= models.SlugField()
    price = models.CharField('Price', max_length=50)
    deleted_price = models.CharField('Deleted Price', max_length=50, blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)
    # sizes = models.CharField(choices=SIZE , max_length=255, default=None, blank=True, null)
    category = models.CharField(choices=cat , max_length=255, default=None)
    # category = models.ManyToManyField(Category, related_name='products', default=None)
    date_added = models.DateField(auto_now_add=True, blank=True, null=True)



    objects = models.Manager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'name'
    set_password = 'password'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk":self.pk})

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    class Meta:
        db_table = 'product'
        verbose_name = 'product'

        verbose_name_plural = verbose_name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, db_constraint=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField(default=None, blank=True, null=True)
    date_added= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
    
    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.product.name} - {self.author}'


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE, db_constraint=False)

    def get_absolute_url(self):
        return reverse('cart', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=None, blank=True, null=True)
    address = models.CharField(max_length=240)
    status = models.CharField(max_length=20, default="Pending")
