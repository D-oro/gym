from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# route to view all members
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

# route to add new member
@members_blueprint.route("/members/new")
def new():
    members = member_repository.select_all()
    return render_template("/members/new.html", members = members)


# post route to actually add the input from the new member page
@members_blueprint.route("/members", methods=['POST'])
def create():
    firstname = request.form['firstname']
    lastname = request.form['lastname']

    if request.form['premium'] == 'Yes':
        premium = 2
    else:
        premium = 1

    member = Member(firstname, lastname, premium)
    member_repository.save(member)
    return redirect('/members')


# route to edit member
@members_blueprint.route("/members/<id>/edit")
def edit(id):
    member = member_repository.select(id)
    return render_template('/members/edit.html', member = member)


# route to update the member we're editing
@members_blueprint.route("/members/<id>", methods=['POST'])
def update(id):
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    if request.form['premium'] == 'Yes':
        premium = 2
    else:
        premium = 1
    member = Member(firstname, lastname, premium, id)
    member_repository.update(member)
    return redirect('/members')