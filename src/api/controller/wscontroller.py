import functools

from flask import (
    Blueprint, jsonify, request
)

bp = Blueprint('v1', __name__, url_prefix='/')
