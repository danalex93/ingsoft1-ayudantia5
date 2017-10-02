from models.post import Post
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = '14e69cd065664ebcbb273a07c8105b2e338717fc4786de2479daa8b60d11e3ee9ebf16b80cd04a0ca746164fea8047be6cd76f19ede2ecb75e3ab290beacd472'

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/posts", methods=['GET'])
def posts():
  posts = Post().all()
  return render_template('posts.html', posts=posts)

@app.route("/posts", methods=['POST'])
def create_post():
  post = Post()
  if post.create(request.form['title'], request.form['description']):
    flash("New post was successfully published")
  else:
    flash("New post can't be published")

  return redirect(url_for('posts'))

@app.route("/posts/<id>/delete")
def delete_post(id):
  post = Post()
  if post.destroy(id):
    flash("Post was successfully deleted")
  else:
    flash("Post can't be deleted")

  return redirect(url_for('posts'))


@app.route("/about")
def about():
  return render_template("about.html")