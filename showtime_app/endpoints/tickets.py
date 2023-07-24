from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from showtime_app.models import Movie, Venue, Ticket, Review, Order, User
from showtime_app.serializers import TicketSerializer


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class GetTicketPriceForAMovie(APIView):
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, movie_code):
        movie = get_object_or_404(Movie, movie_code=movie_code)
        tickets = Ticket.objects.filter(movie=movie)
        serializer = self.serializer_class(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateTicket(generics.CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminUser)
