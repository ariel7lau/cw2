from flask import Blueprint, render_template, request, redirect, url_for, flash
from portfolio import db
from portfolio.model import Comment

auth = Blueprint('auth', __name__)

@auth.route('/<home>/')
def home():
    return render_template('home.html')

@auth.route('/<about>/')
def about():
    return render_template('about.html')

@auth.route('/<comment>/', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        message = Comment(name=name, message=message)
        if len(message) < 1:
            flash('Comment is too short!', category='error')  
        else:   
            db.session.add(message)
            db.session.commit()
            flash('Comment posted!', category='success')
            return render_template("comment.html")
