sk application  initialization for aibrnb clone
"""
from flask import Flask, jsonify, make_response, render_template, url_for
from models import storage
from flask_cors import CORS
from api.v1.views import app_views
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(exception=None):
    """closes current sqlalchemy session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """ Provides a JSON-formatted response with a 404 status code. """
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    """Main function for flask app"""
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
