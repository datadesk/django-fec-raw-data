"""
Custom field overrides that allow for cleaning and transforming the data
when it is bulk loaded into the database with PostgreSQL's COPY command via
django-postgres-copy.
"""
from django.db.models import fields

class DecimalField(fields.DecimalField):
    copy_type = 'text'
    copy_template = """
    CASE
        WHEN "%(name)s" IS NULL
            THEN 0
        WHEN "%(name)s" IS NOT NULL
            THEN CAST("%(name)s" AS decimal(16,2))
    END
    """

class IntegerField(fields.IntegerField):
    copy_type = 'text'
    copy_template = """
    CASE
        WHEN "%(name)s" IS NULL
            THEN 0
        WHEN "%(name)s" IS NOT NULL
            THEN CAST("%(name)s" AS INTEGER)
    END
    """

class CharField(fields.CharField):
    copy_type = 'text'
    copy_template = """
    CASE
        WHEN "%(name)s" IS NULL
            THEN ''
        ELSE UPPER(TRIM(BOTH ' ' from %(name)s))
    END
    """