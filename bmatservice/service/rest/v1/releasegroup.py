import urllib2
from flask_restful import Resource, abort
from webargs import fields
from webargs.flaskparser import use_args
import json

from bmatservice.model.common import Constants
from bmatservice.model.releasegroupprocessor import ReleaseGroupProcessor

url_args = {
    "artist": fields.String(required=True),
    "offset": fields.Int(default=0, missing=0),
    "limit": fields.Int(default=Constants.RELEASE_GROUP_MIN_LIMIT, missing=Constants.RELEASE_GROUP_MIN_LIMIT),
    "sleep_time": fields.Float(default=1.0, missing=1.0)
}


class ReleaseGroupEndpoint(Resource):

    def __init__(self):
        pass

    @use_args(url_args)
    def get(self, args):
        rgp = ReleaseGroupProcessor()
        results = rgp.get(args["artist"], args["offset"], args["limit"], args["sleep_time"])
        return results
