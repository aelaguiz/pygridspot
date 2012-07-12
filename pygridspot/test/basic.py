import cgi
import unittest
from pygridspot import *

class TestBasic(unittest.TestCase):
    def test_version(self):
        # Should throw for invalid api version
        self.assertRaises(GridspotError, Gridspot, **{'api_key': 'lkjsdf',
            'api_version':3333})

        # Should succeed
        g = Gridspot(api_key='32523', api_version=1)

        self.assertTrue(isinstance(g.api, Gridspot_api_v1))

    def test_url(self):
        # Should succeed
        g = Gridspot(api_key='32523', target_url_base='http://www.google.com/')

    def test_request_url(self):
        g = Gridspot(api_key='32523', target_url_base='http://www.testurl.com/')

        url = g.api.get_request_url('testfunc', testarg1=5)

        res = urlparse.urlparse(url)
        self.assertEqual(res.scheme, 'http')
        self.assertEqual(res.netloc, 'www.testurl.com')
        self.assertEqual(res.path, '/testfunc')

        args = dict(cgi.parse_qsl(res.query))
        self.assertEqual(args['testarg1'], '5')
        self.assertEqual(args['api_key'], '32523')
