from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

from django.utils import timezone
# Create your models here.

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft') , ('published','Published'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now ) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = CustomManager()

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'year':self.publish.year,'month':int(self.publish.strftime('%m')),\
            'day':int(self.publish.strftime('%d')),'post':self.slug })
    
    
    
# ----------------------Dropdown Choice Field 
# CHOICES = (('a','A') , ('b','B'))
# in this Ex A and B is shown to end User BUT a and b are stored in the backend database 
# used as
# COUNTRY =  (('in','India') , ('us','United States'))
# in model class use as 
# country = models.CharField(max_length=10 , choices=COUNTRY , default='in')

# -----------------------Slug Field 
# used for seo purpose, to build proper human understandable urls 
# slug = models.SlugField(max_length=256 , unique_for_date='published')
# unique_for_date means unique slug per published date 
# i.e there will be one and only unique slug on a particular date no duplicate slug on a same day 

# primary key --> id(default) 

# Foreign Key --> 
# class Posts(models.Model):
#     author = models.ForeignKey(User , related_name='blog_posts')
    
# Field author is many-to-one mapping with respect to model post 
# many-to-one mapping is established by using models.ForeignKey() method 

# DateTime Field 
# from django.utils import timezone
# publishes_Date = models.DateTimeField(default=timezone.now )
# auto_now = True use whenever we use post.save() method that date and time will be saved in database by default 
