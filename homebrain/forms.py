from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import EqualTo, InputRequired


class RegisterForm(FlaskForm):
    name = StringField('Podaj imie', validators=[InputRequired()], render_kw={"placeholder": "Imie"})
    password = PasswordField('Podaj hasło', validators=[InputRequired(), EqualTo('confirm',
                                                                                 message='Hasła muszą być zgodne')],
                             render_kw={"placeholder": "Hasło"})
    confirm = PasswordField('Powtórz hasło', render_kw={"placeholder": "Powtórz hasło"})
