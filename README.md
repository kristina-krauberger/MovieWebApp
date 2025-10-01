# 🎬 Movie Web App

A simple Flask-based movie management web application that allows users
to: - Add users - Add movies to a user's favorite list (via OMDb API) -
Update movie titles - Delete favorite movies - Display custom error
pages (404 & 500)

## 📁 Project Structure

    MovieWebApp/
    │
    ├── app.py                 # Main Flask application
    ├── data_manager.py        # Logic for managing users and movies
    ├── helpers.py             # Helper functions (e.g., validation)
    ├── models/                # SQLAlchemy models for Users, Movies, and FavoriteMovies
    │   └── models.py
    ├── templates/             # HTML templates (Jinja2)
    │   ├── base.html
    │   ├── index.html
    │   ├── movies.html
    │   ├── 404.html
    │   └── 500.html
    ├── data/
    │   └── movies.db          # SQLite database
    ├── .env                   # Environment variables (e.g. API key, secret)
    ├── .gitignore
    ├── requirements.txt       # List of dependencies
    └── README.md              # Project documentation

## 🚀 How to Run the Project

1.  **Create virtual environment** (optional but recommended):

``` bash
python -m venv venv
source venv/bin/activate  # or 'venv\Scripts\activate' on Windows
```

2.  **Install dependencies**:

``` bash
pip install -r requirements.txt
```

3.  **Set up environment variables**\
    Create a `.env` file with the following content:

``` bash
KEY_FLASH=your_flask_secret_key
KEY=your_omdb_api_key
```

4.  **Run the app**:

``` bash
python app.py
```

Then visit: `http://localhost:5001/`

------------------------------------------------------------------------

## 📦 Dependencies

-   Flask
-   SQLAlchemy
-   requests
-   python-dotenv

------------------------------------------------------------------------

## 🧠 Notes

-   All movie data is fetched from the OMDb API.
-   Uses SQLite for easy local development.

------------------------------------------------------------------------

## ✨ Author

Kristina Krauberger 
