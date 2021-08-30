from django.urls import path, re_path
from . import views

urlpatterns = [
    path("user/signup", views.SignupView.as_view()),
    path("user/signin", views.signin),
    path("user/kakao", views.kakao),
    path("user/check/email", views.verify_email),
    path("refresh", views.refresh),
    path("airport/<str:name>", views.AirportAPIView.as_view()),
    path("dog/search/", views.DogDstDateAPIView.as_view()),
    path("dog/desc/", views.DogSingleAPIView.as_view()),
    path("dog/deadline/", views.DogDeadlineAPIView.as_view()),
    path("dog/add/", views.DogAddAPIView.as_view()),
    path("dog/modify/<str:_id>/", views.DogModifyAPIView.as_view()),
    path("upload/test", views.upload_test),
    path("review/user", views.UserReviewAPIView.as_view()),
]
