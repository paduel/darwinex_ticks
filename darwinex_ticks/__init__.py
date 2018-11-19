# -*- coding: utf-8 -*-

import argparse
import configparser
from core import *

__version__ = "0.1.1"
__author__ = "Antonio Rodriguez (Paduel)"


def download(args=None):
    args = argparser(args)

    if not args.user:
        try:
            _config = configparser.ConfigParser()
            _config.read('darwinex_ticks.cfg')
            args.user = _config['Server']['user']
            args.password = _config['Server']['password']
            args.hostname = _config['Server']['hostname']
            args.port = int(_config['Server']['port'])
        except KeyError:
            raise ValueError('user and password must be passed as arguments')

    if not args.path:
        try:
            _config = configparser.ConfigParser()
            _config.read('darwinex_ticks.cfg')
            args.path = _config['File']['path']
        except KeyError:
            args.path = ''

    _dwt = DarwinexTicksConnection(dwx_ftp_user=args.user,
                                   dwx_ftp_pass=args.password,
                                   dwx_ftp_hostname=args.hostname,
                                   dwx_ftp_port=args.port)

    _data = _dwt.ticks_from_darwinex(args.assets, start=args.start,
                                     end=args.end,
                                     cond=args.condition, verbose=False,
                                     side='both', separated=False,
                                     fill=True, darwinex_time=args.dwtime)

    for _asset in args.assets:
        _filename = _get_filename(args)
        if args.path:
            _path = args.path + '/' if args.path[-1] != '/' else args.path
        else:
            _path = ''
        _filename = '{}{}_{}.csv'.format(_path, _asset, _filename)
        _data.loc[_asset].dropna().to_mtcsv(_filename)
        print('Saved file {}'.format(_filename))

    _dwt.close()

    if args.config_save:
        _config = configparser.ConfigParser()
        _config['Server'] = {'user': args.user,
                             'password': args.password,
                             'hostname': args.hostname,
                             'port': args.port}
        _config['File'] = {'path': args.path}
        with open('darwinex_ticks.cfg', 'w') as archivoconfig:
            _config.write(archivoconfig)
        print('Config saved')

    return


def _get_filename(args):
    if args.condition:
        _filename = args.condition
    else:
        _filename = '{}_{}'.format(args.start, args.end)
    return _filename


def argparser(pargs=None):
    parser = argparse.ArgumentParser(
        description='Tool for download Darwinex ticks data'
    )
    parser.add_argument('assets', help='Assets to download tick data',
                        nargs='+')
    parser.add_argument('--user', '-u', help='Darwinex ftp service user name')
    parser.add_argument('--password', '-w', help='Darwinex ftp service '
                                                 'password')
    parser.add_argument('--hostname', '-n', default='tickdata.darwinex.com',
                        help='Darwinex ftp host name')
    parser.add_argument('--port', '-p', default=21, help='Darwinex ftp port '
                                                         'number', type=int)

    parser.add_argument('--path', '-f', help='path to save the csv files'
                                             'the downloaded data')
    parser.add_argument('--condition', '-c', help='Datetime condition e.g. '
                                                  '"2018-10"')
    parser.add_argument('--start', '-s', help='Start of period to download, '
                                              'if a condition is passed, '
                                              'start is ignored')
    parser.add_argument('--end', '-e', help='End of period to download, '
                                            'if a condition is passed, '
                                            'start is ignored')
    parser.add_argument('--dwtime', '-t', help='Use darwinex time, False use '
                                               'UTC', type=bool,
                        default=True, nargs='?')
    parser.add_argument('-g', '--config_save', help='Save ftp server params '
                                                    'and path at config file',
                        action='store_true')

    args = parser.parse_args(pargs)
    return args


if __name__ == '__main__':
    download()
