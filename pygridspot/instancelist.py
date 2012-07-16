"""
    ============================================
    :mod:`instancelist` -- Gridspot Instance List
    ============================================

    .. Copyright 2012 Amir Elaguizy

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.

    .. module:: instancelist
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
"""

from instance import *


class InstanceList:
    """
    Represents a list of gridspot instances. Automatically maintains a list of
    new and terminated instances from the last update operation.

    Attributes:
        - *instances* - Dictionary of all known valid instances
        - *new* - List of instances created on last update
        - *term* - List of instances destroyed on last update
    """
    def __init__(self):
        self.instances = {}
        self.new = []
        self.term = []

    def set_instances(self, instances):
        """
        Overwrites the existing instances dictionary forcefully, resets the new
        and terminated list to empty lists
        """
        self.instances = instances
        self.new = []
        self.term = []

    def update(self, instance_response):
        """
        Accepts a gridspot object (deserialized json) and creates a list of
        ``Instance`` objects internally. Sets the new and term lists as well as
        updates the instances dictionary.
        """
        instance_map = {
            i['instance_id']: i for i in instance_response['instances']}

        existing_set = set(self.instances)
        updated_set = set(instance_map)

        new_set = updated_set.difference(existing_set)
        terminated_set = existing_set.difference(updated_set)

        new_instances = [Instance(instance_map[id]) for id in new_set]
        terminated_instances = [self.instances[id] for id in terminated_set]

        for id in terminated_set:
            del self.instances[id]

        for instance in new_instances:
            self.instances[instance.instance_id] = instance

        self.new = new_instances
        self.term = terminated_instances
