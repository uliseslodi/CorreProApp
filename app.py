from flask import Flask, render_template, redirect, request

app = Flask("myApp")

competidores = []

@app.route('/')
def pagLista():
    return render_template("index.html", corredores = sorted(competidores, key = lambda i: (i['tiempo'])))

@app.route('/agregar', methods=["GET", "POST"])
def pagAgregar():
    
    if request.method == "POST":
        competidor = {
            'nombre': request.form["name"],
            'tiempo': request.form["number"],
            'carrera': request.form["carrera"]
        }

        competidores.append(competidor)
        return redirect("/")

    return render_template("agregar.html")
    
app.run()   