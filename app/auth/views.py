from flask import render_template, session, url_for, redirect, flash
from app.forms import LoginForm
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data #obtenemos el username
        session['username']= username #lo guardamos en la sesion para enviarlo al contexto

        flash('Successfully Registered')
        return redirect(url_for('index'))
    return render_template('login.html',**context)