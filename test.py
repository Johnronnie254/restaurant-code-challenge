import unittest
from customer import Customer
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.restaurant1 = Restaurant("Restaurant A")
        self.restaurant2 = Restaurant("Restaurant B")
        self.customer = Customer("John", "Doe")

    def test_restaurant_creation(self):
        self.assertEqual(self.restaurant1.name, "Restaurant A")
        self.assertEqual(self.restaurant2.name, "Restaurant B")

    def test_customer_creation(self):
        self.assertEqual(self.customer.full_name(), "John Doe")

    def test_add_review(self):
        self.customer.add_review(self.restaurant1, 4)
        self.customer.add_review(self.restaurant2, 5)
        self.assertEqual(len(self.customer.reviews()), 2)

    def test_all_restaurants(self):
        self.assertEqual(Restaurant.all_restaurants, [self.restaurant1, self.restaurant2])

    def test_review_interaction(self):
        self.customer.add_review(self.restaurant1, 4)
        self.assertEqual(self.restaurant1.customers(), [self.customer])

if __name__ == '__main__':
    unittest.main()
