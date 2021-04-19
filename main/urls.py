from django.urls import path

from main.views import MainTemplateView, GalleryListView, NewsListView, StaffListView, ContactCreateView, NewsDetailView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('staff/', StaffListView.as_view(), name='staff'),
    path('contact/', ContactCreateView.as_view(), name='contact')
]
