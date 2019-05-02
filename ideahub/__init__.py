from flask import Flask, Blueprint

app = Flask(__name__)

app.config.from_pyfile('config.py')

from ideahub.users.views import users
from ideahub.topic.views import topic
from ideahub.ideas.views import ideas

app.register_blueprint(users)
app.register_blueprint(topic)
app.register_blueprint(ideas)

