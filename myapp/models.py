from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


# Create your models here.

# myapp/models.py
class NewBookRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DECLINED', 'Declined'),
        ('ALREADY_PRESENT', 'Already Present'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.title} requested by {self.user.username} - {self.get_status_display()}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()
    taken_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    taken_out_date = models.DateTimeField(null=True, blank=True)  # Store when the book is checked out
    due_date = models.DateTimeField(null=True, blank=True)  # Store the due date of the book
    loan_period_days = models.IntegerField(default=14)  # Number of days the book can be loaned out

    def __str__(self):
        return self.title

    def calculate_due_date(self):
        """Calculate the due date based on the loan period days."""
        if self.taken_out_date:
            return self.taken_out_date + timedelta(days=self.loan_period_days)
        return None
