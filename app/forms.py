from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# haciendo el formulario de Login
class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')

class TodoForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submint = SubmitField('Create')