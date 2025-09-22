# django-blog-app/django-blog-app/README.md

# Django Blog Application

This is a simple blog application built with Django, utilizing SQLite3 as the backend database. The application supports CRUD (Create, Read, Update, Delete) operations for blog posts.

## Features

- Create new blog posts
- View a list of all blog posts
- View details of a single blog post
- Update existing blog posts
- Delete blog posts

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```
   cd django-blog-app
   ```

3. Create a virtual environment:

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:

   ```
   pip install django
   ```

6. Run migrations to set up the database:

   ```
   python manage.py migrate
   ```

7. Create a superuser to access the admin panel:

   ```
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```
   python manage.py runserver
   ```

9. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Navigate to the admin panel at `http://127.0.0.1:8000/admin/` to manage blog posts.
- Use the application to create, view, update, and delete blog posts.

## License

This project is licensed under the MIT License.
