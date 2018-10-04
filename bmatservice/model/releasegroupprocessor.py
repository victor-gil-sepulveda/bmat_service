from urllib2 import HTTPError

import time

from bmatservice.model.releasegroup import ReleaseGroup
from bmatservice.model.releasegrouplist import ReleaseGroupList


def process_year(year_string):
    return year_string


class ReleaseGroupProcessor:

    @staticmethod
    def get(artist_bmat_id, offset, limit, sleep_time=1.0):
        results = {"albums": []}

        # Note that the API is robust to limit and offset values > object count and (it looks like)
        # values outside the range [25, 100] for the limit.
        if not isinstance(offset, int) or not isinstance(limit, int) or offset < 0 or limit < 0:
            return {"error": "offset and limit must be positive integers"}

        try:
            rgroup_list = ReleaseGroupList(artist_bmat_id)
            rgroup_list.get(offset, limit)

            for i in range(len(rgroup_list)):
                rgroup = ReleaseGroup(rgroup_list[i]["id"])
                rgroup.get()
                results["albums"].append(
                    {
                        "id": rgroup["id"],
                        "title": rgroup["title"],
                        "year": process_year(rgroup["first-release-date"]),
                        "release_count": len(rgroup["releases"])
                    }
                )
                time.sleep(sleep_time)

        except RuntimeError, e: # (api error etc)
            return {"error": str(e)}

        except HTTPError, e: # url get errors
            return {"error": "HttpError - code: {code}; reason: {reason}".format(code=e.code, reason=e.reason)}

        return results
