from django.db import models
from autoslug import AutoSlugField
from PIL import Image


from django.contrib.auth.models import User

class Customer(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=240, default=None)
    last_name = models.CharField('Last Name', max_length=240, default=None)
    email = models.EmailField(default=None)
    username=models.CharField("Username", max_length=240, blank=True, null=True)
    password1 = models.CharField('Password', max_length=10, default='111111')
    password2 = models.CharField('Password2', max_length=10, default='111111')
    registrationDate = models.DateField("Registration Date", auto_now_add=True, blank=True, null=True)
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    # status= models.BooleanField(default=False)
    # salary=models.PositiveIntegerField(null=True)
    @property
    def get_name(self):
        return self.first_name+" "+self.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.first_name



class Profile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user', null=True)
    address = models.CharField(max_length=240)
    profile_pic= models.ImageField(default='default.png', upload_to='profile_pic/Users/',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=False)
    # bio = models.TextField(default='', blank=True, null=True)
    # birthday = models.DateField('Birthday', blank=True, null=True)
    # registrationDate = models.DateField("Registration Date", auto_now_add=True, blank=True, null=True)

    # image = models.ImageField(default='default.png', upload_to='profile_pics', blank=True, null=True)
    # coverimage = models.ImageField(default='default_cover.jpg', upload_to='cover_pics', blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return "/users/profile/{}".format(self.slug)
        # return reverse('profile_view', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
