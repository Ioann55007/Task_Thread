import json

import requests
import psycopg2



conn = psycopg2.connect(dbname="test_task", user="postgres", password="ioann005", host="127.0.0.1", port="5432")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE QUIZZES  
     (id serial, PRIMARY KEY,
      x int
     ''')

cursor.execute('''CREATE TABLE  CATEGORY 
     (id serial, PRIMARY KEY,
      category_name text,
      id_category int,
      FOREIGN KEY (id_category) REFERENCES QUIZZES(id)
     ''')

conn.commit()
conn.close()


class Test:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def valid_unique(self, x):
        params = {'key': x}
        get_quizzes = requests.get('https://jservice.io/', params)
        with conn.cursor():
            cursor.execute("INSERT INTO QUIZZES (UNIQUE(x) VALUES(get_quizzes)")


    def get_count_category(self, name_category: str):
        cursor.execute('SELECT COUNT(*) FROM CATEGORY')
        name_category = cursor.fetchall()
        cursor.close()
        conn.close()
        return name_category

    def return_record(self, y):
        cursor.execute("SELECT * FROM QUIZZES, CATEGORY")
        y = cursor.fetchall()
        cursor.close()
        conn.close()

        with open('data_json.txt', 'w') as my_file:
            json.dump(y, my_file)

        return y



