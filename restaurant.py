from typing import List, Optional
from review import Review  # Import the Review class

class Restaurant:
    all_restaurants: List['Restaurant'] = []

    def __init__(self, name: str):
        self.name = name
        self.reviews_list = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def add_review(self, review):
        self.reviews_list.append(review)

    def reviews(self):
        return self.reviews_list

    def num_reviews(self):
        return len(self.reviews_list)

    def average_review(self):
        if not self.reviews_list:
            return 0
        return sum(review.get_rating() for review in self.reviews_list) / len(self.reviews_list)
