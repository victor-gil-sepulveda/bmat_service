import json
import unittest

from bmatservice.model.releasegroup import ReleaseGroup


class TestReleaseGroup(unittest.TestCase):
    def test_get(self):
        rg = ReleaseGroup("65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab")
        rg.get()
        open("test.json", "w").write(json.dumps(rg.release_group_data, indent=4, sort_keys=True))

if __name__ == '__main__':
    unittest.main()
