-- 데이터베이스 생성
CREATE DATABASE sns_db;

USE sns_db;

-- users 테이블 생성
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255),
  email VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- posts 테이블 생성
CREATE TABLE posts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id),
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- users 테이블에 profile_picture 필드 추가
ALTER TABLE users
ADD profile_picture VARCHAR(255);


-- users 테이블에서 email 필드의 크기를 255에서 320으로 변경
ALTER TABLE users
MODIFY email VARCHAR(320);

ALTER TABLE posts
ADD title VARCHAR(255);

ALTER TABLE posts
MODIFY content LONGTEXT;