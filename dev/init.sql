CREATE DATABASE tracker_db;
CREATE USER test WITH ENCRYPTED PASSWORD 'testpassword';
GRANT ALL PRIVILEGES ON DATABASE tracker_db TO test;