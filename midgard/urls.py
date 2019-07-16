from django.urls import path
from midgard import views

urlpatterns = [
    path('vols/', views.VolList.as_view()),
    path('vols/<int:pk>/', views.VolDetail.as_view()),
    path('vol/', views.VolsView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('user/', views.UserInfo.as_view()),
    path('', views.IndexView.as_view(), name='home'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.successView, name='thanks'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
]