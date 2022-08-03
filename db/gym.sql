DROP TABLE bookings;
DROP TABLE members;
DROP TABLE courses;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255),
    lastname VARCHAR(255)
);

CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    capacity INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    course_id INT REFERENCES courses(id)
);

