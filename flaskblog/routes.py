from flask import render_template, url_for, flash, redirect, request, session, abort, Blueprint
from flaskblog.blog.forms import PostForm
from flaskblog.models import User, Post




main = Blueprint('main', __name__)




@main.route("/")
@main.route("/home")
def home():

    if 'user_id' not in session:
        posts = Post.query.all()
        return render_template('home.html', posts=posts)

    return redirect(url_for('main.account'))

@main.route("/account")
def account():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = User.query.get(user_id)
    posts = Post.query.all()  # Filter posts by the current user

    return render_template('account.html', title='Your Posts', posts=posts, user=user)
