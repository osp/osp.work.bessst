import os.path
from fabric.api import run, local, put, cd, sudo, env
from fabric.contrib.console import confirm


def mozzarella():
    env.hosts = ['stdin@mozzarella.stdin.fr']
    env.path = '/home/stdin/www/bessst.stdin.fr/'
    #env.git_path = '/home/sarma/www/be.sarma/db/repositories'
    #env.media_path = '/home/sarma/www/be.sarma/static/media/'


def fix_permissions():
    # fixes permission issues
    with cd(env.path + 'bessst.be/'):
        sudo('chown -R %s:www-data %s' % (env.user, env.path))
        sudo('chmod -R g+w %sbessst.be' % env.path)
        sudo('/etc/init.d/apache2 reload')
        sudo('/etc/init.d/nginx reload')


def deploy(treeish='HEAD'):
    env.path = '/home/stdin/www/bessst.stdin.fr/'
    # makes a tarball of the django project and transfers it
    #local('git archive %s . | gzip > project.tar.gz' % treeish)
    put('project.tar.gz', env.path)
    #local('rm project.tar.gz')

    # backups old versions
    with cd(env.path):
        import time
        timestamp = time.strftime('%Y%m%d%H%M%S')
        try:
            run('mv bessst.be bessst.be.%s.bak' % timestamp)
        except:
            pass
        run('mkdir bessst.be')

    # gunzips the new django project
    with cd(env.path + 'bessst.be/'):
        run('tar zxvf ../project.tar.gz')
        run('rm ../project.tar.gz')

    # recreates symbolic links
    #with cd(env.path + 'bessst.be/'):
        #run('ln -s ../esadgv.db')
        #run('ln -s ../media')
    with cd(env.path + 'bessst.be/run/static/'):
        run('ln -s ../../../venv/lib/python2.6/site-packages/django/contrib/admin/static/admin')


    fix_permissions()


def download():
    env.path = '/home/stdin/www/esadgv2.stdin.fr/'
    local('scp stdin@mozzarella.stdin.fr:%sesadgv.db run/run/' % env.path)
    local('rsync -avz --progress --stats stdin@mozzarella.stdin.fr:%smedia run/run/' % env.path)


def upload():
    env.path = '/home/stdin/www/esadgv2.stdin.fr/'
    print("You are about to replace the remote database with the local one...")
    choice = confirm("...Do you really want to continue?", default=False)
    if choice:
        with cd(env.path):
            import time
            timestamp = time.strftime('%Y%m%d%H%M%S')
            try:
                run('mv esadgv.db esadgv.db.%s.bak' % timestamp)
            except:
                pass
        local('scp run/run/esadgv.db stdin@mozzarella.stdin.fr:%s' % env.path)
        sudo('chown -R %s:www-data %sesadgv.db' % (env.user, env.path))
        sudo('chmod -R g+w %sesadgv.db' % env.path)
        local('rsync -avz --progress --stats run/run/media stdin@mozzarella.stdin.fr:%s' % env.path)
        run('cd %sesadgv/run/run/' % env.path)
    else:
        print "Aborted"


