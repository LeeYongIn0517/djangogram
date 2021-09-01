from django.shortcuts import render, get_object_or_404
from djangogram.users.models import User as user_model
from django.db import models
# Create your views here.
def index(request):
    return render(request, 'posts/base.html')

def posts_create(request):
    if request.method == 'GET':
        return render(request, 'posts/posts_create.html')

    elif request.method == 'POST':
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, pk=request.user.id)
            
            image = request.FilES['image']
            caption = request.POST['caption']

            new_post = models.Post.objects.create(
                author = user,
                image = image,
                caption = caption
            )
            new_post.save()

            return render(request, 'posts/base.html')
        else:
            return render(request, 'users/main.html')