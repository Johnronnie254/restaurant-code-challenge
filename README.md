Customer and Review Management Application
This Python application provides a simple framework for managing customer information and their reviews for restaurants. It includes two main classes: Customer and Review, each contributing to the overall functionality of the application.

Table of Contents
Installation
Usage
Classes
Customer
Review
Examples
Contributing
License
Installation
To use this application, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your_username/your_repository.git
Change into the project directory:

bash
Copy code
cd your_repository
Run the application:

bash
Copy code
python main.py
Usage
The application allows you to create and manage customer records and their corresponding restaurant reviews. It provides methods to retrieve information such as the full name of a customer, the restaurants they have reviewed, and the average rating for a specific restaurant.

Classes
Customer
The Customer class represents a customer and includes the following attributes and methods:

Attributes:

given_name: First name of the customer.
family_name: Last name of the customer.
all_customers: Class variable to store all instances of customers.
Methods:

__init__(self, given_name, family_name): Initializes a new customer instance.
given_name(self): Returns the given name of the customer.
family_name(self): Returns the family name of the customer.
full_name(self): Returns the full name of the customer.
all(cls): Returns a list of all customer instances.
restaurants(self): Returns a list of unique restaurants reviewed by the customer.
add_review(self, restaurant, rating): Adds a new review for a restaurant.
num_reviews(self): Returns the number of reviews submitted by the customer.
find_by_name(cls, name): Finds a customer by their full name.
find_all_by_given_name(cls, name): Finds all customers with a given first name.
Review
The Review class represents a customer review for a restaurant and includes the following attributes and methods:

Attributes:

customer: The customer who submitted the review.
restaurant: The restaurant being reviewed.
rating: The rating given by the customer.
all_reviews: Class variable to store all instances of reviews.
Methods:

__init__(self, customer, restaurant, rating): Initializes a new review instance.
rating(self): Returns the rating given in the review.
customer(self): Returns the customer who submitted the review.
restaurant(self): Returns the restaurant being reviewed.
all(cls): Returns a list of all review instances.
Examples
Here are some examples demonstrating how to use the application:

python
Copy code
# Create a new customer
customer1 = Customer("John", "Doe")

# Add a review for a restaurant
customer1.add_review("Example Restaurant", 4)

# Retrieve all customers
all_customers = Customer.all()

# Find a customer by full name
found_customer = Customer.find_by_name("John Doe")

# Find all customers with a given first name
all_customers_with_name = Customer.find_all_by_given_name("John")
Contributing
Feel free to contribute to the development of this application by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

License
This project is licensed under the MIT License.

