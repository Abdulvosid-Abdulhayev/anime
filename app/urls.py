from django.urls import path
from .views import Home, Caregory, Anime_detail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("category/", Caregory.as_view(), name='category'),
    
    path("category/<slug:slug>", Caregory.as_view(), name='category'),
    path('detail/<str:selected_category>/<slug:slug>/', Anime_detail.as_view(), name='detail')


]
