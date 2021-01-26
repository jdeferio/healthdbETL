## __HealthDB ETL__ ##

#### ETL and Database Interaction Tools for HealthDB
<br />

__What is it?__ 

healthdbETL is a python package that contains tools for interacting with the [HealthDB](https://github.com/jdeferio/healthdbModels/) database. Functions currently include connecting to the database and loading data in chunks.

<br />

__Where to get it:__


The source code is currently hosted on GitHub at:
https://github.com/jdeferio/healthdbETL

Binary installers for the latest released version are _not_ currently available, but the package can be installed using either [Pip](https://pip.pypa.io/en/stable/), [Poetry](https://python-poetry.org) or a package manager of your choosing. 

```sh
# pip
pip install git+https://www.github.com/jdeferio/healthdbETL
```

```sh
# or poetry
poetry add git+https://www.github.com/jdeferio/healthdbETL
```
<br />

__Dependencies:__

- [SQLAlchemy - allows the user to interact with the ORM on which the database is modeled](https://www.sqlalchemy.org)

<br />

__License:__ [MIT](LICENSE.txt)