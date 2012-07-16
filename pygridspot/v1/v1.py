"""
    ============================================
    :mod:`v1` -- Gridspot API Version 1
    ============================================

    .. Copyright 2012 Amir Elaguizy

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.

    .. module:: v1
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
"""

from pygridspot.api import *


class Gridspot_api_v1(Gridspot_api):
    def __init__(self, args):
        args.setdefault(
            'target_url_base', 'https://gridspot.com/compute_api/v1/')

        super(Gridspot_api_v1, self).__init__(args)

    def get_instances(self):
        url = self._get_request_url('list_instances')
        resp, content = self.http.request(url, "GET")

        if resp.status != 200:
            raise GridspotError("Received failure from gridspot: " + resp)

        obj = json.loads(content)

        if obj['exception_name']:
            raise GridspotError(
                "Received exception from gridspot: " + obj.exception_name)

        il = self.cache.load()
        il.update(obj)
        self.cache.save(il)

        return il

    def stop_instance(self, instance_id):
        url = self._get_request_url('stop_instance', instance_id=instance_id)
        resp, content = self.http.request(url, "GET")

        if resp.status != 200:
            raise GridspotError("Received failure from gridspot: " + resp)

        obj = json.loads(content)

        if obj['exception_name']:
            raise GridspotError(
                "Received exception from gridspot: " + obj.exception_name)
