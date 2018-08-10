from django.shortcuts import render, get_object_or_404
from .models import Post 

# Create your views here.
def home(request):
  posts = Post.objects.order_by('-publish_date')

  return render(request, 'posts/home.html', {'posts':posts})

def post_details(request, post_id):
  # pk means primary key
  post = get_object_or_404(Post, pk=post_id) #Post.objects.get(pk=post_id)
  return render(request, 'posts/post_details.html', {'post':post})