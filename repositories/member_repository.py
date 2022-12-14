from db.run_sql import run_sql
from models.member import Member
from models.course import Course

def save(member):
    sql = "INSERT INTO members(firstname, lastname, premium) VALUES (%s, %s, %s) RETURNING id"
    values = [member.firstname, member.lastname, member.premium]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['firstname'], row['lastname'], row['premium'], row['id'])
        members.append(member)
    return members

#select one member
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id =%s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        member = Member(result['firstname'], result['lastname'], result['premium'], result['id'])
    return member

#update one member
def update(member):
    sql = "UPDATE members SET (firstname, lastname, premium) = (%s, %s, %s) WHERE id =%s"
    values = [member.firstname, member.lastname, member.premium, member.id]
    run_sql(sql, values)



def courses(id):
    sql = "SELECT courses.* FROM courses INNER JOIN bookings ON courses.id = bookings.course_id WHERE bookings.member_id = %s"
    values = [id]
    results = run_sql(sql, values)

    courses = []
    for row in results:
        course = Course(row['title'], row['date'], row['time'], row['id'])
        courses.append(course)
    return courses 