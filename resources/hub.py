from flask import request, jsonify, make_response
from flask_restful import Resource
from models.models import Rooms, Hubs

from db import db


class Hub(Resource):
    def get(self, id):
        rooms = Rooms.query.filter_by(hub_id=id).all()
        if len(rooms) > 0:
            rms = []
            for room in rooms:
                rms.append(room.json())
            return make_response(jsonify({'hub_id': id, 'hub_name': room.hub.name, 'rooms': rms}), 200)
        return make_response(jsonify({'msg': 'The hubs is not defined'}), 401)

    def put(self, id):
        hub = Hubs.query.filter_by(id=id).first()
        if hub is None:
            return make_response(jsonify({'msg': 'This hub id is not valid'}), 401)
        data = request.get_json()
        name = data.get('name')
        hub.name = name if name is not None else hub.name
        db.session.add(hub)
        db.session.commit()
        return make_response(jsonify({'msg': 'Hub name changed'}))

    def delete(self, id):
        hub = Hubs.query.filter_by(id=id).first()
        if hub is None:
            return make_response(jsonify({'msg': 'Hub id is not valid'}), 401)
        db.session.delete(hub)
        db.session.commit()
        return make_response(jsonify({'msg': 'Hub is deleted now'}), 200)


class HubList(Resource):
    def get(self):
        return make_response(jsonify({'hubs': [hub.json() for hub in Hubs.query.all()]}), 200)

    def post(self):
        data = request.get_json()
        name = data.get('name')
        if name is None:
            return make_response(jsonify({'msg': 'Some fields are missing'}), 401)
        hub = Hubs(name=name)
        db.session.add(hub)
        db.session.commit()
        return make_response(jsonify({'msg': 'Hub added'}), 201)
