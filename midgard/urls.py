from django.urls import path
from midgard import views

urlpatterns = [
    path('vols/', views.vol_list),
    path('vols/<int:pk>/', views.vol_detail),
]