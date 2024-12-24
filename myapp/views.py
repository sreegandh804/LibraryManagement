from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import BookForm
from django.utils import timezone
from .forms import NewBookRequestForm
from .models import NewBookRequest
from .models import Book
# myapp/views.py
from django.db.models import Q


def home(request):
    search_query = request.GET.get('q', '')
    search_field = request.GET.get('field', 'title')  # Default search field
    availability_filter = request.GET.get('availability', '')

    # Books query
    books = Book.objects.all()

    if search_query:
        if search_field == 'title':
            books = books.filter(title__icontains=search_query)
        elif search_field == 'author':
            books = books.filter(author__icontains=search_query)
        elif search_field == 'registered_user':
            books = books.filter(taken_by__username__icontains=search_query)

    if availability_filter == 'available':
        books = books.filter(taken_by__isnull=True)
    elif availability_filter == 'taken':
        books = books.filter(taken_by__isnull=False)

    # Users query
    users = User.objects.all()
    if search_field == 'registered_user' and search_query:
        users = users.filter(username__icontains=search_query)

    return render(request, 'home.html',
                  {'books': books, 'users': users, 'search_query': search_query, 'search_field': search_field,
                   'availability_filter': availability_filter})


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})


@login_required
def take_out_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    # Check if the book is already taken
    if book.taken_by is not None:
        return redirect('book_detail', book_id=book.id)  # Redirect back to book detail if already taken

    # If the book is available, mark it as taken by the current user
    book.taken_by = request.user
    book.taken_out_date = timezone.now()

    # Calculate and set the due date based on the loan period
    book.due_date = book.calculate_due_date()

    book.save()

    return redirect('book_detail', book_id=book.id)


@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Check if the current user is the one who took out the book
    if book.taken_by == request.user:
        book.taken_by = None
        book.due_date = None  # Clear the due date when the book is returned
        book.save()
        return redirect('home')  # Redirect back to home page after returning the book
    else:
        # If the user is not the one who borrowed the book, prevent the return
        return redirect('book_detail', book_id=book.id)



@login_required
def request_new_book(request):
    if request.method == 'POST':
        form = NewBookRequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return render(request, 'request_success.html', {'title': new_request.title})
    else:
        form = NewBookRequestForm()

    return render(request, 'request_new_book.html', {'form': form})


@login_required
def user_requests(request):
    requests = NewBookRequest.objects.filter(user=request.user).order_by('-request_date')
    return render(request, 'user_requests.html', {'requests': requests})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    books_taken_out = Book.objects.filter(taken_by=user)  # Books taken out by this user
    return render(request, 'user_profile.html', {'user': user, 'books_taken_out': books_taken_out})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
