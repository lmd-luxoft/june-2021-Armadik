#!/usr/bin/env python2
import argparse
import server.FileService as fs

__version__ = "0.0.1"


def parse_args():
    """Command line parser."""
    parser = argparse.ArgumentParser(description='Actions ')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-f', '--folder', help='work dir', default="test_folder")

    subparsers = parser.add_subparsers(help='sub-commands')

    create_parser = subparsers.add_parser('create', help='Create file')
    create_parser.add_argument('file_name', nargs='?', help='New file', default="test.txt")

    delete_parser = subparsers.add_parser('delete', help='Delete file')
    delete_parser.add_argument('file_name', help='Delete file', default="test.txt")

    read_parser = subparsers.add_parser('read', help='Read file')
    read_parser.add_argument('file_name', help='Read file', default="test.txt")

    list_parser = subparsers.add_parser('list', help='Show files')

    data_parser = subparsers.add_parser('data', help='Show files')
    data_parser.add_argument('file_name', help='Show data file', default="test.txt")

    create_parser.set_defaults(func=fs.create_file)
    read_parser.set_defaults(func=fs.read_file)
    delete_parser.set_defaults(func=fs.delete_file)
    list_parser.set_defaults(func=fs.get_files)
    data_parser.set_defaults(func=fs.get_file_data)

    return parser.parse_args()


def main():
    """Entry point of app.
    """
    args = parse_args()
    args.func(args)
    print(fs.read_file(args))


if __name__ == '__main__':
    main()
