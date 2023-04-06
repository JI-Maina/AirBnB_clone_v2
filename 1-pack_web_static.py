#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static folder

from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)

    archive = local("tar -cvzf {} web_static".format(file_path))

    if archive.succeeded:
        return file_path
    else:
        return None
