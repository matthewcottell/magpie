from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()  # Fetch all posts (you can add filtering for friends)
    return render(request, "index.html", {"posts": posts})


from django.http import JsonResponse  # ruff: ignore E402, F811
from .models import Post  # ruff: ignore E402, F811
from django.views.decorators.csrf import csrf_exempt  # ruff: ignore E402
from django.utils import timezone  # ruff: ignore E402


@csrf_exempt
def create_post(request):
    if request.method == "POST":
        user = request.user  # You can get the logged-in user here
        content = request.POST.get("content")
        post = Post.objects.create(
            user=user, content=content, created_at=timezone.now()
        )
        return JsonResponse({"post_id": post.id, "content": post.content})
