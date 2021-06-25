#!/usr/bin/env python2
import argparse
import logging
import os
import config

import server.FileService as fs

__version__ = "0.0.1"
LOGGER = logging.getLogger(__name__)


def parse_args():
    """Command line parser."""

    debug_parser = argparse.ArgumentParser(add_help=False)

    debug_options = debug_parser.add_argument_group("Debug Options")
    debug_options.add_argument('-l', '--logfile', metavar='filename', type=argparse.FileType('wb', 0), default='-',
                               help='Specify the logfile (default: <stdout>)')
    group = debug_options.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='disable logging')
    group.add_argument('-v', '--verbose', action='store_true', help='enhanced logging')
    group.add_argument('-d', '--debug', action='store_true', help='extensive logging')

    parser = argparse.ArgumentParser(description='Actions ')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-f', '--folder', help='work dir', default="test_folder")

    subparsers = parser.add_subparsers(help='sub-commands')

    create_parser = subparsers.add_parser('create', help='Create file', parents=[debug_parser])
    create_parser.add_argument('file_name', nargs='?', help='New file', default="test.txt")

    delete_parser = subparsers.add_parser('delete', help='Delete file', parents=[debug_parser])
    delete_parser.add_argument('file_name', help='Delete file', default="test.txt")

    read_parser = subparsers.add_parser('read', help='Read file', parents=[debug_parser])
    read_parser.add_argument('file_name', help='Read file', default="test.txt")

    list_parser = subparsers.add_parser('list', help='Show files', parents=[debug_parser])

    data_parser = subparsers.add_parser('data', help='Show files', parents=[debug_parser])
    data_parser.add_argument('file_name', help='Show data file', default="test.txt")

    create_parser.set_defaults(func=fs.create_file)
    read_parser.set_defaults(func=fs.read_file)
    delete_parser.set_defaults(func=fs.delete_file)
    list_parser.set_defaults(func=fs.get_files)
    data_parser.set_defaults(func=fs.get_file_data)

    options = parser.parse_args()

    return options


def main():
    """Entry point of app.
    """
    options = parse_args()

    if options.quiet:
        logfile = open(os.devnull, 'a')
        loghandler = logging.StreamHandler(logfile)
        loglevel = logging.NOTSET
    elif options.debug:
        logformat = '%(asctime)s,%(msecs)-3d %(levelname)-8s %(message)s'
        timeformat = '%y/%m/%d %H:%M:%S'
        loghandler = logging.StreamHandler(options.logfile)
        loghandler.setFormatter(logging.Formatter(logformat, timeformat))
        loglevel = logging.DEBUG
    elif options.verbose:
        logformat = '%(asctime)s,%(msecs)-3d %(levelname)-8s %(message)s'
        timeformat = '%y/%m/%d %H:%M:%S'
        loghandler = logging.StreamHandler(options.logfile)
        loghandler.setFormatter(logging.Formatter(logformat, timeformat))
        loglevel = logging.INFO
    else:
        logformat = '%(asctime)s,%(msecs)-3d %(levelname)-8s %(message)s'
        timeformat = '%y/%m/%d %H:%M:%S'
        loghandler = logging.StreamHandler(options.logfile)
        loghandler.setFormatter(logging.Formatter(logformat, timeformat))
        loglevel = logging.WARNING

    config.loglevel = loglevel
    config.loghandler = loghandler

    log = logging.getLogger("__name__")
    log.setLevel(loglevel)
    log.addHandler(loghandler)
    "Test log out"
    log.error('example of error message')
    log.warning('example of warning message')
    log.info('example of information message')
    log.debug('example of debug message')

    options.func(options)

    # print(fs.read_file(args))  # добавить условие?


if __name__ == '__main__':
    main()
