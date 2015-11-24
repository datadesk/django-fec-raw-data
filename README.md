# django-fec-raw-data

A Django app to download, extract and load campaign finance from the Federal Election Commission.

It relies on the New York Times [Fech](http://nytimes.github.io/Fech/) library to download filings as CSV files, then loads them
into a database preserving all the fields in the raw data.


[![Build Status](https://travis-ci.org/datadesk/django-fec-raw-data.png?branch=master)](https://travis-ci.org/california-civic-data-coalition/django-fec-raw-data)
[![PyPI version](https://badge.fury.io/py/django-fec-raw-data.png)](http://badge.fury.io/py/django-fec-raw-data)
[![Coverage Status](https://coveralls.io/repos/datadesk/django-fec-raw-data/badge.png?branch=master)](https://coveralls.io/r/california-civic-data-coalition/django-fec-raw-data?branch=master)

* Issues: [github.com/datadesk/django-fec-raw-data/issues](https://github.com/datadesk/django-fec-raw-data/issues)
* Packaging: [pypi.python.org/pypi/django-fec-raw-data](https://pypi.python.org/pypi/django-fec-raw-data)
* Testing: [travis-ci.org/datadesk/django-fec-raw-data](https://travis-ci.org/datadesk/django-fec-raw-data)
* Coverage: [coveralls.io/r/datadesk/django-fec-raw-data](https://coveralls.io/r/datadesk/django-fec-raw-data)


## Quick start

Add this app to your ``INSTALLED_APPS`` in ``settings.py``.

```python
    INSTALLED_APPS = (
        ...
        'fec_raw',
    )
```

Create the raw models.

```bash
$ python manage.py migrate
```

Download the FEC filings.

```bash
$ python manage.py downloadfecrawdata
```

Load them into the database.

```bash
$ python manage.py loadfecrawdata
```
