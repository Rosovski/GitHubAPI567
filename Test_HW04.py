import unittest
from Homework04 import get_repo_info

class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: Rosovski',
                    'Repo: hello-world Number of commits: 5',
                    'Repo: SSW-555-GEDCOM Number of commits: 7',
                    'Repo: SSW-567 Number of commits: 2',
                    'Repo: SSW-567-HW-01 Number of commits: 2',
                    'Repo: ssw690ossmgmt Number of commits: 1',
                    'Repo: Stevens-Academic-Data-Repository Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 5']
        self.assertEqual(get_repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_repo_info('zhonghuabao'), 'unable to fetch repos from user')
        self.assertEqual(get_repo_info(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main(verbosity=2)