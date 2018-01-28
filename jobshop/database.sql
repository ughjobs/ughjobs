CREATE TABLE user  (
id integer PRIMARY KEY,
login varchar(80) UNIQUE,
password varchar(80),

name varchar(80),
surname varchar(80),
city varchar(80),
street varchar(80),
street_number varchar(80),
apartment varchar(80),
admin integer
);

CREATE TABLE job  (id integer PRIMARY KEY, title varchar(80) UNIQUE,description varchar(4096),recruiter_id integer,created datetime,surname varchar(80),active integer);

CREATE TABLE application (id integer PRIMARY KEY,job_id integer,candidate_id integer,comment varchar(4096),created datetime,status integer);

--    id = db.Column(db.Integer, primary_key=True)
--    job_id = db.Column(db.Integer)
--    candidate_id = db.Column(db.Integer)
--    comment = db.Column(db.String(4096))
--    created = db.Column(db.DateTime)
--    status = db.Column(db.Enum(ApplicationStatus))