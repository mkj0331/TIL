-- Active: 1757735905949@@localhost@3306@sns_system_db
CREATE DATABASE sns_system_db
DEFAULT CHARACTER SET = 'utf8mb4';

USE sns_system_db;

CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE posts (
  post_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  Foreign Key (user_id) REFERENCES users(user_id),
  title VARCHAR(255),
  content TEXT
);

CREATE TABLE comments (
  comment_id INT PRIMARY KEY AUTO_INCREMENT,
  post_id INT,
  Foreign Key (post_id) REFERENCES posts(post_id),
  content TEXT
);

INSERT INTO users (name, email) VALUES
('홍길동', 'hong@example.com'),
('이순신', 'lee@example.com');

INSERT INTO posts (post_id, user_id, title, content) VALUES
(101, 1, '첫 번째 게시물', '안녕하세요'),
(102, 1, '두 번째 게시물', '반갑습니다'),
(103, 2, '세 번째 게시물', '좋은 하루');

INSERT INTO comments (comment_id, post_id, content) VALUES
(1001, 101, '첫 댓글'),
(1002, 102, '두 번째 댓글'),
(1003, 103, '세 번째 댓글');


SELECT name, email FROM users;

SELECT posts.title, posts.content FROM posts JOIN users on posts.user_id = users.user_id
WHERE users.name = '홍길동';

SELECT comments.content FROM comments JOIN posts on posts.post_id = comments.post_id
WHERE posts.title = '첫 번째 게시물';

INSERT INTO users (name, email) VALUES
('김유신', 'kim@example.com');

UPDATE users SET email = 'new_lee@example.com'
WHERE users.name = '이순신';
