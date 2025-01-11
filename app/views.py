from datetime import datetime
from app import app, db
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user, login_user, logout_user, LoginManager
from app import bcrypt
from app.models import Cliente
import os
from app.forms import CadastroForm


@app.route('/', methods=['GET', 'POST'])
def indexPage():
    clientes = Cliente.query.all()
    return render_template('index.html', clientes=clientes)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastroPage():
    form = CadastroForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('indexPage'))

    clientes = Cliente.query.all()
    return render_template('cadastro.html', form=form)

@app.route('/cliente/<int:cliente_id>', methods=['GET'])
def detalhes_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    return render_template('detalhes.html', cliente=cliente)