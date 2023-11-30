from parser_part import site_checker
import sqlite3



def getinfo_bd(cur, conn):
    pass

def create_tables(cur, conn):
    listOfTables = cur.execute(
        "SELECT * FROM sqlite_master WHERE type='table'; ").fetchall()
    
    if listOfTables == []:
        print('created')
    
    cur.execute('DROP TABLE IF EXISTS models')


    cur.execute("""
    CREATE TABLE models (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name_model VARCHAR(255),
         price INTEGER)""")

    conn.commit()
    #print(listOfTables[0][1])

def db_adder(cur, conn, models):
    for i in models:
        cur.execute("""INSERT INTO models(name_model, price)
        VALUES(?,?);
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
    with sqlite3.connect('models_bd.db') as conn:
        cur = conn.cursor()
        create_tables(cur, conn)
        db_adder(cur, conn, checked_models)

    

add_models_to_db()

#add_models_to_db()
# checked_models = ['iphone', 5300]
# with sqlite3.connect('models_bd.db') as conn:
#         cur = conn.cursor()
#         create_tables(cur, conn)
#         db_adder(cur, conn, checked_models)