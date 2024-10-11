# Personal Blogging Platform API

This project is a simple RESTful API for a personal blogging platform, built using the Flask framework and PostgreSQL as the database. The API allows users to perform basic CRUD (Create, Read, Update, Delete) operations on blog posts.

## Goals

The goals of this project are to help you:
- Understand what RESTful APIs are, including best practices and conventions.
- Learn how to create a RESTful API.
- Learn about common HTTP methods like GET, POST, PUT, PATCH, and DELETE.
- Understand status codes and error handling in APIs.
- Learn how to perform CRUD operations using an API.
- Learn how to work with databases.

## Requirements

Before running the application, ensure you have the following installed on your machine:

- **PostgreSQL**: Make sure PostgreSQL is installed and running. You can download it from [PostgreSQL's official site](https://www.postgresql.org/download/).

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>

### 2. Create and Configure the `database.ini` File
- In the root of your project directory, create a file named `database.ini`.
- Fill in the database credentials as follows:
    ```ini
    [postgresql]
    host=localhost
    database=your_database_name
    user=your_username
    password=your_password
    port=5432
    ```
    Replace `your_database_name`, `your_username`, and `your_password` with your actual PostgreSQL database details.

### 3. Run the flask application
```
flask --app main run --reload 
```


