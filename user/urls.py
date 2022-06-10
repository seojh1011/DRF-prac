from django.urls import path
from user.views import UserApiView

urlpatterns = [
    path('', UserApiView.as_view()),
]