import os
from tomlkit import dumps
from tomlkit import parse
from shutil import copytree
from subprocess import check_call


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
        _dir = os.getcwd()
        target_dir = os.path.abspath(cmd["DIRS"]["Build"])
        src_dir = os.path.abspath(cmd["DIRS"]["Source"])
        copytree(src_dir, target_dir)
        os.chdir(target_dir)
        command = cmd["Commands"]
        commands = []
        for key in command:
            commands.insert(0, {key: command[key]})
        command = {}
        for i in commands:
            check_call(commands[i].values().join("&&"))
    

class CreatePyFile:
    def __init__(self, target_dir, overwrite = False):
        if os.path.exists(os.path.join(target_dir, 'Pyfile')) and not overwrite:
            raise FileExistsError(os.path.join(target_dir, 'Pyfile') + " exists and overwrite NOT allowed.")
        self.path = os.path.join(target_dir, 'Pyfile')
        self.cmds = {}


    def commands(self, commands: dict):
        self.cmds = self.cmds.update(commands)
    

    def exec(self):
        if os.path.exists(self.path) and not overwrite:
            raise FileExistsError(self.path + " exists and overwrite NOT allowed.")
        f = open(self.path, 'w')
        f.write(dumps(self.cmds))
        f.close()