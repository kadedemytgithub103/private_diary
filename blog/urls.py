from django.urls import path

from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name="blog_index"),
    path('inquiry/', views.BlogInquiryView.as_view(), name="blog_inquiry"),
]