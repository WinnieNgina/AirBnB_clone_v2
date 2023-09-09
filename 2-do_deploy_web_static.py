#!/usr/bin/python3
# Fabfile that distributes an archive to your web servers
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['localhost', '52.91.168.104', '100.24.253.204']
env.user = 'ubuntu'
# env.key_filename = '~/.ssh/id_rsa'

def is_local():
    """
    Check if the script is running locally by checking an environment variable.
    """
    return os.getenv('IS_LOCAL') == 'true'

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    archived = local("tar -cvzf {} web_static".format(archive_path))
    if archived.return_code != 0:
        return None
    else:
        return archive_path

def do_deploy(archive_path):
    '''Use os module to check for valid file path'''
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        if is_local():  # Check if the script is running locally
            local("mkdir -p {}".format(f_path))
            local("tar -xzf {} -C {}".format(a_path, f_path))
            local("rm {}".format(a_path))
            local("mv -f {}web_static/* {}".format(f_path, f_path))
            local("rm -rf {}web_static".format(f_path))
            local("rm -rf /data/web_static/current")
            local("ln -s {} /data/web_static/current".format(f_path))
        else:
            put(archive_path, a_path)
            run("mkdir -p {}".format(f_path))
            run("tar -xzf {} -C {}".format(a_path, f_path))
            run("rm {}".format(a_path))
            run("mv -f {}web_static/* {}".format(f_path, f_path))
            run("rm -rf {}web_static".format(f_path))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(f_path))

        return True
    return False

# Example usage: fab deploy (for remote server deployment)
# Example usage: IS_LOCAL=true fab deploy (for local deployment)

