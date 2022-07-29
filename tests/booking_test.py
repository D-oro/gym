import unittest
from models.booking import Booking

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking = Booking("member1", "course1")

    def test_booking_has_member(self):
        self.assertEqual("member1", self.booking.member)

    def test_booking_has_course(self):
        self.assertEqual("course1", self.booking.course)
        