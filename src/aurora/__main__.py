import create_env
import os
import blessings
import aurora


t = Terminal()


def create_env(path, with_pip, system_site_packages, prompt, clear, upgrade, upgrade_deps, requirements,install_requirements):
    if os.name == 'nt':
        symlinks = False
    else:
        symlinks = True
    builder = create_env.BuildEnv(path = path, system_site_packages = system_site_packages, prompt = prompt, with_pip = with_pip, clear = clear, symlinks = symlinks, upgrade = upgrade, upgrade_deps = upgrade_deps)
    builder.apply()
    builder.create(path)

positive = ['yes', 'true', 'allow', 'y']
path = os.getcwd()
with_pip = True
system_site_packages = False
prompt = "Aurora:: " + os.path.dirname(path)
clear = False
upgrade = False
upgrade_deps = False
re = open('requirements.txt')
req = re.read().split('\n')
re.close()
requirements = []
for i in req:
    if i:
        requirements.append(i)
install_requirements = True

print(t.bold + "Aurora:: The beautiful environment sharing module for Python.")
print(t.bold + "Options:\n1. Run pipfile if present\n2. Create Virtual environment and pipfile\n3. Nothing." + t.normal)
try:
    opt = int(input("Enter the option code"))
except:
    print("Only integer values permitted!")
    print("Exiting. To run, rerun!")
else:
    if opt == 1:
        aurora.pipfile.execute(os.path.join(path, 'Pipfile'))
    elif opt == 2:
        if (input("Install pip? Yes/No").lower() in positive):
            with_pip = True
        else:
            with_pip = False
        if input("Upgrade dependencies? Yes/No").lower() not in positive:
            upgrade_deps
        if input("Use --upgrade flag for venv creation? Yes/No").lower() in positive:
            upgrade = True
    elif opt == 3:
        print("Exiting.")
    else:
        print("Invalid option.\nExit triggered.")