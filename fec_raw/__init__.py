import os
from django.conf import settings


def get_download_directory():
    """
    Returns the download directory where we will store downloaded data.
    """
    if hasattr(settings, 'FEC_DOWNLOAD_DIR'):
        return getattr(settings, 'FEC_DOWNLOAD_DIR')
    elif hasattr(settings, 'BASE_DIR'):
        return os.path.join(getattr(settings, 'BASE_DIR'), 'data')
    raise ValueError("CAL-ACCESS download directory not configured. Set either \
FEC_DOWNLOAD_DIR or BASE_DIR in settings.py")
