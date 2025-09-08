-- 데이터베이스 생성
CREATE DATABASE hospital_db;

USE hospital_db;


-- patients 테이블 생성
CREATE TABLE patients (
  patient_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  birthdate DATE NOT NULL,
  phone_number VARCHAR(15),
  email VARCHAR(50) UNIQUE,
  address VARCHAR(200)
);

-- 필드 추가
ALTER Table patients
ADD gender VARCHAR(10);

-- 필드 수정
ALTER TABLE patients
MODIFY phone_number VARCHAR(20);

-- 테이블에 있는 데이터 삭제
TRUNCATE TABLE patients;