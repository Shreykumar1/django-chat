# Django Chat Application

This is a real-time chat application built using Django, Django Channels, WebSocket, and Bootstrap. Users can chat in private rooms with real-time message updates.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-chat-app.git
cd django-chat-app
```

### 2. Install Dependencies
Make sure you have Python installed (preferably Python 3.8 or higher). Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Remove Migrations and Data (Optional)
If you want to reset the database and migrations:
```bash
# Delete migration files
rm -rf your_app_name/migrations/*

# Delete the database (this will remove all data)
rm db.sqlite3
```

### 4. Create and Apply Migrations
Generate and apply fresh migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/

### 6. Using the Application
- Access chat rooms at: http://127.0.0.1:8000/chat/room_name/ (replace room_name with desired chat room name)
- Use the Logout button in the sidebar to sign out

## Dependencies
- Django >= 3.0
- Channels >= 3.0
- Redis (for Channels Layer)

## Additional Notes
- Ensure Redis is installed and running for WebSocket communication
- The application can be customized to add features like multiple rooms, private messages, etc.