from flask import request, jsonify, make_response
from flask_restful import Resource
from models.models import *

from db import db


class Button(Resource):
	def get(self, id):
		button = Buttons.query.filter_by(id=id).first()
		if button is None:
			return make_response(jsonify({'msg': 'No button by this id'}), 404)
		return make_response(jsonify(button.json()), 200)


	def put(self, id):
		button = Buttons.query.filter_by(id=id).first()
		if button is None:
			return make_response(jsonify({'msg': 'No button by this id'}), 404)
		data = request.get_json()
		name = data.get('name')
		power = data.get('power')
		
		if button.button_type == 'relay':
			# rd_id = data.get('relay_id')
			rd_id = button.rd_id

			if power is None or rd_id is None:
				return make_response(jsonify({'msg': 'Some field missing'}), 401)
		else:
			# rd_id = data.get('dimmer_id')
			rd_id = button.rd_id
			intensity = data.get('intensity')
			if power is None or rd_id is None or intensity is None:
				return make_response(jsonify({'msg': 'Some field missing'}), 401)


		button.name = name if name else button.name
		button.power = power
		if button.button_type == 'dimmer':
			button.intensity = intensity
		db.session.add(button)
		db.session.commit()
		if button.button_type == 'relay':
			relay = Relays.query.filter_by(relay_id=rd_id).first()
			relay.power = power
			db.session.add(relay)
			db.session.commit()
			return make_response(jsonify({'msg': 'Value changed'}), 200)
		else:
			dimmer = Dimmers.query.filter_by(dimmer_id=rd_id).first()
			dimmer.power = power
			dimmer.intensity = intensity
			db.session.add(dimmer)
			db.session.commit()
			return make_response(jsonify({'msg': 'Value changed'}), 200)
			

	def delete(self, id):
		button = Buttons.query.filter_by(id=id).first()
		if button is None:
			return make_response(jsonify({'msg': 'Button does not exists'}), 401)
		db.session.delete(button)
		db.session.commit()
		return make_response(jsonify({'msg': 'Button deleted'}), 200)



class ButtonList(Resource):
	def get(self):
		return make_response(jsonify({'buttons': [button.json() for button in Buttons.query.all()]}), 200)


	def post(self):
		data = request.get_json()
		name = data.get('name')

		button_type = data.get('button_type')
		room_id = data.get('room_id')

		# daedadada
		ip_address = data.get('ip_address')

		if button_type == 'relay':
			rd_id = data.get('relay_id')
			# power = data.get('power')
			power = False
			if name is None or button_type is None or room_id is None or ip_address is None or rd_id is None or power is None:
				return make_response(jsonify({'msg': 'some fields are messing'}), 401)
		elif button_type == 'dimmer':
			rd_id = data.get('dimmer_id')
			# power = data.get('power')
			power = False
			# intensity = data.get('intensity')
			intensity = 0
			if name is None or button_type is None or room_id is None or ip_address is None or rd_id is None or power is None or intensity is None:
				return make_response(jsonify({'msg': 'some fields are missing'}), 401)
		else:
			return make_response(jsonify({'msg': 'button_type is not as specified'}), 401)


		button = Buttons.query.filter_by(rd_id=rd_id, button_type=button_type).first()
		if button is not None:
			return make_response(jsonify({'msg': 'Button already exists'}), 401)


		if button_type == 'relay':
			button = Buttons(name=name, button_type=button_type, room_id=room_id, power=power, rd_id=rd_id, ip_address=ip_address)
			db.session.add(button)
			db.session.commit()
			return make_response(jsonify({'msg': 'Button added'}), 201)
		button = Buttons(name=name, button_type=button_type, room_id=room_id, power=power, intensity=intensity ,rd_id=rd_id, ip_address=ip_address)
		db.session.add(button)
		db.session.commit()
		return make_response(jsonify({'msg': 'Button added'}), 201)	




