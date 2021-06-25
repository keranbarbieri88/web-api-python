from src.model.challenged import Challenged
from src.app.server import app
from src.controllers.challengedController import ChallengedController
from src.controllers.response import Answer
from flask import request


@app.route("/")
def index():
    return "Hello Jillian!!"


@app.route("/challenged/", methods=["GET"])
def get_challenged():
    dados = ChallengedController.get(Challenged)
    return Answer.newResponse(200, dados, "Sucesso")


@app.route("/challenged/<id>", methods=["GET"])
def get_challengedo_id(id):
    dados = ChallengedController.get_id(id)
    return Answer.newResponse(200, dados, "Sucesso")


@app.route("/challenged/", methods=["POST"])
def create_challenged():
    body = request.get_json()
    dados = ChallengedController.create(body)
    return Answer.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])


@app.route("/challenged/<id>", methods=["PUT"])
def update_challenged(id):
    body = request.get_json()
    dados = ChallengedController.update(id, body)
    return Answer.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])


@app.route("/challenged/<id>", methods=["DELETE"])
def delete_challenged(id):
    dados = ChallengedController.delete(id)
    return Answer.newResponse(dados["status"], dados["conteudo"], dados["mensagem"])


# if __name__ == "__main__":
#     app.run()
