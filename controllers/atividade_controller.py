from flask import request
from flask_restx import Resource
from services.atividade_service import AtividadeService
from swagger.namespaces import atividade_namespace, atividade_response_model, atividade_model


@atividade_namespace.route('/')
class ListaAtividades(Resource):
    @atividade_namespace.doc('listar_atividades')
    @atividade_namespace.param('professor_id', 'ID do professor')
    @atividade_namespace.marshal_list_with(atividade_response_model)
    def get(self):
        """
        Lista todas as atividades, podendo filtrar pelo ID do professor.
        """
        professor_id = request.args.get('professor_id', type=int)
        atividades = AtividadeService.listar_atividades(professor_id)
        return [atividade.to_dict() for atividade in atividades]

    @atividade_namespace.doc('criar_atividade')
    @atividade_namespace.expect(atividade_model, validate=True)
    @atividade_namespace.marshal_with(atividade_response_model, code=201)
    def post(self):
        """
        Cria uma nova atividade vinculada a um professor.
        """
        dados = request.get_json()
        try:
            atividade = AtividadeService.criar_atividade(dados)
            return atividade.to_dict(), 201
        except Exception as e:
            atividade_namespace.abort(400, f"Erro ao criar atividade: {str(e)}")