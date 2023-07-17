from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from .models import Post

### Post
class PostList(View):
    
    def get(self, request):
        posts = Post.objects.all()
        page = request.GET.get('page', '1') # 페이지
        paginator = Paginator(posts, 10) # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {
            "title" : "PostList",
            "posts" : page_obj,
        }
        return render(request, 'blog/post_list.html', context)