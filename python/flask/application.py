
# This file is a simple framework to help you organize your flask's project likes django
# if you use it , your project's constructure likes the follows:

#myflask
#      |---admin
#      |      |---views.py
#      |      |---models.py
#      |      |---static
#      |      |---templates
#      |---blog
#      |      |---views.py
#      |      |---models.py
#      |      |---static
#      |      |---templates
#      |---static
#      |---templates
#      |---settings.py
#      |---application.py
#      |---wsgi.py

# author: stonenice@outlook.com
# date: 2017-03-04

from flask import Flask, Blueprint
import settings
import importlib


class Application(object):
    def __init__(self, name):
        self.__name = name
        self.__app = Flask(self.__name)
        self.__apps = []

        try:
            self.__static_folder = settings.static_folder
            if not self.__static_folder or len(self.__static_folder.strip())<=0:
                self.__static_folder = 'static'
        except:
            self.__static_folder = 'static'


        try:
            self.__templates_folder = settings.templates_folder
            if not self.__templates_folder or len(self.__templates_folder.strip())<=0:
                self.__templates_folder = 'templates'
        except:
            self.__templates_folder = 'templates'


    def __normalize(self, entry):
        if not isinstance(entry, (tuple, list)):
            return None
        entry = [str(x).strip() for x in entry if x]
        size = len(entry)

        if size == 1:
            e = (entry[0], (entry[0] if str(entry[0]).startswith('bp_') else 'bp_' + entry[0]), None)
        elif size == 2:
            if str(entry[1]).startswith('/'):
                e = (entry[0], (entry[0] if str(entry[0]).startswith('bp_') else 'bp_' + entry[0]), entry[1])
            else:
                e = (entry[0], entry[1], None)
        elif size == 3:
            e = entry
        else:
            e = None
        return e

    def __blueprinturl(self, register_url, url_prefix, module_name=''):

        if not module_name:
            module_name = ''

        if register_url:
            if not url_prefix or url_prefix == '/':
                new_u = register_url
            else:
                new_u = register_url + url_prefix
                new_u = new_u.replace('//', '/')
        else:
            if not url_prefix:
                new_u = '/' + module_name
            else:
                new_u = url_prefix

        return new_u

    def register_blueprint(self):

        try:

            apps = settings.INSTALLED_APPS

            for x in apps:
                e = self.__normalize(x)
                if not e:
                    continue

                m, b, u = e

                if m == '.':
                    continue

                try:
                    module = importlib.import_module(m)
                    bp = getattr(module, b)
                except (ImportError, AttributeError) as e:
                    try:
                        module = importlib.import_module(m + '.views')
                        bp = getattr(module, b)
                    except (ImportError, AttributeError) as e:
                        bp = None

                if not isinstance(bp, Blueprint):
                    print 'Warning: cannot find "%s" in "%s" module' % (b, m)
                    continue

                url_prefix = getattr(bp, 'url_prefix')

                if url_prefix:
                    url_prefix = url_prefix.strip()
                    if not url_prefix.startswith('/'):
                        url_prefix = '/' + url_prefix

                if str(m).find('.') >= 0:
                    s = str(m).split('.')
                    module_name = s[len(s) - 1]
                else:
                    module_name = str(m)

                bp.template_folder = self.__templates_folder
                bp.static_folder = self.__static_folder
                bp.static_url_path = '/%s/%s/%s' % (self.__static_folder, module_name,self.__static_folder)

                new_u = self.__blueprinturl(u, url_prefix, module_name)

                options = {}

                if new_u and not new_u.startswith('/'):
                    options['url_prefix'] = new_u
                self.__app.register_blueprint(bp, **options)
                self.__apps.append((m, b, new_u))

        except Exception, e:
            print e

    def run(self, host='localhost', port=5000, debug=True):

        self.register_blueprint()
        if debug:
            print self.__apps

        # self.__app.template_folder='templates'

        self.__app.run(host, port, debug)
