from django.test import TestCase
from restaurant.models import Menu,booking_Model
from datetime import datetime
from decimal import Decimal

class MenuItemTest(TestCase):
    def test_create_item(self):
        item1 = Menu.objects.create(
            title="IceCream",
            price=80,
            inventory=100)
        self.assertEqual(item1.title, "IceCream")
        self.assertEqual(item1.price, 80)
        self.assertEqual(item1.inventory, 100)
        self.assertEqual(item1.description,"")

class BookingTest(TestCase):

    def test_create_booking(self):
        booking = booking_Model.objects.create(
            first_name="John Doe",
            no_of_guest=4,
            reservation_date=datetime(2023, 6, 24, 18, 0)

        )
        expected_str = "John Doe for 4 guests on 2023-06-24 18:00:00"
        self.assertEqual(str(booking.first_name) + ' for ' + str(booking.no_of_guest) + ' guests on ' +
                         str(booking.reservation_date), expected_str)
