from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",fila=8,columna=8,background = "black", color = "red")

@app.route('/<int:numero>')
def task2(numero):
    return render_template("index.html",fila=numero,columna=8,background = "black", color = "red")

@app.route('/<int:x>/<int:y>')
def task3(x,y):
    return render_template("index.html",fila=x,columna=y,background = "black", color = "red")

@app.route('/<int:x>/<int:y>/<string:bg>')
def task4(x,y,bg):
    return render_template("index.html",fila=x,columna=y,background = bg, color = "red")

@app.route('/<int:x>/<int:y>/<string:bg>/<string:c>')
def task5(x,y,bg,c):
    return render_template("index.html",fila=x,columna=y,background = bg, color = c)

if __name__=="__main__":
    app.run(debug=True)