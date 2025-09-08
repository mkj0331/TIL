-- 데이터베이스 생성
CREATE DATABASE hospital_db;

USE hospital_db;


-- hospital 테이블 생성
CREATE TABLE hospital (
  hospital_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  location VARCHAR(200) NOT NULL,
  established_date DATE,
  contact_number VARCHAR(20) UNIQUE,
  type VARCHAR(50) NOT NULL
)


-- 테이블 수정
ALTER TABLE hospital
ADD capacity INT;

ALTER TABLE hospital
MODIFY type VARCHAR(100);

ALTER TABLE hospital
RENAME COLUMN established_date TO founded_date;

-- 테이블 삭제
DROP TABLE hospital;