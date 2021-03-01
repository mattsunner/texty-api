from distutils.core import setup
import re

with open('README.md') as fp:
    long_description = fp.read()


def find_version():
    with open('parser-app/__init__.py') as fp:
        for line in fp:
            match = re.search(r"__version__\s*=\s*'([^']+)'", line)
            if match:
                return match.group(1)
    assert False, 'cannot find version'


setup(
    name='texty-API',
    version=find_version(),
    author='Matthew Sunner',
    author_email='matt@mattsunner.com',
    license='LICENSE.txt',
    description='API to Perform Simple Text Pre-Processing',
    long_description=long_description,
    packages=['parser-app']
)
