from django.urls import path
from endpoints.movie import MovieList, MovieDetail, MovieGenreList, GetMovieByCode

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<str:title>/', MovieDetail.as_view(), name='movie-detail'),
    path('movies/genre/<str:genre>/', MovieGenreList.as_view(), name='movie-genre-list'),
    path('movies/code/<str:code>/', GetMovieByCode.as_view(), name='movie-code'),
]
