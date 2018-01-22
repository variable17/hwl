import os	
from datetime import timedelta


from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager



from resources.cennet import Cennet, CennetList
from resources.room import Room, RoomList
from resources.button import Button, ButtonList
from resources.hub import Hub, HubList

from resources.authentication import Register, Login, Refresh, Protected

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'fgnoignvoghorihgnonvznn874fiv98u'


app.config['JWT_SECRET_KEY'] = 'kuiciryn9 8fhromf8rh oirzo8gnyhghn8gy'
# Dynamically defining the expiration time, default time is 15 minute for access-token
# and 30 day for the refresh token.
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
# app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta


from db import db
db.init_app(app)
	
jwt = JWTManager(app)

api = Api(app)

# Login check
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Refresh, '/refresh')
api.add_resource(Protected, '/protected')



# other resources check
api.add_resource(Room, '/rooms/<int:id>')
api.add_resource(RoomList, '/rooms')
api.add_resource(Button, '/buttons/<int:id>')
api.add_resource(ButtonList, '/buttons')
api.add_resource(Cennet, '/cennets/<int:id>')
api.add_resource(CennetList, '/cennets')
api.add_resource(Hub, '/hubs/<int:id>')
api.add_resource(HubList, '/hubs')


if __name__ == '__main__':
	app.run(debug=True)