"""  Handles routing for rating_list path """
from flask import Blueprint, render_template
from config import OUTPUT_FILE
from scripts.prepare import read_dump, print_ratings

rating_list = Blueprint('rating_list', __name__, url_prefix='/rating_list')

@rating_list.route('/', methods=['GET'])
def home():
    """ Render the list of movies and imdb scores """
    lst = read_dump(OUTPUT_FILE)
    lst = decode_list(lst)
    print_ratings(OUTPUT_FILE)
    return render_template('rating.html', lst=lst)

def decode_list(lst):
	for i in range (1, len(lst)):
		lst[i][0] = lst[i][0].decode('utf_8')
		lst[i][1] = lst[i][1].decode('utf_8')
	return lst


