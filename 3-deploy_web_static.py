#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['100.25.142.157', '54.160.93.135']  # <IP web-01>, <IP web-02>
env.user = 'ubuntu'


def do_pack():
    """fuck pycode style """
# make the dir to store the .tgz files
    local("sudo mkdir -p versions")
# make the name of the file tha alx wanted
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
# tar : command to make the archive
# -c :create a new archive
# -v :display the progress while archiving.
# -z :compress using gzip
# -f : specif the name of file
    result = local("sudo tar -cvzf {} web_static".format(filename))

    if result.succeeded:
        return filename
    else:
        return None


def do_deploy(archive_path):
    '''pycodestyle'''
    if exists(archive_path) is False:
        return False

    archive_file = archive_path[9:]
    re_archive = '/data/web_static/releases/{}'.format(archive_file[:-4])
# print(archive_file)    web_static_20240307150135.tgz
# print(re_archive)/data/web_static/releases/web_static_20240307150135
    try:
        # upload
        put(archive_path, '/tmp/')
        # make dir
        run('sudo mkdir -p {}'.format(re_archive))
        # extract
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_file, re_archive))
        # remove the uploaded file
        run('sudo rm /tmp/{}'.format(archive_file))

        run('sudo mv {}/web_static/* {}'.format(re_archive, re_archive))
        run('sudo rm -rf /data/web_static/releases/web_static')
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(re_archive))
        return True
    except BaseException:
        return False


def deploy():
    """Create and distributes an archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False
