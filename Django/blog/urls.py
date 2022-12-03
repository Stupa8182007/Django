from django.urls import path
from django.contrib import admin
from blog.views import CategoryListView, PostByCategoryView
from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
)
urlpatterns = [
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('admin/', admin.site.urls),
    # path('accounts/logout/', CategoryListView.as_view(), name='category_list'),
    # path('accounts/login/', CategoryListView.as_view(), name='category_list'),
    path('', CategoryListView.as_view(), name='category_list'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),     
]

