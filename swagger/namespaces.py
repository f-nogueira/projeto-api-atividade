from flask_restx import Namespace, fields

atividade_namespace = Namespace('atividades', description='Operações relacionadas às atividades')

professor_model = atividade_namespace.model('Professor', {
    'id': fields.Integer(required=True, description='ID do professor'),
    'nome': fields.String(required=True, description='Nome do professor'),
})

atividade_model = atividade_namespace.model('Atividade', {
    'titulo': fields.String(required=True, description='Título da atividade'),
    'descricao': fields.String(description='Descrição da atividade'),
    'professor_id': fields.Integer(required=True, description='ID do professor associado'),
})

atividade_response_model = atividade_namespace.model('AtividadeResponse', {
    'id': fields.Integer(required=True, description='ID da atividade'),
    'titulo': fields.String(required=True, description='Título da atividade'),
    'descricao': fields.String(description='Descrição da atividade'),
    'professor': fields.Nested(professor_model, description='Dados do professor vinculado'),
})