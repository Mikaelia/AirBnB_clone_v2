#!/usr/bin/python3
"""
deploy web static
"""
import os
import time
from fabric.api import local, run, hosts, env, put

env.hosts = ['35.237.60.90', '35.237.27.137']
env.user = 'ubuntu'

def do_pack():
    """
    function creates a .tgz archive
    """

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None

def do_deploy(archive_path):
    """
    function to dist to web server
    """

    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    filename = archive_path[9:]
    foldername = "/data/web_static/releases/" + filename[:-4]
    filename = "/tmp/" + filename
    if not run('mkdir -p {}'.format(foldername)).succeeded:
        return False
    if not run('tar -xzf {} -C {}'.format(filename, foldername)).succeeded:
        return False
    if not run('rm {}'.format(filename)).succeeded:
        return False
    if not run('mv {}/web_static/* {}'.format(foldername,
                                              foldername)).succeeded:
        return False
    if not run('rm -rf {}/web_static'.format(foldername)).succeeded:
        return False
    if not run('rm -rf /data/web_static/current').succeeded:
        return False
    return run('ln -s {} /data/web_static/current'.format(
        foldername)).succeeded


if __name__ == "__main__":
    do_pack()
