from flask import request, jsonify, make_response
from flask_restful import Resource
from models.models import Rooms, Buttons
from flask_jwt_extended import jwt_required

from db import db


class Room(Resource):
    @jwt_required
    def get(self, id):
        buttons = Buttons.query.filter_by(room_id=id).all()
        if len(buttons) > 0:
            btn = []
            for button in buttons:
                btn.append(button.json())
            return make_response(jsonify({'room_id': id, 'room_name': button.room.name, 'buttons': btn}), 200)
        return make_response(jsonify({'msg': 'The room is not defined'}), 401)

    @jwt_required
    def put(self, id):
        room = Rooms.query.filter_by(id=id).first()
        if room is None:
            return make_response(jsonify({'msg': 'Room does not exist'}), 404)
        data = request.get_json()
        name = data.get('name')
        room.name = name
        db.session.add(room)
        db.session.commit()
        return make_response(jsonify({'msg': 'Room name has changed'}), 200)

    @jwt_required
    def delete(self, id):
        room = Rooms.query.filter_by(id=id).first()
        if room is None:
            return make_response(jsonify({'msg': 'No room to begin with'}), 404)
        db.session.delete(room)
        db.session.commit()
        return make_response(jsonify({'msg': 'Room deleted'}), 200)


class RoomList(Resource):
    @jwt_required
    def get(self):
        return make_response(jsonify({'rooms': [room.json() for room in Rooms.query.all()]}), 200)

    @jwt_required
    def post(self):
        data = request.get_json()
        name = data.get('name')
        hub_id = data.get('hub_id')
        if hub_id is None or name is None:
            return make_response(jsonify({'msg': 'Some fields are missing'}), 401)
        room = Rooms(name=name, hub_id=hub_id)
        db.session.add(room)
        db.session.commit()
        return make_response(jsonify({'msg': 'Room added'}), 201)
