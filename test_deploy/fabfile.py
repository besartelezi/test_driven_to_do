import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, sudo
import os, getpass

REPO_URL = 'https://github.com/besartelezi/test_driven_to_do'

def deploy():
    print("checking if folder already exists...")
    print('user: ' + env.user)
    print('host: ' + env.host)
    sudo('mkdir -p testfolder')