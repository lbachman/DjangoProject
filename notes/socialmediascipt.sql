-- This script creates four tables:

--     users: Stores information about users such as their username, email, password, and the timestamp when they joined.
--     posts: Stores posts made by users. Each post is associated with a user through the user_id foreign key.
--     comments: Stores comments made by users on posts. Each comment is associated with a user and a post through the user_id and post_id foreign keys.
--     likes: Stores likes made by users on posts. Each like is associated with a user and a post through the user_id and post_id foreign keys.

-- These tables have relational aspects such as foreign key constraints to ensure referential integrity. For example, a user cannot be deleted if there are posts, 
-- comments, or likes associated with that user due to the ON DELETE CASCADE constraint, ensuring that related data remains consistent.

-- Create users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create posts table
CREATE TABLE posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create comments table
CREATE TABLE comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    post_id INT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

-- Create likes table
CREATE TABLE likes (
    like_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    post_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);
