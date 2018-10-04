import json
import unittest
import os
import bmatservice.model.test.data as data
from bmatservice.model.common import Constants
from bmatservice.model.releasegrouplist import ReleaseGroupList


class TestReleaseGroup(unittest.TestCase):

    def test_get(self):
        """
        Uses the api (we should use a mock here!) in order to check if the data is being
        retrieved properly.
        """
        rg = ReleaseGroupList("65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab")
        rg.get()
        # It would be cooler to use inspect
        handler = open(os.path.join(data.__path__[0], "test_rgroup.json"), "r")
        self.assertItemsEqual(rg.release_groups, json.load(handler))
        # golden data
        # open("test_rgroup.json", "w").write(json.dumps(rg.release_groups, indent=4, sort_keys=True))

    def test_offset_limit(self):
        """
        Simple test to check if we get the expected number of elements
        """
        class RGroupDouble(ReleaseGroupList):
            def add_releases_from_url(self, offset, limit):
                self.release_groups.extend(range(offset, offset+limit))

        rgd = RGroupDouble("whatever")
        rgd.get(100, Constants.RELEASE_GROUP_MIN_LIMIT-20)
        self.assertEqual(len(rgd.release_groups), Constants.RELEASE_GROUP_MIN_LIMIT)
        self.assertEqual(rgd.release_groups[-1], 149)

        rgd.get(100, Constants.RELEASE_GROUP_MIN_LIMIT)
        self.assertEqual(len(rgd.release_groups), Constants.RELEASE_GROUP_MIN_LIMIT)
        self.assertEqual(rgd.release_groups[-1], 149)

        rgd.get(100, Constants.RELEASE_GROUP_MAX_LIMIT-20)
        self.assertEqual(len(rgd.release_groups), Constants.RELEASE_GROUP_MAX_LIMIT-20)
        self.assertEqual(rgd.release_groups[-1], 229)

        rgd.get(100, Constants.RELEASE_GROUP_MAX_LIMIT)
        self.assertEqual(len(rgd.release_groups), Constants.RELEASE_GROUP_MAX_LIMIT)
        self.assertEqual(rgd.release_groups[-1], 249)

        rgd.get(100, Constants.RELEASE_GROUP_MAX_LIMIT+100)
        self.assertEqual(len(rgd.release_groups), Constants.RELEASE_GROUP_MAX_LIMIT)
        self.assertEqual(rgd.release_groups[-1], 249)

if __name__ == '__main__':
    unittest.main()
