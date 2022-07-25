from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

clientes = []


@app.route("/clientes/cadastro", methods=['POST'])
def cadastrar():
    user_cliente = request.json
    for user in clientes:
        if user["nome"] == user_cliente["nome"] and user["numero"] == user_cliente["numero"]:
            return {"status": "Cliente já existe."}
    user_cliente = {
        "id": str(uuid.uuid4()),
        "nome": user_cliente["nome"],
        "numero": user_cliente["numero"]
    }
    clientes.append(user_cliente)
    return jsonify(user_cliente)


@app.route("/listar/clientes")
def listar_clientes():
    return jsonify(clientes)


@app.route("/entrada/contato", methods=['POST'])
def comunicação():
    fidelizar = request.json
    for contato in clientes:
        if contato["nome"] == fidelizar["nome"] and contato["numero"] == fidelizar["numero"]:
            return{"ligação": "realizada."}
        else:
            return{"Status": "numero Incorretos."}


@app.route("/excluir/clientes", methods=['POST'])
def excluir_clientes():
    excluir = request.json
    print(clientes)
    for list in clientes:
        if list["id"] == excluir["id"]:
            clientes.remove(list)
            return excluir


remedios = []


@app.route("/drogaria", methods=['POST'])
def drogaraia():
    comprimidos = request.json
    for remedios_liquido in remedios:
        if remedios_liquido["remedio"] == comprimidos["remedio"]:
            return {"status": "Produto já cadastrado."}
    comprimidos = {
        "id": str(uuid.uuid4()),
        "remedio": comprimidos["remedio"]
    }
    remedios.append(comprimidos)
    return jsonify(comprimidos)


@app.route("/listar/remedios")
def listar_remedios():
    return jsonify(remedios)


@app.route("/excluir/remedios", methods=['POST'])
def excluir_produto():
    body_excluir = request.json
    print(remedios)
    for estoque in remedios:
        if estoque["id"] == body_excluir["id"]:
            remedios.remove(estoque)
            return body_excluir


app.run()
