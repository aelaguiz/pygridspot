===========
PyGridspot
===========

PyGridspot is a simple python client for the Gridspot API (www.gridspot.com). It is
intended to make managing gridspot vms easier. Typical usage looks like:

	import os
	from pygridspot import *

	g = Gridspot(api_key='<YOUR API KEY>',\
			cache='file',\
			cache_file='cache.dat')

	il = g.get_instances()

	for instance in il.new:
	    g.bootstrap(os.path.expanduser('~/.ssh/id_rsa'), instance, '/tmp/test.sh')

The above code when executed results in:

	aelaguiz$ python test.py
	[Instance inst_<INSTANCE_ID> = Running]
	[69.4.239.72:64333] put: /tmp/test.sh -> /tmp/test.sh
	[69.4.239.72:64333] sudo: chmod +x /tmp/test.sh && /tmp/test.sh && exit
	[69.4.239.72:64333] out: Ign http://security.ubuntu.com oneiric-security InRelease
	[69.4.239.72:64333] out: Ign http://us.archive.ubuntu.com oneiric InRelease
	[69.4.239.72:64333] out: Ign http://us.archive.ubuntu.com oneiric-updates InRelease

The key improvement over a simple REST client is the support for automatic bootstrapping
of the new VMs using the Fabric SSH API to push a setup script and run it on any new VMs.

Dependencies
===========

Fabric >= 1.4.3
httplib2 >= 0.7.4

Contributing
===========

Please do!

Changelog
========

0.01 - Initial release

0.01dev - Initial Upload
