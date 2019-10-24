import unittest
from unittest import mock
import json
import requests


def fake_get(url):
    if url.startswith("https://api.github.com/users/"):
        return open("getReposResponse.json").read()
    elif url.startswith("https://api.github.com/repos/"):
        url = url[29:]  # remove the above prefix
        url = url.replace("/commits", "")  # remove /commits
        repo_name = url[url.find("/") + 1:]  # remove username
        # read the file content from the associated json file
        return open("repo-" + repo_name + ".json").read()


class TestHW4(unittest.TestCase):

    @mock.patch("requests.get", side_effect=fake_get)
    def test_something(self, mocked):
        content = requests.get("https://api.github.com/repos/Rosovski/Triangle567/commits")
        expect = 5
        self.assertEquals(expect, len(json.loads(content)))
        # for line in json.loads(content):
        #     print(line["name"])

    
if __name__ == '__main__':
    unittest.main()
