from flask import render_template, request, flash, redirect, url_for, session
from src.app import app

from src.models.retailers.retailer import Retailer


@app.route("/")
def home_method():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        if Retailer.is_login_valid(username, password):
            retailer = Retailer.get_by_username(username)
            session['uid'] = retailer._id
            return redirect(url_for('.redirect_to_dash'))
        else:
            return render_template('login.html')

    return render_template('login.html')


@app.route('/redirecting')
def redirect_to_dash():
    if 'uid' in session.keys() and session['uid'] is not None:
        return redirect(url_for('retailer.dashboard', user_id=session['uid']))
    else:
        return redirect(url_for('home_method'))

@app.route('/logout')
def logout():
  session['username'] = None
  session.clear()
  return redirect(url_for('home_method'))


