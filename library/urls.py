from django.contrib import admin
from django.urls import path, include
from myapp.views import signup, home
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # Book details page
    path('book/<int:book_id>/take_out/', views.take_out_book, name='take_out_book'),  # Take out book
    path('user/<str:username>/', views.user_profile, name='user_profile'),  # User profile page
    path('request-new-book/', views.request_new_book, name='request_book_page'),  # Request new book
    path('my-requests/', views.user_requests, name='user_requests'),  # User requests page
    path('book/return/<int:book_id>/', views.return_book, name='return_book'),  # New URL for returning a book
]
