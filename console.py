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

member1 = Member('Kat', 'Kitten', 2)
member_repository.save(member1)

member2 = Member('Siam', 'Ese', 1)
member_repository.save(member2)

member3 = Member('Tom', 'Eatsjerry', 2)
member_repository.save(member3)

member4 = Member('Grumpy', 'Cat', 1)
member_repository.save(member4)

member5 = Member('Kitten', 'Boots', 2)
member_repository.save(member5)

member6 = Member('Gar', 'Field', 1)
member_repository.save(member6)

course1 = Course('Feather and String', '01/01/2023', '10am', 5, 1)
course_repository.save(course1)

course2 = Course('Cardboard Boxing', '02/02/2023', '9am', 2, 2)
course_repository.save(course2)

course3 = Course('Laserpointer', '02/05/2022', '5pm', 4, 1)
course_repository.save(course3)

course4 = Course('Scratchpost', '10/10/2022', '4pm', 3, 2)
course_repository.save(course4)

booking1 = Booking(member1, course1)
booking_repository.save(booking1)

booking2 = Booking(member2, course1)
booking_repository.save(booking2)

booking3 = Booking(member1, course2)
booking_repository.save(booking3)

booking4 = Booking(member6, course4)
booking_repository.save(booking4)

booking5 = Booking(member5, course3)
booking_repository.save(booking5)

pdb.set_trace()


