import create_env
import os

def create_env(path, with_pip, system_site_packages, prompt, clear, upgrade, upgrade_deps, requirements,install_requirements):
    if os.name == 'nt':
        symlinks = False
    else:
        symlinks = True
    builder = create_env.BuildEnv(path = path, system_site_packages = system_site_packages, prompt = prompt, with_pip = with_pip, clear = clear, symlinks = symlinks, upgrade = upgrade, upgrade_deps = upgrade_deps)
    builder.apply()
    builder.create(path)

