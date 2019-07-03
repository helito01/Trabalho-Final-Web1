from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, SelectField, TextAreaField, DateField, FloatField
from wtforms.validators import DataRequired



from app.models import Role

class AddChampion(FlaskForm):
    name = StringField('Nome do Evento', validators=[DataRequired()] )
    initial_date = DateField('Início do Evento', format="%d/%m/%Y")
    end_date = DateField('Final do Evento', format="%d/%m/%Y")
    awards = FloatField('Valor do prêmio em US$')
    submit = SubmitField('Enviar')

    def validate_end_date(self, field):
        if field.data < self.initial_date.data:
            raise ValidationError('Evento deve terminar depois do seu início')


class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class EditUserForm(FlaskForm):
    username = StringField('Usuário', validators=[
        DataRequired()])
    role = SelectField('Role', coerce=int)
    submit = SubmitField('Enviar')

    def __init__(self, user, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.role.choices = [
            (role.id, role.name) for role in Role.query.order_by(Role.name).all() 
        ]
        self.user = user
        self.username.data = user.username
class RoleForm(FlaskForm):
    name = StringField('Função', validators=[
        DataRequired()
    ])
    submit = SubmitField('Cadastrar')

    def validate_name(self, field):
        role = Role.query.filter_by(name=field.data).first()
        if role:
            raise ValidationError('Função já cadastrada')

class AddComment(FlaskForm):
    comment = TextAreaField('Mensagem')
    submit = SubmitField('Publicar')

