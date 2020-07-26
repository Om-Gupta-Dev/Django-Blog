from django.shortcuts import render , get_object_or_404

from Blog.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request , 'Blog/index.html' , {'posts':posts})

def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,
                             publish__month=month,publish__day=day)
    return render(request,'Blog/post_detail.html',{'post':post})