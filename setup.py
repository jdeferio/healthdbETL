try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DISTNAME = "healthdbETL"
AUTHOR = "Joseph Deferio"
EMAIL = "jdeferio.io@gmail.com"
DESCRIPTION = "ETL and Database Interaction Tools for HealthDB"
URL = "https://github.com/jdeferio/healthdbETL"

setup(
    name=DISTNAME,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    packages=['healthdbetl'],
    install_requires=[ 
        'sqlalchemy',
        'python-dotenv'
        ],
    version='0.1.0',
    license='LICENSE.txt',
    description=DESCRIPTION,
    long_description=open('README.rst').read(),
)
