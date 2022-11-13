#!/usr/bin/python3
"""This module uses Fabric to archive the repo contents
of AirBNB Clone Repo which will be deployed later on
"""

import os
from fabric.api import local, run, env, put, sudo
from datetime import datetime

env.hosts = ['44.200.40.98', '100.26.164.91']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'

def do_pack():
    """This function downloads the web_static folder
    and creates an archive of it
    """
    try:
        # Create the directory to save the archive
        local("mkdir -p versions")
        n = datetime.now()
        archive = f"versions/web_static_{n.strftime('%Y%m%d%H%M%S')}.tgz"
        # Get the archive
        local(f"tar -cvzf {archive} web_static ")
        print('Packing Successful')
        return archive
    except Exception:
        print('Packing Error!')
        return None


def do_deploy(archive_path):
    """This function uploads the archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_name = archive_path.replace('.tgz', '')
        archive_name = archive_name.replace('versions/', '')
        release_path = f"/data/web_static/releases/{archive_name}"
        sudo(f"mkdir -p {release_path}/")
        sudo(f"tar -xvzf /tmp/{archive_name}.tgz -C {release_path}/")
        run(f"rm /tmp/{archive_name}.tgz")
        sudo(f"mv {release_path}/web_static/* {release_path}/")
        sudo("rm -rf /data/web_static/current")
        sudo(f"rm -rf {release_path}/web_static/")
        sudo(f"ln -sf {release_path} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        print('Deploy Error!')
        return False

def deploy():
    """Deploy the AirBNB Clone"""
    try:
        archive_path = do_pack()
    except:
        print('Error!')
        return False

    return do_deploy(archive_path)
