from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'posts/base.html')

def posts_create(request):
    if request.method == 'GET':
        return render(request, 'posts/posts_create.html')
    elif request.method == 'POST':
        pass