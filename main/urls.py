from django.urls import path
from . import views
from .views import blogs
from .views import post_details
from .views import upload
from .views import edit_post, delete_post, add_category

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', blogs.as_view(), name='blog'),
    path('post/<int:pk>', post_details.as_view(), name='post'),
    path('upload/', upload.as_view(), name='upload'),
    path('post/edit/<int:pk>', edit_post.as_view(), name='edit_post'),
    path('post/edit/<int:pk>/remove', delete_post.as_view(), name='delete_post'),
    path('add_category/', add_category.as_view(), name='add_category'),
    path('all_posts/', views.all_posts, name='all_posts'),
    path('cyber_posts/', views.cyber_posts, name='cyber_posts'),

]
