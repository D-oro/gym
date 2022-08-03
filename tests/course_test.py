import unittest
from models.course import Course

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("Yoga", "25/08/2022", "10am", 2)

    def test_course_has_title(self):
        self.assertEqual("Yoga", self.course.title)

    def test_course_has_date(self):
        self.assertEqual("25/08/2022", self.course.date)

    def test_course_has_time(self):
        self.assertEqual("10am", self.course.time)

    def test_course_has_capacity(self):
        self.assertEqual(2, self.course.capacity)