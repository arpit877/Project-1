import sqlite3 

conn= sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute ("CREATE TABLE customer (id INTEGER,name TEXT,email TEXT,subscription TEXT)"); 
print ("Table created successfully");
conn.close()

