Flask-Code-Challenge - Pizza Restaurants

Welcome to the Flask-Code-Challenge - Pizza Restaurants application. This Flask web application allows you to manage pizza restaurants, their menus, and customer orders. Below, you'll find detailed instructions on getting started and using the application.
Table of Contents

    Features
    Getting Started
        Prerequisites
        Installation
    Usage
    Project Structure
    Contributing
    License

Features

    Create, edit, and delete pizza restaurants.
    Define pizza menus for each restaurant.
    Customers can view restaurant menus and place orders.
    Restaurant owners can manage orders and mark them as complete.
    Database integration using Flask-SQLAlchemy.
    Flask-Migrate for handling database migrations.

Getting Started

These instructions will help you set up the project on your local machine.
Prerequisites

Make sure you have the following installed:

    Python 3.8 or higher
    Virtual environment (recommended)
    Git (optional)

Installation

    Clone the repository to your local machine:

git clone https://github.com/mbitutu/Flask-Code-Challenge---Pizza-Restaurants
cd Flask-Code-Challenge-Pizza-Restaurants

Create a virtual environment (recommended):

bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install project dependencies:

pip install -r requirements.txt

Initialize the database and apply migrations:

    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

Usage

Follow these steps to run and use the application:

    To run the application, use the following command:

    bash

    flask run

    Access the application in your web browser at http://localhost:5000.

    Explore the application's features:
        Create and manage pizza restaurants.
        Define menus for each restaurant.
        Place orders as a customer.
        Manage orders as a restaurant owner.

Project Structure

Here's a brief overview of the project structure:

    app.py: The main application script.
    models.py: Contains SQLAlchemy database models.
    migrations/: Database migration scripts generated by Flask-Migrate.
    requirements.txt: List of Python packages required for the project.
    .env: Environment variables (create your own for sensitive data).

Contributing

Contributions are welcome. If you'd like to contribute, please follow these guidelines:

    Fork the repository.
    Create a new branch for your feature or bug fix.
    Make your changes and commit them.
    Test thoroughly.
    Create a pull request.

License

This project is licensed under the Bitutu License. 