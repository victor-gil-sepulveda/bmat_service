import json
import urllib2
from bmatservice.model.common import Constants


class ReleaseGroup:
    """
    "Tool class" to obtain and store the data from a release
    """

    def __init__(self, rgroup_bmat_id):
        self.rgroup_id = rgroup_bmat_id
        self.data = {}

    def get(self):
        api_call_url = Constants.BASE_API_URL + Constants.RELEASE_GROUP_QUERY.format(
            rgroup_id=self.rgroup_id
        )
        print api_call_url
        json_data_s = urllib2.urlopen(api_call_url).read()
        self.data = json.loads(json_data_s)

    def __getitem__(self, key):
        return self.data[key]
