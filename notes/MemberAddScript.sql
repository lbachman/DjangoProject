<<<<<<< HEAD:notes/script.sql
DROP TABLE IF EXISTS facebook.members_member;

CREATE TABLE facebook.members_member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL
);

INSERT INTO facebook.members_member (firstname, lastname, username) VALUES
    ('John', 'Doe', 'jdoe'),
    ('Jane', 'Smith', 'jsmith'),
    ('Michael', 'Johnson', 'mjohnson'),
    ('Emily', 'Williams', 'ewilliams'),
    ('Daniel', 'Brown', 'dbrown'),
    ('Sophia', 'Jones', 'sjones'),
    ('Matthew', 'Clark', 'mclark'),
    ('Olivia', 'Anderson', 'oanderson'),
    ('William', 'Taylor', 'wtaylor'),
    ('Emma', 'Moore', 'emoore');
=======
-- CREATE TABLE facebook.member (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     firstname VARCHAR(255) NOT NULL,
--     lastname VARCHAR(255) NOT NULL
-- );

INSERT INTO facebook.members_member (firstname, lastname) VALUES
    ('John', 'Doe'),
    ('Jane', 'Smith'),
    ('Michael', 'Johnson'),
    ('Emily', 'Williams'),
    ('Daniel', 'Brown'),
    ('Sophia', 'Jones'),
    ('Matthew', 'Clark'),
    ('Olivia', 'Anderson'),
    ('William', 'Taylor'),
    ('Emma', 'Moore');
>>>>>>> b95f1a8264833bb3eb1d87161186a88771da9495:notes/MemberAddScript.sql
