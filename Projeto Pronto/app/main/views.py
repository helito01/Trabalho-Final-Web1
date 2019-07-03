from flask import flash, redirect, render_template, session, url_for
from flask_login import login_required
from sqlalchemy.exc import IntegrityError


from app import db
from app.models import Role, User, Champions

from . import main
from .forms import NameForm, RoleForm, EditUserForm, AddComment, AddChampion


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')


@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

@main.route('/noticia1')
def not1():
    return render_template('not1.html')


@main.route('/noticia2')
def not2():
    form = AddComment()
    return render_template('not2.html', form=form)


@main.route('/adicionar_campeonato', methods=['GET', 'POST'])
def add_champion():
    champions = Champions.query.all()
    form = AddChampion()
    if form.validate_on_submit():
        new_champion = Champions()
        new_champion.name = form.name.data
        new_champion.initial_date = form.initial_date.data
        new_champion.end_date = form.end_date.data
        new_champion.awards = form.awards.data
        db.session.add(new_champion)
        db.session.commit()
        flash('Novo campeonato cadastrado.')
        return redirect(url_for('main.champions'))
    return render_template('add_champion.html', champions=champions, form=form)


@main.route('/noticia4')
def not4():
    return render_template('not4.html')

    
@main.route('/noticia5')
def not5():
    return render_template('not5.html')


@main.route('/noticia6')
def not6():
    return render_template('not6.html')


@main.route('/admin')
@login_required
def admin():
    return render_template('venv/flask_admin/bootstrap2/index.html')
    
    
@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) 


@main.route('/user/list', methods=['GET', 'POST'])

def list_user():
    users = User.query.all()
    return render_template('list_user.html', users=users)




@main.route('/role/add', methods=['GET', 'POST'])

def add_role():
    form = RoleForm()
    roles = Role.query.all()
    if form.validate_on_submit():
        new_role = Role()
        new_role.name = form.name.data
        db.session.add(new_role)
        db.session.commit()

        flash('Função cadastrada com sucesso.')
        return redirect(url_for('main.index'))
    return render_template('add_role.html', form=form, roles=roles)


@main.route('/edit-user/<int:id>', methods=['GET', 'POST'])

def edit_user(id):
    user = User.query.filter_by(id=id).first()
    form = EditUserForm(user)
    return render_template('edit_user.html', form=form)



@main.route('/campeonatos', methods=['GET', 'POST'])
def champions():
    champions = Champions.query.all()
    form = AddChampion()
    if form.validate_on_submit():
        new_champion = Champions()
        new_champion.name = form.name.data
        new_champion.initial_date = form.initial_date.data
        new_champion.end_date = form.end_date.data
        new_champion.awards = form.awards.data
        db.session.add(new_champion)
        db.session.commit()
        flash('Novo campeonato cadastrado.')
        return redirect(url_for('main.champions'))
    return render_template('champions.html', champions=champions, form=form)
    

