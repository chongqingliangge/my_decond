from flask import Blueprint

index_blu = Blueprint('index_blu', __name__, template_folder='templates', static_folder='static', url_prefix='/index')
from . import index, view
