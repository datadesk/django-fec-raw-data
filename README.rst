=====
fec-raw
=====

fec-raw is a Django app to download FEC campaign finance filings
and load them into a database. It relies on the New York Times
Fech library to download filings as CSV files, then loads them
into a database preserving all the fields in the raw data.


Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'fec-raw',
    )

3. Run `python manage.py migrate` to create the raw models.

4. Run `python manage.py download` to download FEC filings.

5. Run `python manage.py load` to load them into the database.