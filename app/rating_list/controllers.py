from flask import Blueprint
import  os
from config import STATIC

rating_list = Blueprint('rating', __name__, url_prefix = '/rating') 

@rating_list.route('/',methods=['GET'])
def home():
        str = ""
        with open(os.path.join(STATIC, 'movies.csv')) as file:
             str = ''.join ([str, file.read()])
        return str

