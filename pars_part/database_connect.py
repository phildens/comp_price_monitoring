from parser_part import site_checker
import sqlite3
import psycopg2
import time


def getinfo_bd(cur, conn):
    pass

def create_tables(cur, conn):
    table_cheecker = cur.execute('''SELECT * FROM INFORMATION_SCHEMA.TABLES
                                        WHERE TABLE_NAME = 'models';''')
    print(cur.rowcount)
    if cur.rowcount == 0:
        print('notable created')
    else:
        print('deleted db')
            
    cur.execute('DROP TABLE IF EXISTS public.models')
    cur.execute("""
                    CREATE TABLE public.models (id SERIAL PRIMARY KEY ,
                    name_model VARCHAR(255),
                    price INTEGER)""")

    conn.commit()
    #print(listOfTables[0][1])

def db_adder(cur, conn, models):
    for i in models:
        cur.execute("""INSERT INTO models(name_model, price)
        VALUES(%s, %s);
        """,i)
    conn.commit()


def add_models_to_db():
    site_info = site_checker()
    file_with_models = open('all_models.txt','r')
    models = file_with_models.readline().split(',')

    checked_models = []
    for i in site_info.price_list:
        if i[0] in models and not(i[0] in checked_models):
            checked_models.append(i)
    #print(checked_models)

    unique_models = []
    
    for i in checked_models:
        if not(i[0] in unique_models):
            unique_models.append(i[0])

    all_sorted = []
    for i in unique_models:
        cost = 0
        for a in checked_models:
            if a[0] == i and a[1] > cost:
                cost = a[1]
        all_sorted.append([i, cost])
    print(all_sorted)


    while True:
        try:
            # пытаемся подключиться к базе данных
            conn = psycopg2.connect(dbname='dataholder', user='user0', 
                                password='passwrd', host='localhost', port = '5432')
            print('connectted db')
            break
        except:
            time.sleep(5)
            # в случае сбоя подключения будет выведено сообщение  в STDOUT
            print('Can`t establish connection to database')



    with conn.cursor() as cur:
        create_tables(cur, conn)
        db_adder(cur, conn, all_sorted)


    

#add_models_to_db()

# while True:
#     try:
#         # пытаемся подключиться к базе данных
#         conn = psycopg2.connect(dbname='dataholder', user='user0', 
#                                 password='passwrd', host='localhost', port = '5432')
#         print('connectted db')
#         break
#     except:
#         time.sleep(5)
#         # в случае сбоя подключения будет выведено сообщение  в STDOUT
#         print('Can`t establish connection to database')



# with conn.cursor() as cur:
#     create_tables(cur, conn)
#     db_adder(cur, conn, all_sorted)

#add_models_to_db()
# checked_models = ['iphone', 5300]
# with sqlite3.connect('models_bd.db') as conn:
#         cur = conn.cursor()
#         create_tables(cur, conn)
#         db_adder(cur, conn, checked_models)