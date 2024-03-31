from flask import jsonify
from flask import request
from flask.views import MethodView


class HelloController(MethodView):
    def get(self):
        return jsonify({"status": "ok", "data": None}), 200

    def post(self):
        body = request.get_json(force=True, silent=True)
        return jsonify({"status": "ok", "data": body}), 201

    def put(self):
        return jsonify({"status": "ok", "data": None}), 200

    def patch(self):
        return jsonify({"status": "ok", "data": None}), 200
