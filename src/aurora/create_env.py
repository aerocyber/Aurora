import venv
import os.path
import os
import sys
import subprocess


class EnvCreationError(Exception):
    pass


class BuildEnv(venv.EnvBuilder):
    def __init__(self, path):
        self.path = os.path.normcase(
            os.path.normpath(
                path
            )
        )
        self.with_pip = True
        self.system_site_packages = False
        if os.name == 'nt':
            self.symlinks = False
        else:
            self.symlinks = True
        self.prompt = "Aurora:: " + target_dir_name
        self.clear = False
        self.upgrade = False
        self.upgrade_deps = False
        self.requirements = []
        self.install_requirements = True

    
    def add_requirements(self, requirements: list):
        self.requirements = requirements
    

    def upgrade(self):
        self.upgrade = True
    

    def upgrade_deps(self):
        self.upgrade_deps = True


    def allow_site_packages(self):
        self.system_site_packages = True
    

    def clear_dir(self):
        self.clear = True


    def prompt(self, new_prompt):
        self.prompt = new_prompt # Use None for default venv behaviour.


    def no_upgrade(self):
        self.upgrade = False
    

    def no_upgrade_deps(self):
        self.upgrade_deps = False


    def disallow_site_packages(self):
        self.system_site_packages = False
    

    def no_clear_dir(self):
        self.clear = False


    def no_install_requirements(self):
        if self.requirements:
            raise EnvCreationError("Requirements exists. Can't stop installation if requirements exist.")
        self.install_requirements = False
    

    def nopip(self):
        if self.requirements:
            raise EnvCreationError("Requirements exists. Can't stop installation of pip if requirements exist.")
        self.with_pip = False

    
    def apply(self):
        if os.path.exists(self.path) and not self.clear:
            raise TargetExistsError(self.path + " exists.")
        if self.upgrade and self.clear:
            raise ValueError("Cannot use clear and upgrade together.")
        

    def post_setup(self, context):
        for i in self.requirements:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])