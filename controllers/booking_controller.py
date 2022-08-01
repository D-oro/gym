from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings/<id>")
def bookings(id):
    bookings = booking_repository.find_booking_by_course_id(id)
    course = course_repository.select(id)

    return render_template("/bookings/show.html", bookings = bookings, course = course)




@bookings_blueprint.route("/bookings/<id>/new")
def new(id):
    booking = booking_repository.select(id)
    return render_template('/bookings/new.html', booking=booking)

