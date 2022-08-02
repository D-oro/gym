from db.run_sql import run_sql
from models.member import Member
from models.course import Course
from models.booking import Booking

def save(course):
    sql = "INSERT INTO courses(title, date, time) VALUES (%s, %s, %s) RETURNING id"
    values = [course.title, course.date, course.time]
    results = run_sql(sql, values)
    course.id = results[0]['id']
    return course

def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)

def select_all():
    courses = []

    sql = "SELECT * FROM courses"
    results = run_sql(sql)

    for row in results:
        course = Course(row['title'], row['date'], row['time'], row['id'])
        courses.append(course)
    return courses

#select one course
def select(id):
    course = None
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        print(f"result = {result}")
        result = result[0]
        course = Course(result['title'], result['date'], result['time'], result['id'])
    return course

#update one course
def update(course):
    sql = "UPDATE courses SET (title, date, time) = (%s, %s, %s) WHERE id=%s"
    values = [course.title, course.date, course.time, course.id]
    run_sql(sql, values)


def members(id):
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.id = bookings.member_id WHERE bookings.course_id = %s"
    values = [id]
    results = run_sql(sql, values)

    members = []
    for row in results:
        member = Member(row['firstname'], row['lastname'], row['id'])
        members.append(member)
    return members

