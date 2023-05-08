import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, sudo
import os, getpass

REPO_URL = 'https://github.com/besartelezi/test_driven_to_do'

def deploy():
    print("checking if folder already exists...")
    site_folder = f'/home/{env.user}/sites/{env.host}'
    sudo(f'mkdir -p {site_folder}')
    print(site_folder + ' : is path currently in use')
    with cd(site_folder):
        print("getting latest source")
        _get_latest_source()
        print("_update_virtualenv() called")
        _update_virtualenv()
        print("_create_or_update_dotenv() called")        
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _get_latest_source():
    print("function has been successfully called")
    if exists('.git'):
        print("git fetching")
        sudo('git fetch')
    else:
        print("git cloning")
        sudo(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    sudo(f'git reset --hard {current_commit}')

def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        sudo(f'python3.7 -m venv virtualenv')
    sudo('./virtualenv/bin/pip install -r requirements.txt')

def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = sudo('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(  
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_static_files():
    sudo('./virtualenv/bin/python manage.py collectstatic --noinput')  

def _update_database():
    sudo('./virtualenv/bin/python manage.py migrate --noinput')  