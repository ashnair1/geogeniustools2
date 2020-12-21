from distutils.core import setup
from pathlib import Path

NAME = "geogeniustools2"

# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR

# What packages are required for this module to be executed?
def list_reqs(fname='requirements.txt'):
    with open(fname) as f:
        requirements = f.read().splitlines()

    required = []
    dependency_links = []
    # do not add to required lines pointing to git repositories
    EGG_MARK = '#egg='
    for line in requirements:
        if line.startswith('-e git:') or line.startswith('-e git+') or \
                line.startswith('git:') or line.startswith('git+'):
            if EGG_MARK in line:
                package_name = line[line.find(EGG_MARK) + len(EGG_MARK):]
                # Ignore possible subdirectories
                if '&' in package_name:
                    package_name = package_name[0:package_name.find('&')]
                required.append(package_name)
                dependency_links.append(line)
            else:
                print('Dependency to a git repository should have the format:')
                print('git+ssh://git@github.com/xxxxx/xxxxxx#egg=package_name')
        else:
            required.append(line)

    return required, dependency_links

required, dependency_links = list_reqs()

setup(
    name=NAME,
    packages=[
        "geogeniustools2",
    ],
    install_requires=required,
)