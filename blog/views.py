from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Q

from django.views import View

from .forms import PostForm, CommentForm, HashTagForm
from .models import Post, Category, Comment, HashTag


# Post
class PostList(View):

    def get(self, request):
        page = request.GET.get('page', '1')
        search_type = self.request.GET.get('type', '')
        search_keyword = self.request.GET.get('q', '')
        posts = Post.objects.order_by('-created_at')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'category':
                    posts = posts.filter(
                        Q(category_id__name__icontains=search_keyword)).distinct()
                elif search_type == 'title_content':
                    posts = posts.filter(Q(title__icontains=search_keyword) | Q(
                        content__icontains=search_keyword)).distinct()
                elif search_type == 'title':
                    posts = posts.filter(
                        Q(title__icontains=search_keyword)).distinct()
                elif search_type == 'content':
                    posts = posts.filter(
                        Q(content__icontains=search_keyword)).distinct()

        paginator = Paginator(posts, 5)  # 페이지당 5개씩 보여주기

        try:
            page_obj = paginator.get_page(page)
        except PageNotAnInteger:
            page = 1
            page_obj = Paginator.get_page(page)
        except EmptyPage:
            page = paginator.num_pages
            page_obj = Paginator.get_page(page)

        context = {
            "title": "PostList",
            'posts': page_obj,
            'p_count': posts,
            'page': page,
            'q': search_keyword,
            'type': search_type,
        }

        return render(request, 'blog/post_list.html', context)


class PostWrite(LoginRequiredMixin, View):

    def get(self, request):
        category = Category.objects.all()
        form = PostForm()
        context = {
            'title': 'PostWrite',
            'form': form,
            'category': category,
        }
        return render(request, 'blog/post_write.html', context)

    def post(self, request):
        category = Category.objects.all()
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')

        context = {
            'title': 'PostWrite',
            'form': form,
            'category': category,
        }
        return render(request, 'blog/post_write.html', context)


class PostDetail(View):

    def get(self, request, pk):
        post = Post.objects.prefetch_related(
            'comment_set', 'hashtag_set').get(pk=pk)
        post.hits += 1  # 해당 게시글 클릭만으로 조회수 올리기

        comments = post.comment_set.all()
        hashtags = post.hashtag_set.all()

        comment_form = CommentForm()
        hashtag_form = HashTagForm()

        context = {
            'title': 'PostDetail',
            'pk': pk,
            'post_category': post.category,
            'post_title': post.title,
            'post_content': post.content,
            'post_writer': post.writer.nickname,
            'post_created_at': post.created_at,
            'post_hits': post.hits,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': comment_form,
            'hashtag_form': hashtag_form,
        }

        post.save()

        return render(request, 'blog/post_detail.html', context)


class PostUpdate(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        category = Category.objects.all()
        form = PostForm(
            initial={'category': post.category, 'title': post.title, 'content': post.content})
        context = {
            'title': 'PostUpdate',
            'post': post,
            'category': category,
            'form': form,
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        category = Category.objects.all()
        form = PostForm(request.POST)

        if form.is_valid():
            post.category = form.cleaned_data['category']
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)

        context = {
            "title": "Blog",
            'post': post,
            'form': form,
            'category': category,
        }

        return render(request, 'blog/post_edit.html', context)


class PostDelete(View):

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('blog:list')


# Comment
class CommentWrite(LoginRequiredMixin, View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)
        post.hits -= 1
        post.save()
        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user

            try:
                comment = Comment.objects.create(
                    post=post, content=content, writer=writer)
            except ObjectDoesNotExist as e:
                print('Post does not exist.', str(e))
            except ValidationError as e:
                print('Valdation error occurred.', str(e))

            return redirect('blog:detail', pk=pk)

        # hashtag_form = HashTagForm()

        context = {
            'title': 'PostDetail',
            'post_id': pk,
            'comments': post.comment_set.all(),
            # 'hashtags': post.hashtag_set.all(),
            'comment_form': form,
            # 'hashtag_form': hashtag_form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:detail', pk=post_id)


# HashTag
class HashTagWrite(LoginRequiredMixin, View):

    def post(self, request, pk):
        form = HashTagForm(request.POST)
        post = get_object_or_404(Post, pk=pk)

        if form.is_valid():
            name = form.cleaned_data['name']
            writer = request.user

            try:
                hashtag = HashTag.objects.create(
                    post=post, name=name, writer=writer)
            except ObjectDoesNotExist as e:
                print('Post does not exist.', str(e))
            except ValidationError as e:
                print('Valdation error occurred', str(e))

            return redirect('blog:detail', pk=pk)

        comment_form = CommentForm()

        context = {
            'title': 'Blog',
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': comment_form,
            'hashtag_form': form
        }

        return render(request, 'blog/post_detail.html', context)


class HashTagDelete(View):

    def post(self, request, pk):
        hashtag = get_object_or_404(HashTag, pk=pk)
        post_id = hashtag.post.id

        hashtag.delete()

        return redirect('blog:detail', pk=post_id)
