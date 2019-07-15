from django.urls import path
from midgard import views

urlpatterns = [
    path('vols/', views.VolList.as_view()),
    path('vols/<int:pk>/', views.VolDetail.as_view()),
    path('vol/', views.VolsView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('user/', views.UserInfo.as_view()),
    path('', views.IndexView.as_view()),
]