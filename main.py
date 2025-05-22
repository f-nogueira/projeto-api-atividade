from flask import Flask
from flask_restx import Api
from database.config import db, init_db
from controllers.atividade_controller import atividade_namespace

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atividades.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    init_db(app)

    api = Api(
        app,
        title='API de Atividades',
        version='1.0',
        description='Microserviço de Atividades',
        doc='/swagger'
    )

    api.add_namespace(atividade_namespace, path='/atividades')

    @app.route('/health')
    def health():
        return {"status": "OK"}, 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5002, debug=True)