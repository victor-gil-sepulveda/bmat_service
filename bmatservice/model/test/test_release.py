import json
import unittest

from bmatservice.model.releasegroup import ReleaseGroup


class TestReleaseGroup(unittest.TestCase):
    def test_get(self):
        rg = ReleaseGroup("02546843-b2b1-4c7f-a31a-23c31e8133bc")
        rg.get()
        open("test_release.json", "w").write(json.dumps(rg.data, indent=4, sort_keys=True))

if __name__ == '__main__':
    unittest.main()
