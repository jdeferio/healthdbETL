try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='healthdbETL',
    url='https://github.com/jdeferio/healthdbETL',
    author='Joseph Deferio',
    author_email='jdeferio.io@gmail.com',
    packages=['healthdbetl'],
    install_requires=[ 
        'sqlalchemy',
        ],
    version='0.1.0',
    license='LICENSE.txt',
    description='ETL and Database Interaction Tools for HealthDB',
    long_description=open('README.rst').read(),
)
