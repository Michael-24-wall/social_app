# Social App

This is a social application built using Django, inspired by Instagram. The application allows users to create accounts, post images, follow other users, and interact with posts through likes and comments.

## Features

- User registration and authentication
- Profile management
- Image uploads
- Follow/unfollow functionality
- Like and comment on posts
- Responsive design

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd social_app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage users and posts.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.