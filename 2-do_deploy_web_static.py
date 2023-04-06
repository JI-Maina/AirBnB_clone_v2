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
        file = archive_path.split("/")[-1]

        # create new path
        new_path = file.split(".")[0]

        # upload archive to /tmp/
        put("archive_path, /tmp/{}".format(file))

        run("rm -rf /data/web_static/releases/{}/".format(name))

        run("mdir -p /data/web_static/releases/{}/".format(name))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name))

        run("rm /tmp/{}".format(file))

        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name))

        run("rm -rf /data/web_static/releases/{}/web_static".format(name))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))

        return True
    else:
        return False
