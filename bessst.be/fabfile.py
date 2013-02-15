import os.path
from fabric.api import run, local, put, cd, sudo, env
from fabric.contrib.console import confirm

env.hosts = ['osp@bessst.be']
env.path = '/home/osp/apps/osp.work.bessst/'

def deploy():
    with cd(env.path + 'bessst.be/'):
        run('git pull origin master')
        run('python manage.py collectstatic --noinput')
        sudo('/usr/sbin/apachectl graceful')

def getdb():
    local('/usr/bin/scp osp@bessst.be:apps/osp.work.bessst/bessst.be/run/test.db run/test.db')

def getimages():
    local('/usr/bin/scp osp@bessst.be:apps/osp.work.bessst/bessst.be/run/assets/images/*.* run/assets/images/')

