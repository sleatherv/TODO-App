from flask import Flask, request, redirect, make_response, render_template, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

# Inicializamos bootstrap
bootstrap = Bootstrap(app)
# csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'SUPER SECRETO'


# creamos una lista de pruebas para todo.
todos = ['Buy Coffee', 'Send sale order', 'Get video for webpage']\

# haciendo el formulario de Login
class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


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
    login_form = LoginForm()
    username = session.get('username') #obtenemos el username de la sesion
# creamos un contexto para las variables del template
    context = {
        'user_ip':user_ip,
        'todos':todos,
        'login_form': login_form,
        'username': username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data #obtenemos el username
        session['username']= username #lo guardamos en la sesion para enviarlo al contexto

        return redirect(url_for('index'))
    # rendereamos el template con las variables que se requieran desde el contexto
    return render_template('hello.html', **context)