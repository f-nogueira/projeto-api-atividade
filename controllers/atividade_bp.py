from flask import Blueprint
from flask_restx import Api
from swagger.namespaces import atividade_namespace

atividade_bp = Blueprint('atividade', __name__, url_prefix='/')
api = Api(atividade_bp, title='API Atividades', description='Microserviço de Atividades')

api.add_namespace(atividade_namespace)