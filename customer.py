# customer.py

from typing import List, Optional
from review import Review  # Import the Review class
from restaurant import Restaurant  # Import the Restaurant class

class Customer:
    all_customers: List['Customer'] = []

    def __init__(self, given_name: str, family_name: str):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set(review.get_restaurant() for review in Review.all() if review.get_customer() == self))

    def add_review(self, restaurant: 'Restaurant', rating: int):
        from review import Review  # Import inside the method to avoid circular imports
        Review(self, restaurant, rating)

    def num_reviews(self):
        return len([review for review in Review.all() if review.get_customer() == self])

    @classmethod
    def find_by_name(cls, name: str):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name: str):
        return [customer for customer in cls.all_customers if customer.get_given_name() == name]
