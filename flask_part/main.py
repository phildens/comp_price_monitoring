from flask import Flask, render_template
import sqlite3

class model:
    def __init__(self, modele, coste):
        self.model = modele
        self.cost = str(int(coste * 1.25))
        self.realcost = coste

def connect_users():
    info_from_bd = []
    while len(info_from_bd) == 0:
        try:
            with sqlite3.connect('databas/models_bd.db') as conn:
                cur = conn.cursor()
                info_from_bd = cur.execute("""
                SELECT * FROM models;
                """).fetchall()
        except:
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