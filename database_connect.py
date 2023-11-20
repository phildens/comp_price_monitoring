from pars_part.chaeck_site import site_checker
import sqlite3

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

#site_info = site_checker()
file_with_models = open('all_models.txt','r')
models = file_with_models.readline().split(',')
checked_models = []
# for i in site_info.price_list:
#     if i[0] in models and not(i[0] in checked_models):
#         checked_models.append(i)
# print(checked_models)

checked_models = []

with sqlite3.connect('models_bd.db') as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
         name_model VARCHAR(255),
         price INTEGER)""")
    if checked_models != []:
        cur.execute("""DELETE FROM models""")
        conn.commit()
        print('deleted')
        for i in checked_models:
            cur.execute("""INSERT INTO models(name_model, price) VALUES(?,?)""", i)
            print(i)
    data = cur.execute("""SELECT * FROM models group by name_model""").fetchall()
    print(data)
    #if data == []:


    conn.commit()
