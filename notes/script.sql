CREATE TABLE facebook.member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL
);


INSERT INTO facebook.member (firstname, lastname) VALUES
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