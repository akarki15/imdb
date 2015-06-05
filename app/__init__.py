from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from app.rating_list.controllers import rating_list as rating_list

# import module
app.register_blueprint(rating_list)

@app.errorhandler(404)
def not_found(error):
       return render_template('404.html'), 404


