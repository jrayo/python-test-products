## Statement

You have a JSON file containing information about various products, including their names, prices, ratings and update date. The goal of this exercise is to read the JSON file, sort the products by price, and calculate the average rating of the top 10 most expensive products without considering the ones updated more than 3 months ago.

## Prerequisites
Before you begin, ensure you have met the following requirements:

Docker: The application is containerized with Docker, so you will need Docker installed on your system to run it.

Docker Compose: This project uses Docker Compose to manage multi-container Docker applications. Ensure you have Docker Compose installed. Usually, it comes with the Docker Desktop installation for Windows and Mac. 

## Running the Application

1. **Clone the Repository**:

First, clone the repository to your local machine using:

`git clone https://github.com/jrayo/python-test-products.git`

2. **Navigate to the Project Directory**:

Change to the project directory:

`cd python-test-products`

3. **Start the Application**:

Use Docker Compose to build and start the application:

`docker-compose up -d`

This command will download the necessary Docker images, build the application, and start it in detached mode.

4. **Accessing the Application**:

`http://localhost:8000`

5. **Stopping the Application**:

To stop the application, use:

`docker-compose stop`

## Running Tests

1. **Ensure the Application is Running**:

Make sure the application containers are up and running. If not, start them using:

`docker-compose up -d`

2. **Execute the Tests**:

Run the tests by executing the following command:

`docker-compose exec python manage.py test`