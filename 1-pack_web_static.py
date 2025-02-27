#!/usr/bin/python3
"""
    a python script that generates .tgz arcgive from the content of web static
"""
import tarfile
from datetime import datetime
import os.path
from fabric.api import local


def do_pack():
    """
        Return the archive path if archive has been correctly
        gernerated.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None
