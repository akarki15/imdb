""" Create app object. Do high level stuff """
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_object('config')
# import module

from app.rating_list.controllers import rating_list as rating_list

app.register_blueprint(rating_list)

@app.errorhandler(404)
def not_found(error):
    """ Set up 404 page """
    print url_for('rating_list.home')
    return render_template('404.html'), 404



