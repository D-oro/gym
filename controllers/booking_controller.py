from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

bookings_blueprint = Blueprint("bookings", __name__)


# GET route to see all members booked onto one course
@bookings_blueprint.route("/bookings/<id>")
def bookings(id):
    bookings = booking_repository.find_booking_by_course_id(id)
    course = course_repository.select(id)

    return render_template("/bookings/show.html", bookings = bookings, course = course)

# GET route to the page where I can add a member onto one course
@bookings_blueprint.route("/bookings/<id>/new")
def new(id):
    bookings = booking_repository.find_booking_by_course_id(id)
    course = course_repository.select(id)
    members = member_repository.select_all()
    return render_template('/bookings/new.html', bookings=bookings, course=course, members=members)

# route to add the member onto the chosen course
@bookings_blueprint.route("/bookings/<id>", methods=['POST'])
def update(id):
    member_id = request.form['member_id']
    member = member_repository.select(member_id)
    course = course_repository.select(id)
    booking = Booking(member, course)
    booking_repository.save(booking)
    return redirect(f'/bookings/{id}')

    