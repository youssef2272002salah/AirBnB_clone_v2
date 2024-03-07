#!/usr/bin/python3
# make a function that generate a .tgz archive of th content of web_static
# folders

from fabric.api import *
from datetime import datetime


def do_pack():
    """fuck pycode style """
    local("sudo mkdir -p versions")

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)

    result = local("sudo tar -czvf {filename} web_static")

    if result.succeeded:
        return filename
    else:
        return None
