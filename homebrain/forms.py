from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import EqualTo, InputRequired, Length
from wtforms.fields.html5 import DateField, DecimalField, IntegerField


class RegisterForm(FlaskForm):
    name = StringField('Podaj imie', validators=[InputRequired()], render_kw={"placeholder": "Imie"})
    password = PasswordField('Podaj hasło', validators=[InputRequired(), EqualTo('confirm',
                                                                                 message='Hasła muszą być zgodne')],
                             render_kw={"placeholder": "Hasło"})
    confirm = PasswordField('Powtórz hasło', render_kw={"placeholder": "Powtórz hasło"})


class LoginForm(FlaskForm):
    name = StringField('Podaj imie', validators=[InputRequired()], render_kw={"placeholder": "Imie"})
    password = PasswordField('Podaj hasło', validators=[InputRequired()], render_kw={"placeholder": "Hasło"})


class AddItemForm(FlaskForm):
    category = SelectField('Kategoria', choices=[('Wydatek', 'Wydatek'), ('Przychod', 'Przychód')],
                           validators=[InputRequired()])
    name = StringField('Nazwa', validators=[InputRequired(), Length(max=10)], render_kw={"placeholder": "Nazwa"})
    value = DecimalField('Wartość', places=2, validators=[InputRequired()], render_kw={"placeholder": "Wartość"})
    date = DateField('Data', validators=[InputRequired()])


class EditItemForm(FlaskForm):
    id = IntegerField('ID', validators=[InputRequired()])
    name = StringField('Nazwa', validators=[InputRequired(), Length(max=10)])
    value = DecimalField('Wartość', places=2, validators=[InputRequired()])
    date = DateField('Data', validators=[InputRequired()])


class DeleteItemForm(FlaskForm):
    id = IntegerField('ID', validators=[InputRequired()])
