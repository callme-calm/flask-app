from flask import render_template, url_for, flash, redirect, request, abort, session, Blueprint
from flaskblog import db
from flaskblog.models import Post
from flaskblog.blog.forms import PostForm

blog = Blueprint('blog', __name__)

@blog.route("/post/new", methods=['GET', 'POST'])
def new_post():
    if 'user_id' not in session:
        flash('Please log in to create a post', 'danger')
        return redirect(url_for('auth.login'))
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author_id=session['user_id'])
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', form=form)



@blog.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    if 'user_id' not in session:
        flash('Please log in to update this post', 'danger')
        return redirect(url_for('auth.login'))
    post = Post.query.get(post_id)
    if post is None:
        return "Post ID not present", 404

    if post.author_id != session['user_id']:
        return "You dont have authoriyt to update ", 404
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('blog.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('home.html')

@blog.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    if 'user_id' not in session:
        flash('Please log in to delete this post', 'danger')
        return redirect(url_for('auth.login'))
    post = Post.query.get(post_id)
    if post is None:
        return "Post ID not present", 404
    if post.author_id != session['user_id']:
        return "Login first then dare to delete" ,403
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
