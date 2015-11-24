import os
import subprocess
import feedparser
from tomorrow import threads
from django.conf import settings
from fec_raw import get_download_directory
from fec_raw.management.commands import FecCommand



class Command(FecCommand):
    help = "Download FEC filings to data directory"
    # Path to ruby script that uses Fech to save a filing
    FECH_PATH = os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        ),
        'fech_filing.rb'
    )
    # If there are no downloaded filings
    DEFAULT_FIRST_FILING = 1000000
    # Where to download files
    DATA_DIR = get_download_directory()

    def add_arguments(self, parser):
        parser.add_argument(
            '--filing',
            action='store',
            nargs=1,
            type=int,
            required=False,
            help='ID of single filing to retrieve',
            dest='filing'
        )
        parser.add_argument(
            '--first',
            '-f',
            action='store',
            nargs=1,
            type=int,
            required=False,
            help='ID of first record to be added',
            dest='first_record'
        )
        parser.add_argument(
            '--last',
            '-l',
            action='store',
            nargs=1,
            type=int,
            required=False,
            help='ID of last record to be added',
            dest='last_record'
        )
        parser.add_argument(
            '--force',
            action='store_true',
            dest='force',
            default=False,
            help='Force a reload of the filings',
        )

    def handle(self, *args, **options):
        """
        Determines the first and last filing numbers to download, either
        from the provided options or from get_latest_downloaded_filing_number
        and get_latest_filing_number. Loops through those records and, if it
        hasn't been previously downloaded, downloads it.
        """
        self.header("Downloading raw FEC filings")
        # Create the raw data directory if it doesn't exist
        raw_data_path = os.path.join(self.DATA_DIR, 'raw')
        os.path.exists(raw_data_path) or os.makedirs(raw_data_path)

        # Figure out which filings we're going to try to get
        # If we want a specific filing, set both the first and last record to
        # that filing
        if options['filing']:
            options['first_record'] = options['filing']
            options['last_record'] = options['filing']

        if options['first_record']:
            first_record = options['first_record'][0]
        else:
            first_record = self.get_latest_downloaded_filing_number() + 1

        if options['last_record']:
            last_record = options['last_record'][0]
        else:
            last_record = self.get_latest_filing_number()

        if first_record > last_record:
            self.failure('No records to download')
            return

        self.log(
            'Attempting to download filings {} to {}'.format(
                first_record,
                last_record
            )
        )
        # Loop through all filings we're interested in
        for filing_no in range(first_record, last_record + 1):
            # Create string version of the filing number
            filing_id = str(filing_no)

            # It should exist at this path
            filing_path = os.path.join(
                self.DATA_DIR,
                'raw',
                filing_id + '.fec'
            )

            # If it does AND we're not forcing a refresh ...
            if os.path.isfile(filing_path) and not options['force']:
                # Skip to the next record
                self.log('Already downloaded filing {}'.format(filing_id))
                continue
            # Otherwise ...
            else:
                # Interface with fech to get the data
                self.fech_filing(filing_id)

    @threads(getattr(settings, 'FEC_DOWNLOAD_THREADS', 4))
    def fech_filing(self, filing_no):
        """
        Interfaces with Ruby library Fech to return data for a particular filing
        number, saves data to CSVs in DATA_DIR
        """
        self.log('Fech-ing filing {}'.format(filing_no))

        p = subprocess.Popen(
            ['ruby', self.FECH_PATH, filing_no, self.DATA_DIR],
            stdout=subprocess.PIPE,
            stderr=None
        )

        # start the subprocess
        output = p.communicate()
        # this is the stdout of the ruby script
        message = output[0]

        # TODO: Refactor/fix the way this error handling works
        if message[0] == 'E':
            self.failure(' - Failed to download filing {}'.format(filing_no))
        elif message[0] == 'S':
            self.success(' - Downloaded filing {}'.format(filing_no))

    def get_latest_downloaded_filing_number(self):
        """
        Checks data directory to get latest previously downloaded
        filing number.
        """
        files = os.listdir(os.path.join(self.DATA_DIR, 'raw'))
        try:
            filing_numbers = [int(filename.split('.')[0]) for filename in files if not (filename.startswith('.') or filename.startswith('fech'))]
            return sorted(filing_numbers, reverse=True)[0]
        except:
            return self.DEFAULT_FIRST_FILING

    def get_latest_filing_number(self):
        """
        Uses FEC RSS feed to get the ID of the latest filing.
        """
        self.log('Getting latest filing number from FEC...')

        url = 'http://efilingapps.fec.gov/rss/generate?preDefinedFilingType=ALL'
        d = feedparser.parse(url)
        # Sorted entries by date, most recent first
        entries = sorted(
            d.entries,
            key=lambda entry: entry['published_parsed'],
            reverse=True
        )
        # Get filing ID from link that looks like:
        # http://docquery.fec.gov/dcdev/posted/1020510.fec
        link = entries[0]['link']
        latest = int(link.split('/')[-1].replace('.fec', ''))

        self.log('Latest filing number is {}'.format(latest))
        return latest
