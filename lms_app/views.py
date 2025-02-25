from django.shortcuts import render
from rest_framework import generics
from .models import Member, Category, Book, Author, Reservation, Barrow
from .serializers import MemberSerializer, CategorySerializer, BookSerializer, AuthorSerializer, ReservationSerializer, \
    BarrowSerializer


# Create your views here.

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = ReservationSerializer


class BarrowListCreateView(generics.ListCreateAPIView):
    queryset = Barrow.objects.all()
    serializer_class = BarrowSerializer


class BarrowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barrow.objects.all()
    serializer_class = BarrowSerializer
