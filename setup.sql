-- CREATE DATABASE TABLE

CREATE TABLE IF NOT EXISTS task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(128),
  summary VARCHAR(255),
  description TEXT,
  is_done BOOLEAN DEFAULT 0
);

-- Create some dummy data to test
INSERT INTO task (
    name,
    summary,
    description
  ) VALUES
  ('wash dishes', 'use dish soap to wash dishes', 'Description 1'),
  ('Walk dog', 'take scooby to the park', 'Description 2'),
  ('Buy groceries', 'Drive to the store and buy groceries', 'Description 3'),
  ('Task 4', 'Summary 4', 'Description 4'),
  ('Task 5', 'Summary 5', 'Description 5');