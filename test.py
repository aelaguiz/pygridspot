import os
from pygridspot import *

g = Gridspot(api_key='apikey_t_EcF8Dqg2NpBEwgUFcREQ',\
                cache='file',\
                cache_file='cache.dat')

il = g.get_instances()

print il.new

for instance in il.new:
    g.bootstrap(os.path.expanduser('~/.ssh/id_rsa'), instance, '/tmp/test.sh')
