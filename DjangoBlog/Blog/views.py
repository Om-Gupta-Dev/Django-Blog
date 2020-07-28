from django.shortcuts import render , get_object_or_404

from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views.generic import ListView
from Blog.models import Post

# Create your views here.

# def index(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 1)
#     page_number = request.GET.get('page')
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:    #First page when not passing page number
#         posts = paginator.page(1)
#     except EmptyPage:   #last page if not found
#         posts = paginator.page(paginator.num_pages)
#     return render(request , 'Blog/index.html' , {'posts':posts})

def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,
                             publish__month=month,publish__day=day)
    # or 
    # post = Post.objects.get(slug=post,status='published',publish__year=year,
    #                          publish__month=month,publish__day=day)
    return render(request,'Blog/post_detail.html',{'post':post})

# Pagination using Class Based Views 
class Paginator(ListView):
    posts = Post.objects.all()
    paginate_by = 1
    model = Post
    template_name = 'Blog/index.html'