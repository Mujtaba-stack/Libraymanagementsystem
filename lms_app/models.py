from django.db import models
from datetime import timedelta, date

# Create your models here.

class Member(models.Model):
    member_full_name = models.CharField(max_length=220)
    member_Email = models.CharField(max_length=220)
    member_department = models.CharField(max_length=220)
    member_city = models.CharField(max_length=220)
    member_age = models.IntegerField()
    membership_type = models.CharField(max_length=100, choices=[('Free', 'Free'), ('Premium', 'Premium')])
    expeiry_date = models.DateField()

    def __str__(self):
        return self.member_full_name


class Category(models.Model):
    Category_name = models.CharField(max_length=220)

    def __str__(self):
        return self.Category_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=220)
    isbn = models.CharField(max_length=20, default="000-0000000000")  
    description = models.TextField(default="No description available.")
    total_copies = models.IntegerField(null=True, blank=True)  
    available_copies = models.IntegerField(default=1)
    def save(self):
        if self.available_copies > self.total_copies:
            self.available_copies = self.total_copies
        super().save()    

    def __str__(self):
        return self.book_title


class Author(models.Model):
    author_name = models.CharField(max_length=220)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='authors')  

    def __str__(self):
        return self.author_name


class Barrow(models.Model):
    barrow_date = models.DateField(default=date.today() + timedelta(days=14))  
    returned_date = models.BooleanField(default=False)  
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Barrowed on {self.barrow_date}, Returned: {self.returned_date}"

 
class Reservation(models.Model):
    Member = models.ForeignKey(Member, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reversed_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('complete', 'Complete')])

    def __str__(self):
        return f"{self.Member.member_FullName} reserved {self.Book.book_title} - {self.status}"


