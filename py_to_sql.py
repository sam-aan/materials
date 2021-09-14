import psycopg2

def sozdanie_tabl():

  con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="sepiaabrain2012",
    host="127.0.0.1",
    port="5432"
  )

  print("Database opened successfully")
  cur = con.cursor()
  cur.execute('''CREATE TABLE IDIOT  
       (ADMISSION INT PRIMARY KEY NOT NULL,
       NAME TEXT NOT NULL,
       AGE INT NOT NULL,
       COURSE CHAR(50),
       DEPARTMENT CHAR(50));''')

  print("Table created successfully")
  con.commit()
  con.close()

def Vvod_data():
  con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="sepiaabrain2012",
    host="127.0.0.1",
    port="5432"
  )

  print("Database opened successfully")
  cur = con.cursor()
  cur.execute(
    "INSERT INTO IDIOT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')"
  )

  con.commit()
  print("Record inserted successfully")

  con.close()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    s = input('что сделать? создать табл "s", внести данные "v", изменить данные "i"')
    if s == 's':
      sozdanie_tabl()
    elif s == 'v':
      Vvod_data()

'''Ссылка на источник:
    https://dev-gang.ru/article/rabota-s-postgresql-v-python-xn8721sq0g/'''