from flask import render_template, session, url_for, redirect, flash, request
from flask_login import login_user, login_required, logout_user

from app.forms import LoginForm
from . import auth
from app.firestore_service import get_user
from app.models import UserModel, UserData

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data #obtenemos el username
        password = login_form.password.data
        next_url = request.form.get("next")
        user_doc= get_user(username)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                flash('Welcome back')
                # if next_url:
                #     return redirect(next_url)
                return redirect(url_for("hello"))
            else:
                flash('This information is not correct')
        else:
            flash('User or Password do no exist')

        return redirect(url_for('index'))

    return render_template('login.html',**context)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Welcome Back Soon')

    return redirect(url_for('auth.login'))