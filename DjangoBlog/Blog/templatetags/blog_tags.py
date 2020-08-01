from django import template

from Blog.models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()
# can be accessed as by {% total_posts %} 

# --------------------------------------- Applicable to Every type of Custom template Tags ----------------------------
# Note: if you get any error in accessing the custom template tags using this it is because 
        # you don't load the custom tags file in templatetags folder so use {% load blog_tags %}
        # we can't extend this {% load blog_tags %} i.e we have to load template tag in every html file where we want to use custom template tags


@register.inclusion_tag('Blog/latest.html') #'Blog/latest.html' name of the template to which context object is to be passed made by the programmer 
def Latest(count=3):           #Default 3 latest posts but can be overwritten  tag name : Latest
    posts = Post.objects.order_by('-publish')[:count]
    return {'latest':posts}
# can be accessed as by {% for post in latest %} in 'Blog/latest.html' template 

from django.db.models import Count

@register.simple_tag()
def most_commented(count=3):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

# return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
# class Comment(models.Model):
#     post = models.ForeignKey(Post ,related_name = 'comments', on_delete=models.CASCADE)
#     ...
# The comments is referred by related_name defined in the post model 

# return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
# .annotate() method makes a temporary field named as total_comments as defined in .annotate() function 
# and stores total number of comments on every post which is further used by the order_by function to order the posts on the basis of comments
# [:count] is used to pass dynamic value to get the specified number of posts from the template 
# .order_by('-total_comments') is used to sort the output on the basis of total_comments "-" is used to order by descending default id ascending 

# {% most_commented 4 as most_commented_posts %} is used to access most_commented function in templates