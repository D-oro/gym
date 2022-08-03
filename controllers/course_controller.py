from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository
import repositories.booking_repository as booking_repository

courses_blueprint = Blueprint("courses", __name__)

# route to view all courses
@courses_blueprint.route("/courses")
def courses():
    booking = booking_repository.select_all()
    courses = course_repository.select_all()
    return render_template("courses/index.html", courses = courses, booking = booking)

# route to add new course
@courses_blueprint.route("/courses/new")
def new():
    courses = course_repository.select_all()
    return render_template('/courses/new.html', courses=courses)

# post route to actually add the input from the new course page
@courses_blueprint.route("/courses", methods=['POST'])
def create():
    title = request.form['title']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']

    if request.form['peak'] == 'Yes':
        peak = 2
    else:
        peak = 1

    course = Course(title, date, time, capacity, peak)
    course_repository.save(course)
    return redirect('/courses')

# route to edit course
@courses_blueprint.route("/courses/<id>/edit")
def edit(id):
    course = course_repository.select(id)
    return render_template('/courses/edit.html', course=course)

# route to update the course we're editing
@courses_blueprint.route("/courses/<id>", methods=['POST'])
def update(id):
    title = request.form['title']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']
    peak = request.form['peak']
    course = Course(title, date, time, capacity, peak, id)
    course_repository.update(course)
    return redirect('/courses')
    
