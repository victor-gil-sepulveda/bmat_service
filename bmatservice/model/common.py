
class Constants:
    BASE_API_URL = "http://musicbrainz.org/ws/2"
    RELEASE_GROUP_QUERY = "/release-group?artist={artist_id}&type=album&fmt=json"
    RELEASE_GROUP_MAX_LIMIT = 150
    RELEASE_GROUP_MIN_LIMIT = 50
    API_RELEASE_GROUP_MAX_LIMIT = 100
    API_RELEASE_GROUP_MIN_LIMIT = 25



def set_limit_into_range(limit, lower, upper):
    """
    "limit" must be inside the "lower" and "upper" range, if not, this function returns
     the lower or upper values.
    """
    return min(max(lower, limit), upper)
