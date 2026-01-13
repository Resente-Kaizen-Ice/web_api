# Recipe Book

## Description
**Recipe Book** is a FastAPI application built with Python and MySQL that allows users to create, share, and explore recipes. Users can save their favorite recipes from others to their personal collection.  

With Recipe Book, you can:  
- Create your own recipes with detailed ingredients and quantities.  
- Browse recipes created by other users.  
- Save recipes to your favorites for easy access.  

---

## Database Structure

### Tables

**Account**  
| Column   | Type       |
|----------|------------|
| id       | INT / UUID |
| email    | VARCHAR    |
| password | VARCHAR    |

**User**  
| Column      | Type       |
|-------------|------------|
| id          | INT / UUID |
| account_id  | INT / UUID |
| fname       | VARCHAR    |
| mname       | VARCHAR    |
| lname       | VARCHAR    |
| nickname    | VARCHAR    |

**Recipe**  
| Column      | Type       |
|-------------|------------|
| id          | INT / UUID |
| name        | VARCHAR    |
| created_by  | INT / UUID (user_id) |
| description | TEXT       |

**BOM (Bill of Materials / Ingredients)**  
| Column      | Type       |
|-------------|------------|
| id          | INT / UUID |
| recipe_id   | INT / UUID |
| ingredients | VARCHAR    |
| quantity    | FLOAT / INT|
| unit        | VARCHAR    |

**Favorites**  
| Column      | Type       |
|-------------|------------|
| account_id  | INT / UUID |
| recipe_id   | INT / UUID |

---

## User Endpoints

- **GET /users** – Get all users (admin only)  
- **POST /register** – Create a new account  
- **POST /login** – Login to your account  
- **PUT /update-details** – Update personal information  

---

## Recipe Endpoints

- **GET /recipes** – Browse all recipes  
- **POST /recipes** – Add a new recipe  
- **DELETE /recipes/{id}** – Delete a recipe (only the creator can delete)  

---

## Features

- **Persistent Accounts** – Your work is saved and secure.  
- **Save Recipes** – Save your own recipes or favorites from other users.  
- **Browse Recipes** – Explore a variety of recipes created by other users.  

---

## Tech Stack

- **Backend:** Python, FastAPI  
- **Database:** MySQL  
- **ORM / Connector:** (e.g., SQLAlchemy or MySQL Connector/Python)  

---

## Installation

1. Clone the repository:  
   ```bash git clone https://github.com/your-username/recipe-book.git cd recipe-book```
2. Create a virtual environment and install dependencies:
   ```python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt```
3. Run the FastAPI server:
   ```uvicorn main:app --reload```
4. Access the API docs at:
   http://127.0.0.1:8000/docs
