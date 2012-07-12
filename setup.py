from distutils.core import setup

setup(
    name='PyGridspot',
    version='0.0.1',
    author='Amir Elaguizy',
    author_email='aelaguiz@gmail.com',
    packages=['pygridspot', 'pygridspot.v1', 'pygridspot.test'],
    scripts=[],
    url='https://github.com/aelaguiz/pygridspot',
    license='LICENSE.txt',
    description='Client for the Gridspot computing service.',
    long_description=open('README.md').read(),
    install_requires=[
        "Fabric >= 1.4.3",
        "httplib2 >= 0.7.4"
    ],
)
