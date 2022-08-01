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

def select(id):
    course = None
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        course = Course(result['title'], result['date'], result['time'], result['id'])
    return course

def members(id):
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.id = bookings.member_id WHERE bookings.course_id = %s"
    values = [id]
    results = run_sql(sql, values)

    members = []
    for row in results:
        member = Member(row['firstname'], row['lastname'], row['id'])
        members.append(member)
    return members

