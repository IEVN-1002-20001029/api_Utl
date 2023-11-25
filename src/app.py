from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

@app.route('/')
def index():
    grupo="IEVN 1002"
    lista= ["IEVN 1001" , "IEVN 1002" , "IEVN 1003"]
    return render_template('index.html', grupo=grupo, lista=lista)

@app.route('/hola')
def hola():
  
    return "Saludo utl"

@app.route('/user/<string:nombre>')
def user(nombre):
    return 'saludo {0}'.format(nombre)

@app.route('/numero/<int:n1>')
def nummero(n1):
    return 'El numero es : {}'.format(n1)

@app.route('/user/<int:id>/<string:nom>')
def user1(id ,nom):
    return 'ID: {} NOMBRE: {}'.format(id,nom)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1 ,n2):
    return 'La suma es : {}'.format(n1+n2)

@app.route('/default')
@app.route('/default/<string:dd>')
def default(dd='fulano'):
    return "<h1> El nombre es : {} </h1>".format(dd)

@app.route('/Alumnos')
def Alumnos():
    return render_template('Alumnos.html')





if __name__=="__main__":
    app.run(debug=True)


