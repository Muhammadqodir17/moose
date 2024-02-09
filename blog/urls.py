from django.urls import path
from .views import home_view, articles_view, about_view, contact_view, blog_detail_view

urlpatterns = [
    path('', home_view),
    path('articles/', articles_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('blog/<int:pk>/', blog_detail_view)
]
