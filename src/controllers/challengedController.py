from src.app.server import db
from src.model.challenged import Challenged


class ChallengedController():

    def get(self):
        challenged = Challenged.query.all()
        dados = [Challenged.to_json() for Challenged in challenged]
        return dados

    def get_id(id):
        challenged = Challenged.query.filter_by(id=id).first()
        dados = challenged.to_json()
        return dados

    def create(body):
        try:
            challenged = Challenged(
                id=body["id"],
                name=body["name"],
                area=body["area"],
                hard_skills=body["hard_skills"]
            )
            db.session.add(challenged)
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }

    def update(id, body):
        challenged = Challenged.query.filter_by(id=id).first()
        try:
            challenged.id = body["id"]
            challenged.name = body["name"]
            challenged.area = body["area"]
            challenged.hard_skills = body["hard_skills"]
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }

    def delete(id):
        challenged = Challenged.query.filter_by(id=id).first()
        try:
            db.session.delete(challenged)
            db.session.commit()
            return {
                "status": 201,
                "conteudo": {},
                "mensagem": "Sucesso"
            }
        except Exception as e:
            return {
                "status": 400,
                "conteudo": {},
                "mensagem": "Erro"
            }
