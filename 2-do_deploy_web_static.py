#!/usr/bin/python3
# Fabfile that distributes an archive to your web servers
from fabric.api import put, env, run
import os


env.hosts = ["52.91.168.104", "100.24.253.204"]


def do_deploy(archive_path):
    '''use os module to check for valid file path'''
    if os.path.isfile(archive_path) is False:
        return False
    # Remove version
    filewithextension = archive_path.split("/")[-1]
    filename = filewithextension.split(".")[0]
    if put(archive_path, "/tmp/{}".format(filename)).failed is True:
        return False
        # If failed is True, means upload was unseccessful
    if run("rm -rf /data/web_static/releases/{}/".format(filename)).failed is True:
        # Remove existing web app version
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(filename)).failed is True:
        # create a new empty directory
        # if it fails return false
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filewithextension, filename)).failed is True:
        '''
        tar decompresses and compresses tape archives files and directories
        -x: specifies files to extract
        -z: Specifies archives uses gzip compression
        -f: name of archive file to extract
        -C: specifies where files are stored after extraction
        '''
        return False
    if run("rm /tmp/{}".format(filewithextension)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/*" "/data/web_static/releases/{}/".format(filename, filename)).failed is True:
        return False
        # move the files to right directory
    if run("rm -rf /data/web_static/releases/{}/web_static/".format(filename, filename)).failed is True:
        return False
        # Remove the directory
    if run("rm -rf /data/web_static/current").failed is True:
        # Remove current symbolic link
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(filename)).failed is True:
        # create a new symbolic link with the new version
        return False
    return True
    # if all steps are executed sucessfully return True
