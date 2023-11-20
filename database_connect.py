from pars_part.chaeck_site import site_checker
import sqlite3

def create_tables(cur, conn):
    listOfTables = cur.execute(
        "SELECT * FROM sqlite_master WHERE type='table'; ").fetchall()
    print(listOfTables[0][1])
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
# checked_models = []
# for i in site_info.price_list:
#     if i[0] in models and not(i[0] in checked_models):
#         checked_models.append(i)
# print(checked_models)



with sqlite3.connect('models_bd.db') as conn:
    cur = conn.cursor()
    create_tables(cur, conn)
