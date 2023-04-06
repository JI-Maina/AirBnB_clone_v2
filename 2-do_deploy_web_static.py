#!/usr/bin/python3
# distributes an archive to your web servers
from fabric.api import env, run, put
import os

env.user = "ubuntu"
env.hosts = ["54.173.137.54", "100.25.21.165"]


def do_deploy(archive_path):
    """Returns True if all operations have been done correctly,
    otherwise returns False"""

    if os.path.exists(archive_path):
        # grab the file name
        file_path = archive_path[9:]

        # create new path
        new_path = "/data/web_static/releases/" + file_path[:-4]
        filed_path = "/tmp/" + file_path

        # upload archive to /tmp/
        put("archive_path, /tmp/")

        run("mdir -p {}".format(new_path))

        run("tar -xzf {} -C {}/".format(filed_path, new_path))

        run("rm {}".format(filed_path))

        run("mv {}/web_static/* {}".format(new_path, new_path))

        run("rm -rf {}/web_static".format(new_path))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(new_path))

        return True
    else:
        return False
