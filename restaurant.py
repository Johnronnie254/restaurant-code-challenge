# restaurant.py

from typing import List, Optional
from review import Review

class Restaurant:
    all_restaurants: List['Restaurant'] = []

    def __init__(self, name: str):
        self.name = name
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return [review for review in Review.all() if review.restaurant() == self]

    def customers(self):
        return list(set(review.customer() for review in self.reviews()))

    def average_star_rating(self):
        ratings = [review.rating() for review in self.reviews()]
        if not ratings:
            return 0
        return sum(ratings) / len(ratings)
