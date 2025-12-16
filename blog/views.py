from django.shortcuts import render, get_object_or_404 
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    

class PostDetailView(DetailView):
    queryset = Post.published.all()
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'    

def handlePostRecommendationForm(request,post_id):
    post =  get_object_or_404(
            Post,
            id=post_id,
            status = Post.Status.PUBLISHED
        )
    if request.method == 'POST':
        form = PostRecommendationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = PostRecommendationForm()
    return render(
        request,
        'blog/share.html',
        {'post': post,
         'form': form}
    )
