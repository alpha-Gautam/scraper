# Scraper Django Project Documentation

## Overview

This is a Django-based web scraping project named **scraper**. It provides a web interface for scraping data, managing tasks, and displaying results. The project is organized using Django's best practices and includes support for static files, templates, and background task processing (Celery).

## Features

- Web scraping functionality
- Task management (Celery integration)
- User interface with templates and static files
- Modular Django app structure

## Project Structure

```
db.sqlite3                # SQLite database
manage.py                 # Django management script
requirements.txt          # Python dependencies
home/                     # Main Django app
    admin.py              # Admin configuration
    apps.py               # App configuration
    models.py             # Database models
    script.py             # Scraping logic
    tasks.py              # Celery tasks
    tests.py              # Unit tests
    urls.py               # App URLs
    views.py              # View functions
    migrations/           # Database migrations
    static/               # Static files (CSS, JS)
    templates/            # HTML templates
scraper/                  # Project settings
    celery.py             # Celery configuration
    settings.py           # Django settings
    urls.py               # Project URLs
    wsgi.py, asgi.py      # Deployment entry points
```

## Setup Instructions

1. **Clone the repository**

   ```powershell
   git clone <repo-url>
   cd scraper
   ```

2. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Apply migrations**

   ```powershell
   python manage.py migrate
   ```

4. **Run the development server**

   ```powershell
   python manage.py runserver
   ```

5. **(Optional) Start Celery worker**
   ```powershell
   celery -A scraper worker --loglevel=info
   ```

## Usage

- Access the web interface at `http://127.0.0.1:8000/`
- Use the provided forms/pages to start scraping tasks and view results.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first.

## License

Specify your license here (e.g., MIT, GPL).

## Contact

For questions or support, contact the project owner.
