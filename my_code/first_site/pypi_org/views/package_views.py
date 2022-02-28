import flask

from infrastructure.view_modifiers import response
import services.package_service

blueprint = flask.Blueprint('packages',__name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
  return "Package details for {}".format(package_name)

#Using flask you can add typing into the url!
@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def popular(rank: int):
  return "The details for the {}th most popular package".format(rank)