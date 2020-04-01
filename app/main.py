"""
Minimal web server using Flask
"""

from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from app.controller.login import LoginForm
from app.controller.signup import SignupForm
from app import app, db
from app.model.user import User
from app.model.api.records import RecordsAPI


db.create_all()
login_manager = LoginManager(app)
login_manager.login_view = 'login'

records_api = RecordsAPI()


@login_manager.user_loader
def load_user(user_id):
    """
    Handles automatic login when latest user is still in session
    :param user_id:
    :return:
    """
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Default landing page;
    Login using credentials;
    Implemented with backend validation
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dashboard'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/dashboard/')
@login_required
def dashboard():
    """
    Homepage upon login
    :return:
    """

    records = records_api.get_all_records()
    markers = []
    for record in records:
        markers.append([record['latitude'], record['longitude']])

    return render_template('dashboard.html', markers=markers)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    """
    Register new user; add user to backend db
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = SignupForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Register', form=form)


@app.route('/logout/')
def logout():
    """
    Logout current user
    :return:
    """
    logout_user()
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    """
    Customized Error 404 page.

    :param error:
    :return:
    """
    return render_template('404.html'), 404


""" Starting point of program"""
if __name__ == '__main__':
    app.run()
