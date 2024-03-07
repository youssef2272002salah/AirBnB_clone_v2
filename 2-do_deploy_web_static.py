#!/usr/bin/python3
# fabric script to send the archive file to my servers

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['100.25.142.157', '54.160.93.135']


def do_deploy(archive_path):
    '''fuck pycode style '''
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
