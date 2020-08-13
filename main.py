from flask import request, redirect, make_response, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()
# creamos una lista de pruebas para todo.
todos = ['Buy Coffee', 'Send sale order', 'Get video for webpage']\


# Creando un nuevo comando para test
@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

# manejando errores
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


#creamos una nueva ruta raiz
@app.route('/')
def index():
    #obtenemos la ip del usuario
    user_ip = request.remote_addr
#   usamos make_reponse y redirect a hello
    response = make_response(redirect('/hello'))
    #agregamos la ip del usuario a una cookie
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip #guardamos la variable en una sesion
    #regresamos la respuesta de flask
    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    #obtenemos la ip del usuario desde la cookie
    user_ip = session.get('user_ip')
    username = session.get('username') #obtenemos el username de la sesion
# creamos un contexto para las variables del template
    context = {
        'user_ip':user_ip,
        'todos':todos,
        'username': username
    }
    return render_template('hello.html', **context)