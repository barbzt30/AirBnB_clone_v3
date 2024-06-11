#!/usr/bin/python3
"""Place amenities views"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.amenity import Amenity
import os


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_all_amenities(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenities = [data.to_dict() for data in place.amenities]
    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def place_delete_amenity(place_id, amenity_id):
    """Deletes an amenity object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    place.amenities.remove(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def place_post_amenity(place_id, amenity_id):
    """Creates amenity object by id"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200
    place.amenities.append(amenity)
    return jsonify(amenity.to_dict()), 201
