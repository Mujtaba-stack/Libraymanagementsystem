from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from .models import Member, Category, Book, Author
from .serializers import (
    MemberSerializer, CategorySerializer, BookSerializer, 
    AuthorSerializer
)

@api_view(['GET', 'POST'])
def member_list_create(request):
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def book_list_create(request):
    try:
        if request.method == 'GET':
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Exception: ", e)
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def book_detail(request, id):
    book = get_object_or_404(Book, book_id=id)
    member_id = request.data.get("member_id")
    current_operation = request.data.get("current_operation", "").lower()
    if not member_id:
        return Response({"error": "Member ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    member = get_object_or_404(Member, id=member_id)
    if current_operation == "borrow":
        if book.book_status == "Available":
            book.book_status = "Borrowed"
            member.books.add(book)  
            book.save()
            member.save()
        else:
            return Response({"error": "Book is not available for borrowing."}, status=status.HTTP_400_BAD_REQUEST)
    elif current_operation == "reserve":
        if book.book_status == "Available":
            book.book_status = "Reserved"
            member.books.add(book) 
            book.save()
            member.save()
        else:
            return Response({"error": "Book is not available for reservation."}, status=status.HTTP_400_BAD_REQUEST)
    elif current_operation == "return":
        if book in member.books.all():
            member.books.remove(book)  
            if not any(member.books.filter(id=book.book_id).exists() for member in Member.objects.all()):
                book.book_status = "Available"
            book.save()
            member.save()
        else:
            return Response({"error": "This book was not borrowed by the member."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = BookSerializer(book)
    return Response({"message": f"Book status updated to {book.book_status}", "updated_data": serializer.data})


@api_view(['GET', 'POST'])
def author_list_create(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def search_lms(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(Q(book_title__icontains=query))
    members = Member.objects.filter(Q(member_full_name__icontains=query) |Q(member_Email__icontains=query) |Q(member_department__icontains=query) |Q(member_city__icontains=query) |Q(member_age__icontains=query))
    categories = Category.objects.filter(Q(category_name__icontains=query))
    authors = Author.objects.filter(Q(author_name__icontains=query))
    response = {
        "books": BookSerializer(books, many=True).data,
        "members": MemberSerializer(members, many=True).data,
        "categories": CategorySerializer(categories, many=True).data,
        "authors": AuthorSerializer(authors, many=True).data,            
    }
    

    return Response(response,status=status.HTTP_200_OK)

