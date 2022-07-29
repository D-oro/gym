import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Kat", "Kitten")

    def test_member_has_firstname(self):
        self.assertEqual("Kat", self.member.firstname)

    def test_member_has_lastname(self):
        self.assertEqual("Kitten", self.member.lastname)