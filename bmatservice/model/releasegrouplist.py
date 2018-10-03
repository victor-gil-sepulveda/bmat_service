import json
import urllib2
from bmatservice.model.common import set_limit_into_range, Constants


class ReleaseGroupList:

    def __init__(self, artist_bmat_id):
        self.artist_id = artist_bmat_id
        self.release_groups = []

    def add_releases_from_url(self, offset, limit):
        """
        The API looks to be very solid when wrong offsets and limits are used (e.g. when offset
        or limit > total count
        """
        api_call_url = Constants.BASE_API_URL + Constants.RELEASE_GROUP_BROWSING_QUERY.format(
            artist_id=self.artist_id,
            offset=offset,
            limit=limit
        )
        print "api call", api_call_url
        json_data_s = urllib2.urlopen(api_call_url).read()
        self.release_groups.extend(json.loads(json_data_s)["release-groups"])

    def get(self, offset=0, limit=50):
        """
        Obtains the release group data using bmat API.
        API limit defaults to 25 and can be max 100, in our case limit is >=50, <=150.
        It will not throw any error.
        """
        # Reset internal data
        self.release_groups = []

        corrected_limit = set_limit_into_range(limit,
                                               Constants.RELEASE_GROUP_MIN_LIMIT,
                                               Constants.RELEASE_GROUP_MAX_LIMIT)
        # TODO send error if wrong offset or limit (must be pos int, mst be in range) return {"error": "blah"}

        query_offset = offset
        query_limit = corrected_limit
        while query_limit > 0:
            self.add_releases_from_url(query_offset, query_limit)
            query_limit -= Constants.API_RELEASE_GROUP_MAX_LIMIT
            query_offset += Constants.API_RELEASE_GROUP_MAX_LIMIT


        #HTTPError: HTTP Error 404: Not Found
        # or contains "error" key