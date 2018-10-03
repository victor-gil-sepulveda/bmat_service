import json
import urllib2
from bmatservice.model.common import set_limit_into_range, Constants


class ReleaseGroup:

    def __init__(self, artist_bmat_id):
        self.artist_bmat_id = artist_bmat_id
        self.release_group_data = []

    def add_releases_from_url(self, offset, limit):


    def get(self, offset=0, limit=50):
        """
        Obtains the release group data using bmat API.
        API limit defaults to 25 and can be max 100, in our case limit is >=50, <=150.
        It will not throw any error.
        """
        # Reset internal data
        self.release_group_data = []

        corrected_limit = set_limit_into_range(limit,
                                               Constants.RELEASE_GROUP_MIN_LIMIT,
                                               Constants.RELEASE_GROUP_MAX_LIMIT)

        api_call_url = Constants.BASE_API_URL + Constants.RELEASE_GROUP_QUERY.format(
            artist_id=self.artist_bmat_id
        )
        print api_call_url
        json_contents = urllib2.urlopen(api_call_url).read()
        print json_contents

        self.release_group_data = json.loads(json_contents)
        #HTTPError: HTTP Error 404: Not Found
        # or contains "error" key