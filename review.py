# review.py

from typing import List, Optional

class Review:
    all_reviews: List['Review'] = []

    def __init__(self, customer: 'Customer', restaurant: 'Restaurant', rating: int):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self) -> int:
        return self.rating

    def customer(self) -> 'Customer':
        return self.customer

    def restaurant(self) -> 'Restaurant':
        return self.restaurant

    @classmethod
    def all(cls) -> List['Review']:
        return cls.all_reviews
