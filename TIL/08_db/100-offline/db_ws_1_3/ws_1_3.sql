
CREATE DATABASE sns_system_db;

USE sns_system_db;

CREATE TABLE users (
  user_id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE
);


CREATE TABLE posts (
  post_id INT PRIMARY KEY,
  title VARCHAR(255),
  content TEXT,
  created_at DATETIME,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE comments (
  comment_id INT PRIMARY KEY,
  content TEXT,
  created_at DATETIME,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  post_id INT,
  FOREIGN KEY (post_id) REFERENCES posts(post_id)
);