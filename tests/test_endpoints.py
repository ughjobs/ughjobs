import unittest
import urllib.request as request
import urllib.error

class FlaskJobShopTest(unittest.TestCase):

    def test_home_status_code(self):
        """Assert that user successfully lands on homepage"""
        result = request.urlopen('http://localhost:5000/')
        self.assertEqual(result.code, 200)

    def test_user_not_autheticated(self):
        with self.assertRaises(urllib.error.HTTPError) as cm:
            result = request.urlopen('http://localhost:5000/user')
        exception = cm.exception
        self.assertEqual(exception.code, 401)


if __name__ == '__main__':
    unittest.main()
