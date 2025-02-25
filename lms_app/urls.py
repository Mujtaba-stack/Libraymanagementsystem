from django.urls import path
from .views import MemberListCreateView, MemberDetailView, CategoryListCreateView, CategoryDetailView, \
    BookListCreateView, BookDetailView, AuthorListCreateView, AuthorDetailView, ReservationDetailView, \
    ReservationListCreateView, BarrowListCreateView, BarrowDetailView

urlpatterns = [
    path('member/', MemberListCreateView.as_view(), name='user-list-create'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='user-list-details'),
    path('category/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-list-details'),
    path('books/', BookListCreateView.as_view(), name='book-list-Create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-list-details'),
    path('authors/', AuthorListCreateView.as_view(), name='Author-list-Create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='Author-list-details'),
    path('reservation/', ReservationListCreateView.as_view(), name='Resveration-list-Create'),
    path('reservation/<int:pk>/', ReservationDetailView.as_view(), name='Resveration-list-details'),
    path('barrow/', BarrowListCreateView.as_view(), name='Barrow-list-Create'),
    path('barrow/<int:pk>/', BarrowDetailView.as_view(), name='Barrow-list-details'),
]
