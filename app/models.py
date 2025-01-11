from app import db
from datetime import datetime, timedelta

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    cpf = db.Column(db.Integer, nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.now)
    
    def calcular_mensagem(self):
        agora = datetime.now()
        diferenca = agora - self.data_cadastro

        if diferenca >= timedelta(days=365):
            return "Inscrito há 1 ano ou mais"
        elif diferenca >= timedelta(days=30):
            return "Inscrito há 1 mês ou mais"
        else:
            return "Recém-inscrito"