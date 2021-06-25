import functools

from flask import (
    Blueprint, jsonify, request
)

from src.core.segmenterfactory import SegmenterFactory

factory = SegmenterFactory()
segmenter = factory.getSegmenter()

bp = Blueprint('v1', __name__, url_prefix='/')

@bp.route("/getwords/", methods=["GET", "POST"])
def getWords():
    domains = request.get_json()
    if type(domains) != list:
        return jsonify(error='json should be a list ["hello","keyword"]')
    return jsonify(result=segmenter.getWords(domains))
