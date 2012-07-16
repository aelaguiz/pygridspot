"""
    ============================================
    :mod:`bootstrap` -- Gridspot Instance bootstrapper
    ============================================

    .. Copyright 2012 Amir Elaguizy

    .. You should have received a copy of the BSD License along with this
       program; see the file LICENSE.

    .. module:: bootstrap
    .. moduleauthor:: Amir Elaguizy <aelaguiz@gmail.com>
"""
import os

from fabric import api as fapi
from fabric.state import env

from error import *


def bootstrap_instance(ssh_key, instance, script_path, args):
    if not os.path.exists(script_path):
        raise GridspotError("Script not found")

    if not os.path.exists(ssh_key):
        raise GridspotError("Ssh key not found")

    fabric_args = {
        'key_filename': ssh_key,
        'user': 'gridspot_user'
    }
    fabric_args.update(args)
    fabric_args['use_shell'] = True

    args.setdefault('remote_tmp', '/tmp')

    script_filename = os.path.basename(script_path)
    remote_script = os.path.join(args['remote_tmp'], script_filename)

    with fapi.settings(**fabric_args):
        env.host_string = instance.vm_ssh_wan_ip_endpoint
        fapi.put(script_path, remote_script)
        fapi.sudo("chmod +x %s && %s && exit" % (
            remote_script, remote_script))
