
# Library Management System

## Overview

The **Library Management System** is a web application built using Django, allowing users to manage books, request books, view book details, and track book loans. The system allows users to sign up, log in, and interact with books, while an administrator can manage book requests and approvals.

## Live Application:
The application is live and can be accessed at:
https://librarymanagement-zq9i.onrender.com/

## Credentials for Super User (Librarian)
Username: sreeg
Password: @Sreegandh381

## Time Spent & Thoughts

I spent approximately 5-6 hours on this project from start to finish. 
I implemented all the requested features along with the bonus features in a minimalistic way, focusing on simplicity rather than advanced design. The goal was to make the app easy to use while demonstrating my ability to develop modular code. As the assessment/task primarily focused on evaluating clean code and coding style, I did not spend much time on the CSS or UI design aspects. For efficiency, I used tools like GitHub Copilot and ChatGPT in an assistive manner to help with certain code implementations, ensuring best practices and optimizing my workflow. However, if I had more time, I would have definitely focused on improving the UI and adding more advanced features like those mentioned in the Future Improvements section below.

## Assumptions

I made a few assumptions while developing this project to both simplify the implementation and focus on the core features:
- The student can borrow a book without any restrictions or permission from the admin.
- There is no late fee or penalty for overdue books.
- Only logged-in users can view the list of books and request new books.

## Project Structure

The project is organized into two main directories:

- **library/**: Contains the core configuration files, settings, URLs, and static assets.
- **myapp/**: Contains the business logic, models, views, and templates for the application.

### Project Structure Diagram

```
library/
    ├── settings.py        # Django settings for the project
    ├── urls.py            # URL configuration for the project
    ├── wsgi.py            # WSGI configuration for deployment
    └── asgi.py            # ASGI configuration for deployment
myapp/
    ├── migrations/        # Django migrations for the app
    ├── models.py          # Models for database schema
    ├── views.py           # Views for rendering templates
    ├── forms.py           # Forms for handling user input
    ├── urls.py            # URL configuration for the app
    ├── templates/         # Templates for rendering HTML pages
    └── apps.py            # App configuration for Django
    └── admin.py           # Admin configuration for managing models
```

---

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sreegandh804/LibraryManagement.git
   cd LibraryManagement
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations to set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (This would be the library admin):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the app.


### **2. Key Features**

- **User Authentication**: Users can sign up, log in, and view their profile. 
- **Admin Panel**: Admins can manage books, book requests, and user data.
- **Book Management**: Users can view available books, request new books, check out books and return them.
- **Book Requests**: Users can request books that are not currently available, and the admin can approve or decline those requests.
- **Overdue Book Tracking**: Admins can track overdue books by monitoring the due date and sending reminders.


## Future Improvements

In an ideal scenario with more time, I would have implemented the following:

1. **Advanced Search Filters**:
   - Allow users to search by genres, ratings, or authors. This would improve the search functionality and make it more intuitive.

2. **Book Categories and Tags**:
   - Implement a system where books can be categorized (e.g., fiction, non-fiction, science, etc.) and tagged with keywords for more detailed searches.

3. **Email Notifications**:
   - Set up automatic email notifications for overdue books, book request approvals, or new book availability.

4. **Late Fee System**:
   - Implement a late fee system where users are charged for overdue books based on the number of days they are late.

5. **Custom Library Admin Panel**:
   - Create a custom admin panel with more detailed analytics, user management, and book tracking features.

6. **Responsiveness and Beautification**:
   - Improve the CSS and front-end design to make the app more visually appealing and responsive across different devices.

7. **Testing**:
   - Write unit tests and integration tests to ensure the functionality of the application, especially the book borrowing and request systems.

8. **User Roles**:
   - Implement different user roles, such as `Admin`, `Librarian`, and `User`, each with different permissions for managing books and requests.

