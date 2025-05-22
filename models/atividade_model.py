import requests
from database.config import db

class Atividade(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String)
    professor_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        professor_data = {"id": None, "nome": None}
        try:
            response = requests.get(f'http://localhost:5000/professores/{self.professor_id}')
            if response.status_code == 200:
                json_response = response.json()
                professor = json_response.get("data", {})
                professor_data = {
                    "id": professor.get("id"),
                    "nome": professor.get("nome")
                }
        except Exception:
            pass

        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "professor": professor_data
        }