# django-fec-raw-data

A Django app to download, extract and load campaign finance from the Federal Election Commission.

It relies on the New York Times Fech library to download filings as CSV files, then loads them
into a database preserving all the fields in the raw data.

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
$ python manage.py download
```

Load them into the database.

```bash
$ python manage.py load
```
