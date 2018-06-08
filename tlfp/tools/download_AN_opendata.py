import sys

from anpy.dossier_from_opendata import download_open_data_doslegs

from .common import download_daily


def download_AN_opendata(legislature):
    def _download():
        return download_open_data_doslegs(legislature)
    return _download


def process(output_directory):
    all_data = {}
    for legislature in 14, 15:
        all_data[legislature] = download_daily(download_AN_opendata(legislature), 'opendata_AN_dossiers_%d' % legislature, output_directory)
    return all_data


if __name__ == '__main__':
    process(sys.argv[1])
