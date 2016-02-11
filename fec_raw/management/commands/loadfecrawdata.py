import os
from django.conf import settings
from postgres_copy import CopyMapping
from fec_raw import get_download_directory
from string import ascii_letters, punctuation
from fec_raw.management.commands import FecCommand
from fec_raw.models import RawF3XFiling, RawF3PFiling, RawF24Filing
from fec_raw.models import RawContribution, RawIndependentExpenditure


class Command(FecCommand):
    help = "Load downloaded filings into database"
    DATA_DIR = get_download_directory()

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
        self.header("Load raw FEC filings")
        name_to_model = {
            "F3X": RawF3XFiling,
            "F3P": RawF3PFiling,
            "F24": RawF24Filing,
            "sa": RawContribution,
            "se": RawIndependentExpenditure,
        }

        if options['flush']:
            self.log('Flushing the DB')
            for model in name_to_model.values():
                model.objects.all().delete()

        # Characters to strip from filenames to get filing number
        ignore = ascii_letters + punctuation
        loaded = 0

        for name, model in name_to_model.items():
            data_dir = os.path.join(self.DATA_DIR, name)
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
                        self.log(
                            '{} CSV for filing {} is already in the DB'.format(
                                name,
                                filing_no
                            )
                        )
                    else:
                        self.log(
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
                            self.failure('Error on {} CSV for filing {}'.format(name, filing_no))

        self.success("Loaded {} CSVs".format(loaded))
