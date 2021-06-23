#!/usr/bin/env python2
import argparse
import server.FileService as FileService

__version__ = "0.0.1"

def parse_args():
    """Command line parser."""
    parser = argparse.ArgumentParser(description='Actions ')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-f', '--folder', help='work dir', default="test_folder")

    subparsers = parser.add_subparsers(help='sub-commands')

    create_parser = subparsers.add_parser('create', help='Create file')
    create_parser.add_argument('file_name',nargs='?', help='New file', default="test.txt")

    delete_parser = subparsers.add_parser('delete', help='Delete file')
    delete_parser.add_argument('file_name', help='Delete file', default="test.txt")

    read_parser = subparsers.add_parser('read', help='Read file')
    read_parser.add_argument('file_name', help='Read file', default="test.txt")

    list_parser = subparsers.add_parser('list', help='Show files')

    data_parser = subparsers.add_parser('data', help='Show files')
    data_parser.add_argument('file_name', help='Show data file', default="test.txt")

    #params = parser.parse_args()
    #print(str(params))

    create_parser.set_defaults(func=FileService.create_file)
    read_parser.set_defaults(func=FileService.read_file)
    delete_parser.set_defaults(func=FileService.delete_file)
    list_parser.set_defaults(func=FileService.get_files)
    data_parser.set_defaults(func=FileService.get_file_data)

    return parser.parse_args()


def main():
    """Entry point of app.

    Get and parse command line parameters and configure web app.

    Command line options:
    -f --folder - working directory (absolute or relative path, default: current app folder).
    -h --help - help.
    """
    args = parse_args()
    args.func(args)

if __name__ == '__main__':
    main()