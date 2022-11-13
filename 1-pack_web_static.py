#!/usr/bin/python3
"""This module uses Fabric to archive the repo contents
of AirBNB Clone Repo which will be deployed later on
"""

import fabric
from datetime import datetime


def do_pack():
    """This function downloads the web_static folder
    and creates an archive of it. It generates a .tgz archive from the
    contents of the web_static folder of your AirBnB Clone repo.
    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    Returns: the name of the archive
    """
    try:
        # Create the directory to save the archive
        fabric.operations.local("mkdir -p versions")
        n = datetime.now()
        archive = f"versions/web_static_{n.strftime('%Y%m%d%H%M%S')}"
        # Get the archive
        fabric.operations.local(f"tar -cvzf {archive} web_static ")
        return archive
    except Exception:
        return None
