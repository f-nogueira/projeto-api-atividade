from models.atividade_model import Atividade
from database.config import db


class AtividadeService:
    @staticmethod
    def criar_atividade(dados):
        atividade = Atividade(
            titulo=dados['titulo'],
            descricao=dados.get('descricao', ''),
            professor_id=dados['professor_id']
        )
        db.session.add(atividade)
        db.session.commit()
        return atividade

    @staticmethod
    def listar_atividades(professor_id=None):
        query = Atividade.query
        if professor_id:
            query = query.filter_by(professor_id=professor_id)
        return query.all()