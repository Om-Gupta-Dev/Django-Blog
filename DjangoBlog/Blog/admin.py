from django.contrib import admin

from Blog.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']  #can be tuple 
    list_filter = ['status','author']    #can be tuple 
    search_fields = ('title','slug','author__username','body','publish','created','updated','status')   #can be list
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}                    

# Register your models here.

admin.site.register(Post , PostAdmin)

# list_filter = ['status','author']
# shows a filtering panel at right side in the admin page on the basis of status and author 

# prepopulated_fields = {'slug':('title',)} 
# A dictionary key->which has to be filled 
# Value->From which value key will be filled must be a list or a tuple 
# will fill slug field based on title field 

# Search Fields to be searched when searched in admin panel 
# author__username -->
# here the author field is pointing to User table but not any field to search, in the User table thats why 
# we have to give the fieldname using __Field method 
# the default User Model Class is like --->
# class User(is_superuser, groups, user_permissions, password, last_login, username, email, is_active, first_name, last_name, is_staff, date_joined)
# we need to specify which fields in the User/author table to match on (the default is the primary key , which doesnt make sense here).

# raw id field -->
# it shows an input box for id and replace it by user name in database when saved instead of selecting name from drpdown 

# date_hierarchy 
# Adds a navigation bar in the admin panel to navigate to different years, dates and months.

# ordering = ['status','publish']
# order on the basis of status and if the status is same order on the basis of publish and so onn..