"""
    ============================================
    :mod:`pygridspot` -- Gridspot API
    ============================================
    
    This module serves as the user facing API exported by the pygridspot
    package.

    The Gridspot class contains all user functionality.

    .. Copyright 2012 Amir Elaguizy 

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.
       
    .. module:: pygridspot
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
""" 

import json

from api import *
from v1 import Gridspot_api_v1

from bootstrap import bootstrap_instance

# Lookup table used to lookup the correct api
# for a specified api_version
API_MAP={ '1': Gridspot_api_v1 }

class Gridspot:
    """
    Defines a Gridspot object to be used for all interactions with gridspot

    Keyword arguments:

        - *api_key* - Required. Your gridspot api key. You can get one at
          https://gridspot.com/compute/account
        - *cache* - Required. Controls caching behavior between instantiations of 
          the Gridspot object. Acceptable arguments are 'none' or 'file'. If
          'file' is specified then the cache_file argument is mandatory.
        - *cache_file* - Situational. Specifies the path on disk to use as the
          cache file when file caching is enabled. Will be overwritten with 
          subsequent calls.
        - *api_version* - Optional. The gridspot api to use (default: 1)
        - *target_url_base* - Optional. The url to use for the gridspot api
          servers. Defaults will vary based on api_version.
    """

    def __init__(self, **kwargs):
        kwargs.setdefault('api_version', 1)

        self.args = kwargs

        self.__init_api()

    def get_instances(self):
        """
        Hits the api to retrieve a list of available instances

        Returns an ``InstanceList``
        """
        return self.api.get_instances()

    def bootstrap(self, ssh_key, instance, script_path, **kwargs):
        """
        Uploads and runs the specified script. Useful for bringing new servers
        quickly up to a useable state

        Arguments:
        
        - *ssh_key* -- path to the ssh private key to use
        - *instance* -- an ``Instance`` object representing the server to
          bootstrap
        - *script_path* -- path to the script to be run
        - *kwargs* -- Optional arguments which will be added to the fabric
          configuration, can be used to significantly customize behavior. The
          use_shell=True argument is automatically specified. See
          http://docs.fabfile.org/en/1.4.3/api/core/operations.html#fabric.operations.run
    
        .. note::

            The script is run via sudo
        """
        return bootstrap_instance(ssh_key, instance, script_path, kwargs)

    def __init_api(self):
        api_version = str(self.args['api_version'])

        if not api_version in API_MAP:
            raise GridspotError("Unknown api version: '" +
                        api_version + "'")

        self.api = API_MAP[api_version](self.args)
