import json
import os

from flask import Blueprint, jsonify, request

from app.models import Cliente
from app.validators import validar_email, validar_rfc

bp = Blueprint("clientes", __name__)

DATA_FILE = "data/clientes.json"


def cargar_clientes():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_clientes(clientes):
    with open(DATA_FILE, "w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=4)


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@bp.route("/api/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(cargar_clientes())


@bp.route("/api/clientes", methods=["POST"])
def crear_cliente():
    datos = request.json

    if not validar_email(datos["email"]):
        return jsonify({"error": "Email inválido"}), 400

    if not validar_rfc(datos["rfc"]):
        return jsonify({"error": "RFC inválido"}), 400

    clientes = cargar_clientes()

    nuevo = Cliente(
        len(clientes) + 1,
        datos["nombre"],
        datos["email"],
        datos["rfc"],
        datos["telefono"]
    )

    clientes.append(nuevo.to_dict())

    guardar_clientes(clientes)

    return jsonify(nuevo.to_dict()), 201


@bp.route("/api/clientes/<int:id>", methods=["GET"])
def obtener_cliente(id):
    clientes = cargar_clientes()

    for cliente in clientes:
        if cliente["id"] == id:
            return jsonify(cliente)

    return jsonify({"error": "Cliente no encontrado"}), 404


@bp.route("/api/clientes/<int:id>", methods=["DELETE"])
def eliminar_cliente(id):
    clientes = cargar_clientes()

    nuevos = [c for c in clientes if c["id"] != id]

    if len(clientes) == len(nuevos):
        return jsonify({"error": "Cliente no encontrado"}), 404

    guardar_clientes(nuevos)

    return jsonify({"mensaje": "Cliente eliminado"})