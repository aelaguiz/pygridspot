"""
    ============================================
    :mod:`instance` -- Gridspot Instance
    ============================================

    .. Copyright 2012 Amir Elaguizy

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.

    .. module:: instance
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
"""


class Instance:
    """
    Defines an individual gridspot instance. Instance properties are
    dynamically added to this object as attributes. This object will
    typically be instantiated by the api, not the user

    Arguments:
        - *obj* - An object whos attributes represent this instance.
          Typically a deserialized json string as returned by the
          gridspot api servers.

    API V1 Attributes:
         instance_id: "inst_vOsVC2U4DxcSi_P8XxTbQA"
         vm_num_logical_cores: 4
         vm_num_physical_cores: 2
         winning_bid_id: "bid_iXwNYJzuF9DSy9GZDnKqvw"
         vm_ram: 1891628851
         start_state_time: 1332208799
         vm_ssh_wan_ip_endpoint: null
         current_state: "Starting"
         ended_state_time: null
         running_state_time: null
    """
    def __init__(self, obj):
        for key in obj:
            setattr(self, key, obj[key])

    def __repr__(self):
        return "Instance {0} = {1}".format(
            self.instance_id, self.current_state)
