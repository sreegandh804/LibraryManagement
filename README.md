# **Library Management System**

## **Overview**
The **Library Management System** is a web application built using Django that allows users to manage books, request books, view details, and track book loans. It includes both user and admin features, such as account management, book borrowing, and request approval.

## **Live Application**
You can access the live application here:  
[Library Management System](https://librarymanagement-zq9i.onrender.com/)

## **Super User Credentials**
For admin (librarian) access:  
- **Username**: sreeg  
- **Password**: @Sreegandh381

## **Time Spent & Development Approach**
- **Time Spent**: ~5-6 hours  
- Focused on clean, modular code, prioritizing functionality over advanced design.  
- Used tools like GitHub Copilot and ChatGPT for assistance.  
- Future improvements would focus on UI enhancements and adding advanced features.

## **Assumptions**
- Users can borrow books freely without admin approval.
- No penalties for overdue books.
- Only logged-in users can view and request books.

---

## **Project Structure**

### **Directory Overview**:

```
library/
    ├── settings.py        # Project settings
    ├── urls.py            # Project URL configurations
    ├── wsgi.py            # WSGI configuration for deployment
    └── asgi.py            # ASGI configuration for deployment
myapp/
    ├── migrations/        # Django migrations for the app
    ├── models.py          # Database models
    ├── views.py           # Views for rendering templates
    ├── forms.py           # User input forms
    ├── urls.py            # App-specific URL configurations
    ├── templates/         # HTML templates
    └── apps.py            # App configuration
    └── admin.py           # Admin configurations for models
```

---

## **Installation & Setup**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sreegandh804/LibraryManagement.git
   cd LibraryManagement
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

---

## **Key Features**
- **User Authentication**: Users can sign up, log in, and view their profiles.
- **Admin Panel**: Admins can manage books, book requests, and user information.
- **Book Management**: Users can view, request, check out, and return books.
- **Book Requests**: Users can request unavailable books, and admins can approve/decline them.
- **Overdue Tracking**: Admins can track overdue books and send reminders.

---

## **Future Improvements**
In a future version, the following features would be added:

1. **Advanced Search Filters**: Search by genres, ratings, or authors.
2. **Book Categories and Tags**: Categorize and tag books for improved searches.
3. **Email Notifications**: Automatic notifications for overdue books and new book availability.
4. **Late Fee System**: Implement a fee system for overdue books.
5. **Custom Admin Panel**: A custom admin panel with analytics and user management.
6. **Responsiveness & Beautification**: Improve CSS and UI for better responsiveness.
7. **Testing**: Add unit and integration tests for critical features.
8. **User Roles**: Implement different user roles (Admin, Librarian, User) with specific permissions.
