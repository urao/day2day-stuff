# Upgrade pip packages installed on the host

#!/usr/bin/python
import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
