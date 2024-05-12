

# Image Swiping App

This Django application provides a platform for users to accept or reject images by swiping right or left, respectively. It also includes a history section that displays the records of which user has accepted or rejected a particular image at a specific timestamp.

## Features

- User authentication with OTP verification
- User profile management (name, email, and phone number)
- Swipe functionality to accept or reject images
- History section to track accepted/rejected images with timestamps

## Database Models

The application utilizes the following database models:

1. **ImageHistory**: This model stores the history of accepted or rejected images, including the image path, action (accept or reject), user, and timestamp.

2. **User**: This is the built-in Django User model, which stores user information such as username, email, and password.

3. **Profile**: This model extends the User model and includes additional fields like phone number, OTP, and verification status.

## App Structure

The application consists of two main apps:

1. **users**: This app handles user authentication, registration, and profile management.

2. **swipepic**: This app provides the functionality for swiping images and displaying the history of accepted/rejected images.

## URL Patterns

The following URL patterns are defined in the application:

- `users:login='/'`: The login page for existing users.
- `users:register='register/'`: The registration page for new users.
- `users:otp='otp/'`: The page for OTP verification during registration or login.
- `swipepic:dashboard='swipepic/dashboard/'`: The dashboard page where users can swipe through images.
- `swipepic:history='/swipepic/history'`: The history page that displays the records of accepted/rejected images.

## Getting Started

To get a local copy up and running, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/image-swiping-app.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the database settings in the `settings.py` file.

4. Run the database migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application in your web browser at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Demo

Here's a demo video showing how the project works:

![Project Demo](https://drive.google.com/file/d/1S57_Kp-jUDNSL13wyfXBoXeIknJOeslb/view?usp=sharing)

