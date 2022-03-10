import os
from tomlkit import dumps
from tomlkit import parse


class PyFile:
    def __init__(self, path_to_Pyfile):
        if not os.path.exists(path_to_Pyfile):
            raise FileNotFoundError(path_to_Pyfile + " is not found in: " + os.getcwd())
        self.path = path_to_Pyfile
    def exec(self):
        # Check for existance in case file has been removed prior to running exec
        if not os.path.exists(self.path):
            raise FileNotFoundError(self.path + " is not found in: " + os.getcwd())
        f = open(self.path)
        cmd = parse(f.read())
        f.close()
        os.mkdir("build")
        os.chdir(os.path.join(os.getcwd(), 'build'))