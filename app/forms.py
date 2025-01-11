from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import Length, Email, DataRequired
from app.models import Cliente
from datetime import datetime

class CadastroForm(FlaskForm):
    nome = StringField("Nome do Cliente: ", validators=[DataRequired()])
    email = StringField("Email do Cliente: ", validators=[DataRequired(), Email()])
    idade = StringField("Idade do Cliente: ", validators=[DataRequired()])
    numero = StringField("Número do Cliente: ", validators=[Length(min=10, max=11), DataRequired()])
    cpf = StringField("CPF do Cliente: ", validators=[DataRequired(), Length(min=10, max=11)])
    Submit = SubmitField("Registrar Cliente")

    def save(self):
        add = Cliente(
            nome=self.nome.data,
            email=self.email.data,
            idade=self.idade.data,
            numero=self.numero.data,
            cpf=self.cpf.data
        )
        db.session.add(add)
        db.session.commit()
