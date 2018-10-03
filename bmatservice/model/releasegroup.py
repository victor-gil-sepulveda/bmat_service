import json
import urllib2

from bmatservice.model.common import Constants


class ReleaseGroup:

    def __init__(self, rgroup_bmat_id):
        self.rgroup_id = rgroup_bmat_id
        self.data = {}

    def get(self):
        api_call_url = Constants.BASE_API_URL + Constants.RELEASE_GROUP_QUERY.format(
            rgroup_id=self.rgroup_id
        )
        json_data_s = urllib2.urlopen(api_call_url).read()
        self.data = json.loads(json_data_s)
