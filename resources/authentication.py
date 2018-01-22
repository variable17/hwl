import os



from flask import jsonify, request, make_response
from flask_restful import Resource
from db import db

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, fresh_jwt_required
    )

from models.models import Users



# Creating user
# @app.route('/register', methods=['POST'])
class Register(Resource):
	def post(self):
		data = request.get_json()
		user = Users.query.filter_by(email=data['email']).first()
		if user is not None:
			return make_response(jsonify({'msg': 'email already registered'}), 401)
		try:
			user = Users(email=data['email'], name=data['name'], password=data['password'])
		except:
			return make_response(jsonify({'msg': 'Looks like you forgot a value'}), 401)
		db.session.add(user)
		db.session.commit()

		return make_response(jsonify({'message':'New user created, please login!'}), 201)



# First time login
# @app.route('/login', methods=['POST'])
class Login(Resource):
	def post(self):
		email = request.json['email']
		password = request.json['password']

		user =  Users.query.filter_by(email=email).first()

		if user and user.verify_password(password):
			return make_response(jsonify({
						'access_token': create_access_token(identity=email),
						'refresh_token': create_refresh_token(identity=email)
						}), 200)
		else:
			return make_response(jsonify({'message': 'Bad request'}), 401)



# Refreshing the access_token using refresh_token
# @app.route('/refresh', methods=['POST'])
class Refresh(Resource):
	@jwt_refresh_token_required
	def post(self):
		identity = get_jwt_identity()
		return make_response(jsonify({'access_token': create_access_token(identity=identity, fresh=False)}), 200)



# Checking a required method
# @app.route('/protected', methods=['GET'])
class Protected(Resource):
	@jwt_required
	def get(self):
	    email = get_jwt_identity()
	    return make_response(jsonify({'username': email}), 200)








