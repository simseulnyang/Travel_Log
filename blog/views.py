from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PostForm, CommentForm, HashTagForm
from .models import Post, Comment, HashTag


# Post
class PostList(View):

    def get(self, request):
        posts = Post.objects.all()
        page = request.GET.get('page', '1')  # 페이지
        paginator = Paginator(posts, 5)  # 페이지당 5개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {
            "title": "PostList",
            "posts": page_obj,
        }
        return render(request, 'blog/post_list.html', context)


class PostWrite(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        context = {
            'title': 'PostWrite',
            'form': form,
        }
        return render(request, 'blog/post_write.html', context)

    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')

        context = {
            'title': 'PostWrite',
            'form': form
        }
        return render(request, 'blog/post_write.html', context)


class PostDetail(View):

    def get(self, request, post_id):
        post = Post.objects.prefetch_related(
            'comment_set', 'hashtag_set').get(pk=post_id)

        comments = post.commnet_set.all()
        hashtags = post.hashtag_set.all()

        comment_form = CommentForm()
        hashtag_form = HashTagForm()

        context = {
            'title': 'PostDetail',
            'post_id': post_id,
            'post_title': post.title,
            'post_content': post.content,
            'post_writer': post.writer,
            'post_created_at': post.created_at,
            'post_hits': post.hits,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': comment_form,
            'hashtag_form': hashtag_form,
        }
        return render(request, 'blog/post_detail.html', context)


class PostUpdate(View):

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(
            initial={'post_title': post.title, 'post_content': post.content})
        context = {
            'title': 'PostUpdate',
            'post': post,
            'form': form,
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data['post_title']
            post.content = form.cleaned_data['post_content']
            post.save()
            return redirect('blog:detail', pk=post_id)

        context = {
            'form': form,
            "title": "Blog"
        }

        return render(request, 'blog/post_edit.html', context)


class PostDelete(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return redirect('blog:list')
