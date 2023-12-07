import unittest
from customer import Customer
from restaurant import Restaurant
from review import Review

class TestCustomer(unittest.TestCase):

    def setUp(self):
        # Create some sample data for testing
        self.customer1 = Customer("John", "Doe")
        self.customer2 = Customer("Jane", "Smith")
        self.restaurant = Restaurant("Sample Restaurant")

    def test_properties(self):
        self.assertEqual(self.customer1.given_name, "John")
        self.assertEqual(self.customer1.family_name, "Doe")
        self.assertEqual(self.customer1.full_name(), "John Doe")

    def test_class_methods(self):
        self.assertEqual(Customer.all(), [self.customer1, self.customer2])
        self.assertEqual(Customer.find_by_name("John Doe"), self.customer1)
        self.assertEqual(Customer.find_all_by_given_name("Jane"), [self.customer2])

    def test_review_interaction(self):
        self.customer1.add_review(self.restaurant, 4)
        self.assertEqual(self.customer1.num_reviews(), 1)
        self.assertEqual(self.customer1.restaurants(), [self.restaurant])

class TestRestaurant(unittest.TestCase):

    def setUp(self):
        # Create some sample data for testing
        self.restaurant1 = Restaurant("Restaurant A")
        self.restaurant2 = Restaurant("Restaurant B")
        self.customer = Customer("John", "Doe")

    def test_properties(self):
        self.assertEqual(self.restaurant1.name, "Restaurant A")

    def test_class_methods(self):
        self.assertEqual(Restaurant.all_restaurants, [self.restaurant1, self.restaurant2])

    def test_review_interaction(self):
        self.customer.add_review(self.restaurant1, 3)
        self.assertEqual(self.restaurant1.customers(), [self.customer])
        self.assertEqual(self.restaurant1.average_star_rating(), 3)

class TestReview(unittest.TestCase):

    def setUp(self):
        # Create some sample data for testing
        self.customer = Customer("John", "Doe")
        self.restaurant = Restaurant("Sample Restaurant")
        self.review = Review(self.customer, self.restaurant, 4)

    def test_properties(self):
        self.assertEqual(self.review.rating, 4)

    def test_class_methods(self):
        self.assertEqual(Review.all_reviews, [self.review])
        self.assertEqual(self.review.customer(), self.customer)
        self.assertEqual(self.review.restaurant(), self.restaurant)

if __name__ == '__main__':
    unittest.main()
