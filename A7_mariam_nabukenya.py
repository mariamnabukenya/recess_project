# context manager
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

with open_file('trail.txt', 'r') as f:
    contents = f.read()
    print (contents)

# context manager for database connection
import sqlite3
class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.connection.close()

    def create_table_if_not_exists(self):
        cursor = self.connection.cursor()
        cursor.execute(
             '''CREATE TABLE IF NOT EXISTS mytable(
                       id INTEGER PRIMARY KEY,
                       name VARCHAR(255) NOT NULL,
                       course TEXT
                       )'''
             )
        self.connection.commit()


database_name ="traildb.db"

with Database(database_name) as connection:
     cursor = connection.cursor()
     try:
      cursor.execute("SELECT * FROM mytable ")
     except sqlite3.OperationalError as e:
         print("Error in database: {e}")
     rows = cursor.fetchall()
     for row in rows:
        print(row)

#multi threading and multi processing 
import threading
import multiprocessing
import time
def run(duration):
    print("thread has started")
    time.sleep(duration)
    print("thread has finished")

duration =[4,2,6,7]

threads = []
for x in duration:
    thread = threading.Thread(target=run,args = (duration))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("threads are done")

#multi processing
processes =[]
for x in duration:
    process = multiprocessing.Process(target=run,args=(duration))
    process.start()
    processes.append(process)

for process in processes:
    process.join()

print("processes are done ")
