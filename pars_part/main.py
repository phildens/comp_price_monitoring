from flask import Flask, render_template
import sqlite3

class model:
    def __init__(self, modele, coste) -> None:
        self.model = modele
        self.cost = str(int(coste * 1.25))
        self.realcost = coste

with sqlite3.connect('models_bd.db') as conn:
    cur = conn.cursor()
    info_from_bd = cur.execute("""
    SELECT * FROM models;
    """).fetchall()
    
print(info_from_bd)

phone = []

for i in info_from_bd:
    one_model = model(i[1], i[2])
    phone.append(one_model)
    print(one_model.model, one_model.cost)

app = Flask("site_services")

@app.route('/')
def hello():
    return render_template('place.html', iphones = phone)

app.run()