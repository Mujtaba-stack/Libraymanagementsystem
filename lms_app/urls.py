from django.urls import path
from .views import (
    member_list_create, member_detail,
    category_list_create, category_detail,
    book_list_create, book_detail,
    author_list_create, author_detail,
    barrow_list_create, barrow_detail,
    reservation_list_create, reservation_detail,search_lms,
)

urlpatterns = [
    path('member/', member_list_create, name='member-list-create'),
    path('member/<int:id>/', member_detail, name='member-detail'),

    path('category/', category_list_create, name='category-list-create'),
    path('category/<int:id>/', category_detail, name='category-detail'),

    path('book/', book_list_create, name='book-list-create'),
    path('book/<int:id>/', book_detail, name='book-detail'),

    path('author/', author_list_create, name='author-list-create'),
    path('author/<int:id>/', author_detail, name='author-detail'),

    path('barrow/', barrow_list_create, name='barrow-list-create'),
    path('barrow/<int:id>/', barrow_detail, name='barrow-detail'),

    path('reservation/', reservation_list_create, name='reservation-list-create'),
    path('reservation/<int:id>/', reservation_detail, name='reservation-detail'),

    path('search/', search_lms, name='search_lms_create'),
]
