import urllib2
from flask_restful import Resource, abort
from webargs import fields
from webargs.flaskparser import use_args
import json

example_args = {
    'artist': fields.String(required=True),
    'offset': fields.Int(),
    'limit': fields.Int()
}


class ReleaseGroupEndpoint(Resource):

    def __init__(self):
        pass

    @use_args(example_args)
    def get(self, args):
        print "LOL"
        print args
        xml_contents = urllib2.urlopen("https://musicbrainz.org/ws/2/release-group?artist=410c9baf-5469-44f6-9852-826524b80c61&type=album&fmt=json").read()
        # resp_dict = bf.data(fromstring(xml_contents))
        # print json.dumps(resp_dict)
        print xml_contents
        return {}
        #return urllib2.urlopen(the_path).read()
