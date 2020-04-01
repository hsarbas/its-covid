""" Minimal web app using Flask """

from flask import Flask, render_template
# from app.model.database.db import Database
from app.model.database.api import Database


db = Database()
app = Flask(__name__, static_folder='./view/static', template_folder='./view/templates')


@app.route('/')
def index():
    """
    Default landing page
    
    :return:
    """

    records = db.get_all_records()
    markers = []
    for record in records:
        attributes = record['attributes']
        markers.append([attributes['latitude'], attributes['longitude']])
    return render_template('index.html', markers=markers)


@app.errorhandler(404)
def page_not_found(error):
    """
    Customized Error 404 page.

    :param error:
    :return:
    """
    return render_template('404.html'), 404


""" Starting point of program"""
if __name__ == '__main__':
    app.run()
