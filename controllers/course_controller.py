from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

# route to view all courses
@courses_blueprint.route("/courses")
def courses():
    courses = course_repository.select_all()
    return render_template("courses/index.html", courses = courses)

# route to add new course
@courses_blueprint.route("/courses/new")
def new():
    courses = course_repository.select_all()
    return render_template('/courses/new.html', courses=courses)

# route to edit course
@courses_blueprint.route("/courses/<id>/edit")
def edit(id):
    course = course_repository.select(id)
    return render_template('/courses/edit.html', course=course)



