import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(user='solaris',
                            password='solaris',
                            #host='192.168.98.157',
                            host='95.80.93.177',
                            port="5432",
                            dbname='test',)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()
    #sql_create_database = 'create database postgres_db'
    #cursor.execute(sql_create_database)

    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(conn.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")



    # # Создайте курсор для выполнения операций с базой данных
    # cursor = conn.cursor()
    # # SQL-запрос для создания новой таблицы
    # create_table_query = '''CREATE TABLE mobile
    #                       (ID INT PRIMARY KEY     NOT NULL,
    #                       MODEL           TEXT    NOT NULL,
    #                       PRICE         REAL); '''
    # # Выполнение команды: это создает новую таблицу
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("Таблица успешно создана в PostgreSQL")


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL\n", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")