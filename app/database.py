from app import app,db
import datetime


class Student(db.Model):
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.datetime.utcnow()
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)
    def __repr__(self):
        return '<User %r>' % (self.username)


class Teacher(db.Model):
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.datetime.utcnow()
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)
    def __repr__(self):
        return '<User %r>' % (self.username)

class Course(db.Model):
    course_id = db.Column('id', db.Integer, primary_key=True)
    course_name = db.Column('course_name', db.String(30), unique=True)
    # todo: make faculty a foreign key to refer to the teacher table
    faculty = db.Column('faculty', db.String(30))

    def __init__(self,name, faculty):
        self.course_name = name
        self.faculty = faculty


class Registration(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column('student_id', db.Integer)
    username = db.Column('username', db.String(20))
    guardian_name = db.Column('guardian_name', db.String(20))
    class10_percentage = db.Column('class10_percentage', db.String(5))
    class12_percentage = db.Column('class12_percentage', db.String(5))
    class10_doc = db.Column('class10_doc', db.String(40))
    class12_doc = db.Column('class12_doc', db.String(40))
    registration_time = db.Column('registration_time', db.DateTime)
    approved = db.Column('approved', db.Boolean)

    def __init__(self,
    student_id,
    username,
    guardian_name,
    class10_percentage,
    class12_percentage,
    class10_doc,
    class12_doc):
        self.student_id = student_id
        self.username = username
        self.guardian_name = guardian_name
        self.class10_percentage = class10_percentage
        self.class10_doc = class10_doc
        self.class12_percentage = class12_percentage
        self.class12_doc = class12_doc
        self.registration_time = datetime.datetime.utcnow()
        self.approved = False
