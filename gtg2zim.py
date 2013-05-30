# -*- coding: utf-8 -*- #

"""GtG2Zim - Exports GTG tasks to Zim Desktop Wiki pages.

Usage:
    gtg2zim.py TAG [-o PATH]
    gtg2zim.py (-h | --help)
    gtg2zim.py --version

Arguments:
    TAG                       The GTG Tag to filter by - only export tasks with this tag

Options:
    -o PATH, --output=PATH    The output folder to save the Zim pages to. [default: ./]
    -h --help                 Show this screen.
    --version                 Show version.

"""
from docopt import docopt
import os


def gtg2zim(tag, output_path):
    pass

if __name__ == '__main__':
    args = docopt(__doc__, version='GtG2Zim 0.1')

    if args['--output']:
        try:
            output_path = os.path.isdir(args['--output'])
            gtg2zim(args['TAG'], output_path)

        except IOError, e:
            print e
