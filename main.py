from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import enum
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'SecretPassword'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    city = db.Column(db.String(50))
    street = db.Column(db.String(50))
    street_number = db.Column(db.String(50))
    apartment = db.Column(db.String(50))
    admin = db.Column(db.Boolean)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(4096))
    recruiter_id = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    active = db.Column(db.Boolean)


class ApplicationStatus(enum.Enum):
    NEW = 1
    UNDER_REVIEW = 2
    REJECTED = 3
    ACCEPTED = 4


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer)
    candidate_id = db.Column(db.Integer)
    comment = db.Column(db.String(4096))
    created = db.Column(db.DateTime)
    status = db.Column(db.Enum(ApplicationStatus))


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome home!'})


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(login=data['login'], password=hashed_password, name=data['name'], surname=data['surname'],
                    city=data['city'], street=data['street'], street_number=data['street_number'],
                    apartment=data['apartment'],
                    admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})


@app.route('/user', methods=['GET'])
@token_required
def read_users(current_user):
    users = User.query.all()

    output = []

    for user in users:
        user_data = {'id': user.id, 'login': user.login, 'password': user.password, 'name': user.name,
                     'surname': user.surname, 'city': user.city, 'street': user.street,
                     'street_number': user.street_number, 'apartment': user.apartment, 'admin': user.admin}

        output.append(user_data)

    return jsonify({'users': output})


@app.route('/user/<user_id>', methods=['GET'])
@token_required
def read_user(current_user, user_id):
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user_data = {'id': user.id, 'login': user.login, 'password': user.password, 'name': user.name,
                 'surname': user.surname, 'city': user.city, 'street': user.street, 'street_number': user.street_number,
                 'apartment': user.apartment, 'admin': user.admin}

    return jsonify({'user': user_data})


@app.route('/user/<user_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, user_id):
    if not current_user.admin:
        return jsonify({'message': 'You must be admin!'})

    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user has been deleted!'})


@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        print('No')
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(login=auth.username).first()

    if not user:
        print('No user')
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

        token = jwt.encode(dict(id=user.id, exp=expiration_time), app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})
    print('Password mismatch')
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


@app.route('/user/<user_id>', methods=['PUT'])
@token_required
def promote_user(current_user, user_id):
    if not current_user.admin:
        return jsonify({'message': 'You must be admin!'})

    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user.admin = True
    db.session.commit()

    return jsonify({'message': 'The user has been promoted!'})


@app.route('/job', methods=['POST'])
@token_required
def create_job(current_user):
    data = request.get_json()
    new_job = Job(title=data['title'], description=data['description'], recruiter_id=current_user.id,
                  created=datetime.datetime.now(), active=True)

    db.session.add(new_job)
    db.session.commit()

    return jsonify({'message': 'New user created!'})


@app.route('/job', methods=['GET'])
@token_required
def read_jobs(current_user):
    jobs = Job.query.all()

    output = []

    for job in jobs:
        job_data = {'id': job.id, 'title': job.title, 'description': job.description, 'recruiter_id': job.recruiter_id,
                    'created': job.created, 'active': job.active}

        output.append(job_data)

    return jsonify({'jobs': output})


@app.route('/job/<job_id>', methods=['GET'])
@token_required
def read_job(current_user, job_id):
    job = Job.query.filter_by(id=job_id).first()

    if not job:
        return jsonify({'message': 'No job found!'})

    job_data = {'id': job.id, 'title': job.title, 'description': job.description, 'recruiter_id': job.recruiter_id,
                'created': job.created, 'active': job.active}

    return jsonify({'job': job_data})


@app.route('/job/<job_id>', methods=['DELETE'])
@token_required
def delete_job(current_user, job_id):
    if not current_user.admin:
        return jsonify({'message': 'You must be admin!'})
    job = Job.query.filter_by(id=job_id).first()

    if not job:
        return jsonify({'message': 'No job found!'})

    db.session.delete(job)
    db.session.commit()

    return jsonify({'message': 'The job has been deleted!'})


@app.route('/job/<job_id>', methods=['PUT'])
@token_required
def toggle_job(current_user, job_id):
    job = Job.query.filter_by(id=job_id).first()

    if not job:
        return jsonify({'message': 'No job found!'})

    job.active = not job.active
    db.session.commit()

    return jsonify({'message': 'The Job has been changed!'})


@app.route('/application', methods=['POST'])
@token_required
def create_application(current_user):
    data = request.get_json()
    application = Application(job_id=data['job_id'], candidate_id=current_user.id, comment=data['comment'],
                              created=datetime.datetime.utcnow(), status=ApplicationStatus.NEW)

    db.session.add(application)
    db.session.commit()

    return jsonify({'message': 'New application created!'})


@app.route('/application', methods=['GET'])
@token_required
def read_applications(current_user):
    applications = Application.query.all()

    output = []

    for application in applications:
        application_data = {'id': application.id, 'job_id': application.job_id, 'comment': application.comment,
                            'candidate_id': application.candidate_id,
                            'created': application.created, 'status': application.status}

        output.append(application_data)

    return jsonify({'applications': output})


@app.route('/application/<application_id>', methods=['GET'])
@token_required
def read_application(current_user, application_id):
    application = Application.query.filter_by(id=application_id).first()

    if not application:
        return jsonify({'message': 'No application found!'})

    application_data = {'id': application.id, 'job_id': application.job_id, 'comment': application.comment,
                        'candidate_id': application.candidate_id,
                        'created': application.created, 'status': application.status}

    return jsonify({'application': application_data})


@app.route('/application/<application_id>', methods=['DELETE'])
@token_required
def delete_application(current_user, application_id):
    if not current_user.admin:
        return jsonify({'message': 'You must be admin!'})

    job = Application.query.filter_by(id=application_id).first()

    if not job:
        return jsonify({'message': 'No application found!'})

    db.session.delete(job)
    db.session.commit()

    return jsonify({'message': 'The application has been deleted!'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
