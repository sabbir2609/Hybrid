from django.urls import path
from . import views
from .views import PostListView

app_name = 'blog'

urlpatterns = [
    # post views
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail')
]
