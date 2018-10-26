# my_project/posts/views.py

from flask import Blueprint,render_template,url_for,redirect
from my_project import db
from my_project.models import Post
from my_project.posts.forms import add_post

posts_blueprints = Blueprint('posts',__name__,
                                template_folder='templates/posts'
                                )


@posts_blueprints.route('/add',methods=['GET','POST'])
def add():
    form = add_post

    if form.validate_on_submit():
        
        title   = form.title.data
        content = form.content.data
        member_id = form.member_id.data

        # Add new member to database
        new_post = Post(title,content,member_id)
        db.session.add(new_post)
        return redirect(url_for('index'))
    return render_template('add_post.html',form = form)    



@posts_blueprints.route('/list')
def post_list():
    # Grab a list of puppies from database.
    posts = Post.query.all()
    return render_template('list_post.html', posts=posts)
