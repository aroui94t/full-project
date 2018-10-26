# my_project/members/views.py

from flask import Blueprint,render_template,url_for,redirect
from my_project import db
from my_project.models import Member
from my_project.members.forms import add_members


members_blueprints = Blueprint('members',__name__,
                                template_folder='templates/members'
                                )


@members_blueprints.route('/add',methods=['GET','POST'])
def add():
    form = add_members()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        age = form.age.data
        password = form.password.data

        # Add new member to database
        new_member = Member(username,email,age,password)
        db.session.add(new_member)
        
        # save 
        db.session.commit()
        return redirect(url_for('members.list_members'))
    return render_template('add_members.html',form=form)


@members_blueprints.route('/list')
def member_list():
    # Grab a list of puppies from database.
    members = Member.query.all()
    return render_template('list_members.html', posts=members)