import os
import logging
from django.conf import settings
from postgres_copy import CopyMapping
from string import ascii_letters, punctuation
from django.core.management.base import BaseCommand
from fec_raw.models import RawF3XFiling, RawF3PFiling, RawF24Filing
from fec_raw.models import RawContribution, RawIndependentExpenditure

logger = logging.getLogger('fec')


class Command(BaseCommand):
    help = "Load downloaded filings into database"

    def add_arguments(self, parser):
        parser.add_argument(
            '--flush',
            action='store_true',
            dest='flush',
            default=False,
            help='Flush the database and start anew',
        )

    def handle(self, *args, **options):
        """
        For each of the filing types we support, loops through the downloaded
        CSVs of that type, using the CopyMapping library to dump the records
        into the raw database, preserving all fields from the original data.
        """
        name_to_model = {
            "F3X": RawF3XFiling,
            "F3P": RawF3PFiling,
            "F24": RawF24Filing,
            "sa": RawContribution,
            "se": RawIndependentExpenditure,
        }

        if options['flush']:
            logger.info('Flushing the DB')
            for model in name_to_model.values():
                model.objects.all().delete()

        # Characters to strip from filenames to get filing number
        ignore = ascii_letters + punctuation
        loaded = 0

        for name, model in name_to_model.items():
            data_dir = os.path.join(settings.DATA_DIR, name)
            # If, for some reason, we have no filings of this type
            if not os.path.exists(data_dir):
                continue
            
            # We're making a mapping of CSV to model fields for CopyMapping
            # In this case, they're identical.
            mapping = {
                field: field for field in model._meta.get_all_field_names()
            }

            for file_name in os.listdir(data_dir):
                # Hidden files will mess with us
                if not file_name.startswith('.'):
                    # Remove our list of ignore characters from the file name
                    # to give us just the filing number.
                    filing_no = int(file_name.translate(None, ignore))
                    
                    if model.objects.filter(filing_no=filing_no).exists():
                        logger.info(
                            '{} CSV for filing {} is already in the DB'.format(
                                name,
                                filing_no
                            )
                        )
                    else:
                        logger.info(
                            'Loading {} CSV for filing {}'.format(
                                name,
                                filing_no
                            )
                        )
                        try:
                            c = CopyMapping(
                                model,
                                os.path.join(data_dir, file_name),
                                mapping
                            )
                            c.save(silent=True)
                            loaded += 1
                        except:
                            logger.error('Error on {} CSV for filing {}'.format(name, filing_no))

        logger.info("Loaded {} CSVs".format(loaded))
