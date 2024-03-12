from flask import Flask, render_template, redirect
from flask_login import login_user, LoginManager
from flask_restful import Api

import users_resource
from data import db_session
from data.users import User
from forms.login import LoginForm

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def image(prof):
    return render_template('second.html', prof=prof)


@app.route('/list_prof/<string:list>')
def list_prof(list):
    return render_template('third.html', list=list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UserResource, '/api/v2/users/<int:user_id>')


if __name__ == '__main__':
    db_session.global_init("./db/users.db")
    app.run(port=8080, host='127.0.0.1')
