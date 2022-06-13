from django.urls import path

from blog.views import BlogApiView

urlpatterns = [
    path('', BlogApiView.as_view()),
]