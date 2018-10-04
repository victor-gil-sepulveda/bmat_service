from bmatservice.model.releasegrouplist import ReleaseGroupList


class ReleaseGroupProcessor:

    @staticmethod
    def go(artist_bmat_id):
        rgroup_list = ReleaseGroupList(artist_bmat_id)
        rgroup_list.get