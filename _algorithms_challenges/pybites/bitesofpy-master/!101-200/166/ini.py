import configparser
import re


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        return list({x for x in re.findall(r'[-\w]+', self.config['tox']['envlist'])})

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        return list({self.config[s][i]
                     for s in self.config.sections()
                     for i in self.config[s].keys() if 'basepython' == i})
