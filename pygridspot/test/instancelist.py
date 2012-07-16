import os
import unittest
from pygridspot import *


class TestInstanceList(unittest.TestCase):
    def test_updates(self):
        instances1 = {
            "instances": [{
                "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw",
                "vm_num_logical_cores": 8,
                "vm_num_physical_cores": 4,
                "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
                "vm_ram": 1429436743,
                "start_state_time": 1342108905,
                "vm_ssh_wan_ip_endpoint": "69.4.239.74:62394",
                "current_state": "Running",
                "ended_state_time": "null",
                "running_state_time": 1342108989
            }
            ],
            "exception_name": ""
        }

        strI1 = json.dumps(instances1)
        objI1 = json.loads(strI1)

        il = InstanceList()
        il.update(objI1)

        self.assertEquals(len(il.instances), 1)
        self.assertEquals(len(il.new), 1)
        self.assertEquals(len(il.term), 0)

        i = il.instances['inst_CP2WrQi2WIS4iheyAVkQYw']

        for spec in instances1['instances']:
            for field in spec:
                self.assertEquals(spec[field], getattr(i, field))

        instances2 = {
            "instances": [{
                "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw",
                "vm_num_logical_cores": 8,
                "vm_num_physical_cores": 4,
                "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
                "vm_ram": 1429436743,
                "start_state_time": 1342108905,
                "vm_ssh_wan_ip_endpoint": "69.4.239.74:62394",
                "current_state": "Running",
                "ended_state_time": "null",
                "running_state_time": 1342108989
            }, {
                "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw2",
                "vm_num_logical_cores": 8,
                "vm_num_physical_cores": 4,
                "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
                "vm_ram": 1429436743,
                "start_state_time": 1342108905,
                "vm_ssh_wan_ip_endpoint": "69.4.239.74:62394",
                "current_state": "Starting",
                "ended_state_time": "null",
                "running_state_time": 1342108989
            }
            ],
            "exception_name": ""
        }

        strI2 = json.dumps(instances2)
        objI2 = json.loads(strI2)

        il.update(objI2)

        self.assertEquals(len(il.instances), 2)
        self.assertEquals(len(il.new), 1)
        self.assertEquals(len(il.term), 0)

        self.assertEquals(
            il.new[0].instance_id, 'inst_CP2WrQi2WIS4iheyAVkQYw2')

        for spec in instances2['instances']:
            for field in spec:
                self.assertEquals(
                    spec[field], getattr(
                        il.instances[spec['instance_id']], field))

        instances3 = {
            "instances": [
            ],
            "exception_name": ""
        }

        strI3 = json.dumps(instances3)
        objI3 = json.loads(strI3)

        il.update(objI3)

        self.assertEquals(len(il.instances), 0)
        self.assertEquals(len(il.new), 0)
        self.assertEquals(len(il.term), 2)

        self.assertEquals(
            il.term[0].instance_id, 'inst_CP2WrQi2WIS4iheyAVkQYw')
        self.assertEquals(
            il.term[1].instance_id, 'inst_CP2WrQi2WIS4iheyAVkQYw2')

    def test_filecache(self):
        path = "test.dat"

        if os.path.exists(path):
            os.remove(path)

        instances1 = {
            "instances": [{
                "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw",
                "vm_num_logical_cores": 8,
                "vm_num_physical_cores": 4,
                "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
                "vm_ram": 1429436743,
                "start_state_time": 1342108905,
                "vm_ssh_wan_ip_endpoint": "69.4.239.74:62394",
                "current_state": "Running",
                "ended_state_time": "null",
                "running_state_time": 1342108989
            }
            ],
            "exception_name": ""
        }

        strI1 = json.dumps(instances1)
        objI1 = json.loads(strI1)

        il = InstanceList()
        il.update(objI1)

        fc = InstanceFileCache(path)
        fc.save(il)

        il2 = fc.load()

        print il2.instances
        print il.instances

        self.assertEquals(len(il2.instances), 1)

        for (in1_id, in1) in il.instances.items():
            in2 = il2.instances[in1.instance_id]

            self.assertEquals(
                json.dumps(in1.__dict__), json.dumps(in2.__dict__))

        instances2 = {
            "instances": [{
                "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw",
                "vm_num_logical_cores": 8,
                "vm_num_physical_cores": 4,
                "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
                "vm_ram": 1429436743,
                "start_state_time": 1342108905,
                "vm_ssh_wan_ip_endpoint": "69.4.239.74:62394",
                "current_state": "Running",
                "ended_state_time": "null",
                "running_state_time": 1342108989
            }, {
                "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw2",
                "vm_num_logical_cores": 8,
                "vm_num_physical_cores": 4,
                "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
                "vm_ram": 1429436743,
                "start_state_time": 1342108905,
                "vm_ssh_wan_ip_endpoint": "69.4.239.74:62394",
                "current_state": "Starting",
                "ended_state_time": "null",
                "running_state_time": 1342108989
            }
            ],
            "exception_name": ""
        }

        strI2 = json.dumps(instances2)
        objI2 = json.loads(strI2)

        il2.update(objI2)

        self.assertEquals(len(il2.instances), 2)
        self.assertEquals(len(il2.new), 1)
        self.assertEquals(len(il2.term), 0)

        self.assertEquals(
            il2.new[0].instance_id, 'inst_CP2WrQi2WIS4iheyAVkQYw2')

        for spec in instances2['instances']:
            for field in spec:
                self.assertEquals(
                    spec[field], getattr(
                        il2.instances[spec['instance_id']], field))

        os.remove(path)
