import pdb
from models.course import Course
from models.member import Member
from models.booking import Booking

import repositories.course_repository as course_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
course_repository.delete_all()
member_repository.delete_all()

member1 = Member('Kat', 'Kitten')
member_repository.save(member1)

member2 = Member('Hen', 'Rooster')
member_repository.save(member2)

course1 = Course('Yoga', '01/01/2023', '10am', 5)
course_repository.save(course1)

course2 = Course('Cardio', '02/02/2023', '9am', 2)
course_repository.save(course2)

booking1 = Booking(member1, course1)
booking_repository.save(booking1)

booking2 = Booking(member2, course1)
booking_repository.save(booking2)

booking3 = Booking(member1, course2)
booking_repository.save(booking3)

pdb.set_trace()


