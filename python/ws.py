#!/usr/bin/python
# encoding:utf-8

# ws is a wrapper of wsimport and helps to generate webservice client simply

# After generating, it's better to use eclipse to package the project. Using
# eclipse to build jar is simpler than the other tools.

import os
import sys
import re
import shutil

tag_dev = 'dev'
tag_prod = 'prod'
dflt_scene = 'dev'
dflt_prefix = 'D:/Studio/Eclipse'
dflt_out = '{prefix}/{name}-webservice-client-{scene}/src'
dflt_pkg = 'com.alitrip.busuac.{name}.webservice'

help_info = '''
Usage: ws <options> name wsdl_url
    options:
        -p    prefix
        -s    scene
        -v    version
        -h --help    help 
'''


def help():
    print(help_info)


def version():
    print("ws v1.0 2017-07-05")


if __name__ != '__main__':
    exit()

args = sys.argv
argc = len(args)

argv = []
scene = None
prefix = None
i = 1
while i < argc:
    x = args[i]
    arg = str(x).strip()
    if arg.startswith('-'):
        if x == '-v':
            version()
            exit()
        elif x == '-s':
            if i + 1 >= argc:
                help()
                exit()
            nx = str(args[i + 1]).replace('\\', '/')
            if not re.match(r'\w+', x):
                print('%s is not a valid scene(english words)' % nx)
                exit()
            scene = nx
            i = i + 1
        elif x == '-p':
            if i + 1 >= argc:
                help()
                exit()
            nx = args[i + 1]
            nx = str(nx).replace('\\', '/')
            nx = nx.rstrip('/')
            if not re.match(r'^(\w:)?(/[\w\d\-_]+)+/?$', nx):
                print('%s is not a valid path' % nx)
                exit()
            prefix = nx
            i = i + 1
        else:
            help()
            exit()

    else:
        argv.append(arg)

    i += 1

if len(argv) < 2:
    help()
    exit()

name = argv[0]
url = argv[1]

if not re.match(r'^[\w\d]+$', name):
    print('%s is not a standard project name, allows to consist of characters and numbers.' % name)
    exit()

scene = scene if scene else dflt_scene
prefix = prefix if prefix else dflt_prefix
out = dflt_out.format(prefix=prefix, scene=scene, name=name)
pkg = dflt_pkg.format(name=name)

if not os.path.exists(out):
    os.makedirs(out)
    print('creating directory:%s' % out)
else:
    shutil.rmtree(out,True)
    print('cleaning')

cmd = 'wsimport -keep -p {package} -s {output} {url}'.format(package=pkg, output=out, url=url)

print(cmd)
os.system(cmd)
print('Completed!')
