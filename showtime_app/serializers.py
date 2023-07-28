from rest_framework import serializers
from showtime_app.models import Movie, Venue, Ticket, Review, Order, CustomUser
from rest_framework.exceptions import ValidationError


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'firstname', 'lastname']


class CustomRegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=255, required=True)
    lastname = serializers.CharField(max_length=255, required=True)
    username = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(max_length=255)
    phone = serializers.CharField(max_length=255, required=True)
    password1 = serializers.CharField(max_length=255, write_only=True)
    password2 = serializers.CharField(max_length=255, write_only=True)

    def validate_email(self, value):
        qs = CustomUser.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_username(self, value):
        # this is for case insensitive username
        qs = CustomUser.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_password1(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords must match")
        return data

    def get_cleaned_data(self, data):
        return {
            'first_name': data.get('first_name', ''),
            'last_name': data.get('last_name', ''),
            'username': data.get('username', ''),
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'password': data.get('password1', ''),
        }

    def save(self, request):
        user = CustomUser.objects.create(
            username=self.validated_data['username'].lower(),
            email=self.validated_data['email'].lower(),
            firstname=self.validated_data['firstname'].lower(),
            lastname=self.validated_data['lastname'].lower(),
            phone=self.validated_data['phone'],
        )
        user.set_password(self.validated_data['password1'])
        user.save()
        return user


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
