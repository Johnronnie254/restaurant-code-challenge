from typing import List, Optional
from customer import Customer  # Import the Customer class
from restaurant import Restaurant  # Import the Restaurant class

class Review:
    all_reviews: List['Review'] = []

    def __init__(self, customer: Optional['Customer'], restaurant: Optional['Restaurant'], rating: int):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating_value

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews
