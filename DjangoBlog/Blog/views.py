from django.shortcuts import render , get_object_or_404

from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views.generic import ListView
from Blog.models import *
from taggit.models import Tag

from Blog.forms import *
# Create your views here.

def index(request,tag_slug=None):
    posts = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:    #First page when not passing page number
        posts = paginator.page(1)
    except EmptyPage:   #last page if not found
        posts = paginator.page(paginator.num_pages)
    return render(request , 'Blog/index.html' , {'posts':posts, 'tag':tag})

def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,
                             publish__month=month,publish__day=day)
    # or 
    # post = Post.objects.get(slug=post,status='published',publish__year=year,
    #                          publish__month=month,publish__day=day)
    
    comments = post.comments.filter(active=True)
    cSubmit = False
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.post = post
            new_comment.save()
            cSubmit = True
    else:
        form = CommentForm()
    return render(request,'Blog/post_detail.html',{'post':post,'form':form,'comments':comments,'csubmit':cSubmit})

from django.core.mail import send_mail

def MailSendView(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    if request.method == "POST":
        form = EmailSendForm(request.POST)
        if form.is_valid():
            values = form.cleaned_data
            send_mail('Subject', values['comments'], values['name'], [values['to']], fail_silently=False )
            sent = True
    
    else:
        form = EmailSendForm()
    return render(request, 'Blog/sendbymail.html', {'form':form, 'post':post, 'sent':sent})


# Pagination using Class Based Views:
# -----------------------------------
# class Paginator(ListView):
#     posts = Post.objects.all()
#     paginate_by = 1
#     model = Post
#     template_name = 'Blog/index.html'

# NOTE: In Class Based Views if we pass page=1000 i.e not the page number it will give 404 but in this Function Based View it returns last page 

# Sending mail via django:
# ------------------------
# Django provides mail Module and send_mail() function 
# SMTP Server 
# SMTP --> Simple Mail Transfer Protocol 

# EMAIL_HOST = SMTP SERVER HOST default value is localhost don't use : insted of =
# EMAIL_PORT = THE SMTP SERVER PORT default is 25
# EMAIL_HOST_USER = "Your Email UserName"
# EMAIL_HOST_PASSWORD = "Your email PASSWORD"
# EMAIL_USE_TLS = Bool
# TRANSPORT LAYER SECURITY

# For Gmail Account:
# ------------------
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = T587
# EMAIL_HOST_USER = "UserName"
# EMAIL_HOST_PASSWORD = "PASSWORD"
# EMAIL_USE_TLS = True 
