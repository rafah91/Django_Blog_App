from django.views import generic
from .models import Post

class PostList (generic.ListView):
    model=Post

class PostDetail(generic.DetailView):
    model=Post
    
class PostCreate (generic.CreateView):
    model=Post
    fields='__all__'
    success_url='/blog/'

class PostEdit (generic.UpdateView):
    model=Post
    fields='__all__'
    success_url='/blog/'
    template_name='posts/edit_post.html'