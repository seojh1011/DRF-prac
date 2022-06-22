from django.urls import path
from user.views import UserApiView

urlpatterns = [
    path('', UserApiView.as_view()),
    path('product', UserApiView.as_view()),
    path('product/<int:id>', UserApiView.as_view()),
]