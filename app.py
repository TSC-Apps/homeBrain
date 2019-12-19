from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from datetime import date
from werkzeug.security import check_password_hash, generate_password_hash
from homebrain.models import User, Item
from homebrain import app, db, login_manager
from homebrain.forms import RegisterForm, LoginForm, AddItemForm, EditItemForm, DeleteItemForm
from sqlalchemy import extract


# Flask-Login callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/home', methods=['GET', 'POST'])
@login_required
def index():
    add_form = AddItemForm()
    edit_form = EditItemForm()
    delete_form = DeleteItemForm()

    if request.method == 'POST':
        if add_form.validate_on_submit():
            item = Item(category=add_form.category.data, name=add_form.name.data, date=add_form.date.data,
                        value=add_form.value.data, user=current_user)
            db.session.add(item)
            db.session.commit()
        elif edit_form.validate_on_submit():
            item = Item.query.filter_by(id=edit_form.id.data).first()
            item.date = edit_form.date.data
            item.value = edit_form.value.data
            item.name = edit_form.name.data
            db.session.commit()
        elif delete_form.validate_on_submit():
            id = delete_form.id.data
            item = Item.query.get(id)
            if item:
                db.session.delete(item)
                db.session.commit()
        else:
            app.logger.error('FORM NOT VALID')

    current_date = date.today()
    # zabieg mający na celu sprawdzenie czy kazaliśmy filtrować rekordy
    if 'select-months' and 'select-years' in request.args:
        month = request.args['select-months']
        year = request.args['select-years']
        current_date = current_date.replace(month=int(month))
        current_date = current_date.replace(year=int(year))

    # Ogolne wydatki i przychody z danego miesiaca
    content_expenses = Item.query.filter(extract('month', Item.date) == current_date.month).\
        filter(extract('year', Item.date) == current_date.year).filter_by(category='Wydatek').\
        order_by(Item.date.desc()).all()

    content_incomes = Item.query.filter(extract('month', Item.date) == current_date.month).\
        filter(extract('year', Item.date) == current_date.year).filter_by(category='Przychod').\
        order_by(Item.date.desc()).all()

    # bilans miesięczny
    sum_expenses = 0
    for i in content_expenses:
        sum_expenses += i.value

    sum_incomes = 0
    for i in content_incomes:
        sum_incomes += i.value

    # Stan budzetu - bilans calosciowy
    budget_expenses = Item.query.filter_by(category='Wydatek').all()
    budget_incomes = Item.query.filter_by(category='Przychod').all()

    sum_budget_expenses = 0
    if budget_expenses:
        for i in budget_expenses:
            sum_budget_expenses += i.value

    sum_budget_incomes = 0
    if budget_incomes:
        for i in budget_incomes:
            sum_budget_incomes += i.value

    bilance = sum_budget_incomes - sum_budget_expenses

    header_content = ['', 'id', 'nazwa', 'wartość', 'osoba', 'data']

    return render_template('index.html', the_data_expenses=content_expenses, the_data_incomes=content_incomes,
                           sum_inc=round(sum_incomes, 2), sum_exp=round(sum_expenses, 2),
                           final_bil=round(bilance, 2), header_content=header_content, add_form=add_form,
                           edit_form=edit_form, delete_form=delete_form)


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            user = User.query.filter_by(name=name).first()
            if user:
                # Sprawdzenie czy hash i haslo pasuja
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash("Podałeś złe hasło.")
                    return redirect(url_for('index'))
            else:
                flash("Nie ma takiego użytkownika.")

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            if User.query.filter_by(name=name).first():
                flash('Taki użytkownik już istnieje')
            else:
                password = generate_password_hash(form.password.data)
                user = User(name=name, password=password)
                db.session.add(user)
                db.session.commit()
                flash('Stworzono nowego użytkownika')

    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
