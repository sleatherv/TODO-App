from flask import Flask, request, redirect, make_response

app = Flask(__name__)

#creamos una nueva ruta raiz
@app.route('/')
def index():
    #obtenemos la ip del usuario
    user_ip = request.remote_addr
#   usamos make_reponse y redirect a hello
    response = make_response(redirect('/hello'))
    #agregamos la ip del usuario a una cookie 
    response.set_cookie('user_ip', user_ip)
    #regresamos la respuesta de flask
    return response


@app.route('/hello')
def hello():
    #obtenemos la ip del usuario desde la cookie
    user_ip = request.cookies.get('user_ip')
    return f'Hello World Flask, tu IP es {user_ip}'