import time
import os
import cgi
import unittest
import subprocess
from pygridspot import *


class V1(unittest.TestCase):
    def setUp(self):
        cwd = os.getcwd()
        server_path = os.path.join(cwd, 'pygridspot/test/v1_server.py')

        print "Starting", server_path
        self.serv = subprocess.Popen(['python', server_path])
        print "Started"
        time.sleep(2)

    def tearDown(self):
        print "Stopping test server"

        # This won't work on windows
        subprocess.call("ps -ef | grep python.*v1_server | grep -v grep | awk "
                        "'{print $2}' | xargs -I {} kill -9 {}", shell=True)

    def test_requests(self):
        g = Gridspot(
            api_key='testkey', target_url_base='http://localhost:5000')

        il = g.get_instances()

        self.assertEquals(len(il.new), 1)
        self.assertEquals(il.new[0].instance_id, "inst_CP2WrQi2WIS4iheyAVkQYw")

        g.stop_instance("inst_CP2WrQi2WIS4iheyAVkQYw")
