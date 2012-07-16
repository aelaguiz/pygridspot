"""
    ============================================
    :mod:`api` -- Gridspot API Version Base
    ============================================

    .. Copyright 2012 Amir Elaguizy

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.

    .. module:: api
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
"""

import urllib
import urlparse
import httplib2

from error import *
from instancecache import *


class Gridspot_api(object):
    """
    Base api object to be inherited from when implementing a new api
    specification
    """
    def __init__(self, args):
        self.args = args

        self.__validateArgs()
        self.__setupCache()

        # Requires a cache argument, even though we don't use it
        self.http = httplib2.Http(".cache")

    def get_instances(self):
        raise GridspotError("Unimplemented")

    def stop_instance(self, instance_id):
        raise GridspotError("Unimplemented")

    """
    Protected functions
    """

    def _get_request_url(self, func, **req_params):
        params = {}
        params.setdefault('api_key', self.args['api_key'])
        params.update(req_params)

        params = urllib.urlencode(params)
        base_url = urlparse.urljoin(self.args['target_url_base'], func)

        return base_url + "?" + params

    """
    Private functions
    """

    def __request(self, func, **req_params):
        req_url = self.__get_request_url(func, req_params)

        self.http.request(req_url, "GET")

    def __validateArgs(self):
        self.args.setdefault('cache', 'none')

        self.__requireArg('api_key')
        self.__requireArg('target_url_base')

    def __setupCache(self):
        if self.args['cache'] == 'none':
            self.cache = InstanceCache()
        elif self.args['cache'] == 'file':
            self.__requireArg('cache_file')
            self.cache = InstanceFileCache(self.args['cache_file'])

    def __requireArg(self, key):
        if not key in self.args:
            raise GridspotError("Missing argument: " + key)
