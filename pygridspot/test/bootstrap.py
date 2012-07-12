import time
import os
import cgi
import unittest
import subprocess
from pygridspot import *

class TestBootstrap(unittest.TestCase):
    def test_bs(self):
        print "Running"

        instance1 = {
          "instances": [
            {
              "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw",
              "vm_num_logical_cores": 8,
              "vm_num_physical_cores": 4,
              "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
              "vm_ram": 1429436743,
              "start_state_time": 1342108905,
              "vm_ssh_wan_ip_endpoint": "69.4.239.77:65423",
              "current_state": "Running",
              "ended_state_time": "null",
              "running_state_time": 1342108989
            }
          ],
          "exception_name": ""
        }

        il = InstanceList()
        il.update(instance1)

        i = il.new[0]

        g = Gridspot(api_key='testkey')


        g.bootstrap(os.path.expanduser('~/.ssh/id_rsa'), i, '/tmp/test.sh')
