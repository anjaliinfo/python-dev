from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),
]
