# myapp/forms.py
from django import forms
from .models import Book

from .models import NewBookRequest


# myapp/forms.py
class NewBookRequestForm(forms.ModelForm):
    class Meta:
        model = NewBookRequest
        fields = ['title', 'author', 'description']



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date', 'loan_period_days']
