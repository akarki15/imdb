from flask import Blueprint
rating_list = Blueprint('rating', __name__, url_prefix = '/rating')

@rating_list.route('/',methods=['GET'])
def home():
        return 'Damn son'

