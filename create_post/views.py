from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post

#FBV(Function based View)

@login_required(login_url= 'go-login')
def create_post(request):
    context = {}
    
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Post.objects.create(post_title=title, post_body=body)            
        
    return render(request, 'create_blog.html', context)
    
@login_required(login_url= 'go-login')   
def get_blog(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    # print(blog.post_title, blog.post_body)
    context = { 'title': blog.post_title,
                'content' : blog.post_body,
                'image': blog.post_image,
        
    }
    return render(request, "view_single_blog.html", context)

@login_required(login_url= 'go-login')
def getAllBlogs(request):
    blog =Post.objects.all().order_by('id')
  
    
    context = {'blogs' : blog}
    return render(request, "allpost.html", context)
    
    
# Create your views here.




