from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


def create_user(surname: str = None, name: str = None, age: int = None, position: str = None, speciality: str = None,
                address: str = None, email: str = None, hashed_password: str = None):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    if hashed_password is None:
        user.hashed_password = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    else:
        user.hashed_password = hashed_password
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def create_job():
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    db_session.global_init("db/users.db")
    captain = ['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org']
    first_officer = ['Jones', 'Ellen', 35, 'first officer', 'navigation specialist', 'module_2', 'ellen_jones@mars.org']
    engineer = ['Smith', 'John', 28, 'engineer', 'mechanical engineer', 'module_3', 'john_smith@mars.org']
    scientist = ['Johnson', 'Emily', 40, 'scientist', 'geologist', 'module_4', 'emily_johnson@mars.org']

    all_users = [captain, first_officer, engineer, scientist]

    for user in all_users:
        create_user(*user)

    app.run(port=8080, host='127.0.0.1')
