from django.core import paginator
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Post, Comment
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm


# def post_list(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 3)  # 3 post each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)

    # list of active comments for this post

    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # a comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create comment object but don't save it to database yet
            new_comment = comment_form.save(commit=False)
            # assaign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })

# will work on it ltr


def post_share(request, post_id):
    # Retrive post by id
    post = get_list_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        # From was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid:
            cd = form.cleaned_data
            # ... send email

        else:
            form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post, 'form': form})


# --> end post share
