-- Active: 1755825481655@@127.0.0.1@3306@hospital_db
CREATE DATABASE hospital_db;

USE hospital_db;


-- 환자 테이블
CREATE TABLE patient (
  patient_id   INT PRIMARY KEY,
  first_name   VARCHAR(50),
  last_name    VARCHAR(50),
  birth_date   DATE,
  phone_number VARCHAR(15)
);

-- 의사 테이블
CREATE TABLE doctor (
  doctor_id   INT PRIMARY KEY,
  first_name  VARCHAR(50),
  last_name   VARCHAR(50),
  specialty   VARCHAR(100)
);

-- 진료 기록 테이블
CREATE TABLE visits (
  visit_id   INT PRIMARY KEY,
  patient_id INT,
  doctor_id  INT,
  visit_date DATE,
  CONSTRAINT fk_visits_patient
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
  CONSTRAINT fk_visits_doctor
    FOREIGN KEY (doctor_id)  REFERENCES doctor(doctor_id)
);

-- 데이터 삽입: patient
INSERT INTO patient (patient_id, first_name, last_name, birth_date, phone_number) VALUES
(1, 'John',  'Doe',   '1990-01-01', '123-456-7890'),
(2, 'Jane',  'Smith', '1985-02-02', '098-765-4321'),
(3, 'Alice', 'White', '1970-03-15', '111-222-3333');

-- 데이터 삽입: doctor
INSERT INTO doctor (doctor_id, first_name, last_name, specialty) VALUES
(1, 'Alice',   'Brown',  'Cardiology'),
(2, 'Bob',     'Johnson','Neurology'),
(3, 'Charlie', 'Davis',  'Dermatology');

-- 데이터 삽입: visits
INSERT INTO visits (visit_id, patient_id, doctor_id, visit_date) VALUES
(1, 1, 1, '2024-01-01'),
(2, 2, 2, '2024-02-01'),
(3, 1, 2, '2024-03-01'),
(4, 3, 3, '2024-04-01'),
(5, 1, 2, '2024-05-01'),
(6, 2, 3, '2024-06-01'),
(7, 3, 1, '2024-07-01');


SELECT * FROM patient;
SELECT * FROM doctor;
SELECT * FROM visits;

-- 각 환자의 이름, 전화번호, 모든 방문 날짜, 각 방문별 담당 의사의 이름, 그리고 전문 분야를 조회하시오.
CREATE VIEW temp AS 
SELECT patient.first_name, patient.last_name, patient.phone_number, visits.visit_date, doctor.first_name as doctor_first_name, doctor.last_name as doctor_last_name, doctor.specialty
FROM visits JOIN patient on visits.patient_id = patient.patient_id
JOIN doctor on doctor.doctor_id = visits.doctor_id;
SELECT * FROM temp;


-- 지난 1년 동안(2024년 한 해) 방문한 환자들 중에서 의사별로 방문 횟수를 조회하시오.
SELECT d.first_name, d.last_name, d.specialty, COUNT(v.visit_id) as visit_count
FROM doctor d JOIN visits v on v.doctor_id = d.doctor_id
GROUP BY d.doctor_id;


-- ID가 2인 의사에게 방문한 환자 목록을 조회하되, 방문 횟수가 두 번 이상인 환자만 조회하시오.
SELECT p.first_name, p.last_name, p.phone_number, count(v.visit_id) as visit_count
FROM patient p JOIN visits v ON p.patient_id = v.patient_id
JOIN doctor d ON d.doctor_id = v.doctor_id
WHERE d.doctor_id = 2
GROUP BY p.patient_id
HAVING visit_count > 1;

