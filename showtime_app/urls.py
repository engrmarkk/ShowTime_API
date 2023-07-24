from django.urls import path
from endpoints.movie import MovieList, MovieDetail

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<str:title>/', MovieDetail.as_view(), name='movie-detail'),
]
