"""
    ============================================
    :mod:`instancecache` -- Gridspot Instance Cache
    ============================================

    .. Copyright 2012 Amir Elaguizy 

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.
       
    .. module:: instancecache
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
""" 

import json
import ConfigParser

from instancelist import *

class InstanceCache(object):
    def __init__(self):
        pass

    def load(self):
        return InstanceList()

    def save(self, il):
        pass

class InstanceFileCache(InstanceCache):
    def __init__(self, cachePath):
        self.cachePath = cachePath

        super(InstanceCache, self).__init__()

    def load(self):
        rp = ConfigParser.RawConfigParser()
        rp.read(self.cachePath)

        il = InstanceList()

        if rp.has_section('instances'):
            instance_id_str = rp.get('instances', 'instance_ids')
            instance_ids = instance_id_str.split(',')
        
            instances = dict()

            for instance_id in instance_ids:
                instance_str = rp.get('instances', instance_id)
                instance_obj = json.loads(instance_str)

                instances[instance_obj['instance_id']] = Instance(instance_obj)

            il.set_instances(instances)

        return il

    def save(self, il):
        rp = ConfigParser.RawConfigParser()

        if not rp.has_section('instances'):
            rp.add_section('instances')
        
        for (instance_id,instance) in il.instances.items():
            instance_str = json.dumps(instance.__dict__)
            rp.set('instances', instance_id, instance_str)

        rp.set('instances', 'instance_ids', ','.join([ id for id in\
            il.instances.keys()]))

        with open(self.cachePath, "w") as f:
            rp.write(f)
            f.close()

