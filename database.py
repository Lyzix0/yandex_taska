from data import db_session
from data.jobs import Jobs
from data.users import User


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
