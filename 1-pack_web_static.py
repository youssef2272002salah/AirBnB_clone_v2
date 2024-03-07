#!/usr/bin/python3
# make a function that generate a .tgz archive of th content of web_static
# folders

from fabric.api import *
from datetime import datetime


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
