from django.core import paginator
from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Post
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm


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

    return render(request, 'blog/post/detail.html', {'post': post})


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
