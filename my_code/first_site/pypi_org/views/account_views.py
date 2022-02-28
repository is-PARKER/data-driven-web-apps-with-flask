import flask

from infrastructure.view_modifiers import response

blueprint = flask.Blueprint('account',__name__, template_folder='templates')

#### Index ###

