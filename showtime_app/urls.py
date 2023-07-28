from django.urls import path
from .endpoints.movie import MovieList, MovieDetail, MovieGenreList, GetMovieByCode
from .endpoints.tickets import GetTicketPriceForAMovie, CreateTicket
from .endpoints.user import ListAllUsers

urlpatterns = [
    # Movies
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<str:title>/', MovieDetail.as_view(), name='movie-detail'),
    path('movies/genre/<str:genre>/', MovieGenreList.as_view(), name='movie-genre-list'),
    path('movies/code/<str:code>/', GetMovieByCode.as_view(), name='movie-code'),

    # Users
    path('all_users/', ListAllUsers.as_view(), name='user-list'),

    # Tickets
    path('tickets/<str:movie_code>/', GetTicketPriceForAMovie.as_view(), name='ticket-price'),
    path('tickets/create/', CreateTicket.as_view(), name='create-ticket'),
]
