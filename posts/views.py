from django.shortcuts import render
from .models import Post 
from .models import Comment
# Create your views here.
def post_list(request):
    data = Post.objects.all()
    return render(request,'all_post.html',{'posts':data})

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'post.html',{'post':data})