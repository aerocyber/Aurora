import venv
import os.path


class TargetExistsError(Exception):
    pass


class Customisation:
    def __init__(self, target_dir_location, target_dir_name):
        self.path = os.path.normcase(
            os.path.normpath(
                os.path.join(target_dir_location, target_dir_name)
            )
        )
        self.with_pip = True
        self.system_site_packages = False
        self.symlinks = False
        self.prompt = "Aurora:: " + target_dir_name
        self.clear = False
        self.upgrade = False
        self.upgrade_deps = False
        self.requirements = []
        if os.path.exists(self.path) and not self.clear:
            raise TargetExistsError(self.path + " exists.")

    
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