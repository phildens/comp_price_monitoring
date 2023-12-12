from flask import Flask, render_template
import sqlite3
import psycopg2
import time
class model:
    def __init__(self, modele, coste):
        self.model = modele
        self.cost = str(int(coste * 1.25))
        self.realcost = coste

def connect_users():
    while True:
        try:
            # пытаемся подключиться к базе данных
            conn = psycopg2.connect(dbname='dataholder', user='user0', 
                                    
                                password='passwrd', host='postgres', port = '5432')
            print('connectted db')
            break
        except:
            time.sleep(5)
            # в случае сбоя подключения будет выведено сообщение  в STDOUT
            print('Can`t establish connection to database')
    info_from_bd = []
    while len(info_from_bd) == 0:
        try:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM public.models;""")
                info_from_bd = cur.fetchall()
            if len(info_from_bd) == 0:
                time.sleep(10)
        
        except:
            time.sleep(10)
            pass
        
        
    print(info_from_bd)

    
    phone = []
    for i in info_from_bd:
        one_model = model(i[1], i[2])
        phone.append(one_model)
        

    print("запрос выполнен")
    return phone
    

app = Flask("site_services")

@app.route('/')
def hello():
    phone = connect_users()
    return render_template('place.html', iphones = phone)

app.run(host='0.0.0.0')