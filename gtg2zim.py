# -*- coding: utf-8 -*- #

"""GtG2Zim - Exports GTG tasks to Zim Desktop Wiki pages.

Usage:
    gtg2zim.py TAG [-i PATH] [-o PATH]
    gtg2zim.py (-h | --help)
    gtg2zim.py --version

Arguments:
    TAG                       The GTG Tag to filter by - only export tasks with this tag

Options:
    -o PATH, --output=PATH    The output folder to save the Zim pages to. [default: ./]
    -i PATH, --input=PATH     The input folder where the gtg files are. [default: ~/.local/share/gtg]
    -h --help                 Show this screen.
    --version                 Show version.

"""
from docopt import docopt
import os
from datetime import datetime


def create_zim_notebook(name, output_path):
    """Create a ZIM Notebook in the output folder, with the given name."""

    # Make a notebook folder inside output_path
    notebook_folder = os.path.join(output_path, name.replace(' ', '_'))
    if not os.path.exists(notebook_folder):
        os.makedirs(notebook_folder)

    # Create the notebook.zim index file
    nb = '[Notebook]\nname={0}\nversion=0.4\nendofline=unix\nprofile=None\n'.format(name)
    with open(os.path.join(notebook_folder, 'notebook.zim'), 'w+') as f:
        f.write(nb)

    # Create notebook file
    d = datetime.now()
    nb = 'Content-Type: text/x-zim-wiki\nWiki-Format: zim 0.4\nCreation-Date: {:%Y-%m-%dT%H:%M:%S%z}\n\n====== {} ======\nCreated {:%A %d %B %Y}\n'.format(d, name, d)
    with open(os.path.join(notebook_folder, name.replace(' ', '_') + '.txt'), 'w+') as f:
        f.write(nb)


def gtg2zim(tag, input_path, output_path):
    print tag, output_path, input_path
    create_zim_notebook('Test Notebook', output_path)

    # Check for existence of gtg files in input_path:
    #   tags.xml
    #   projects.xml
    #   gtg_tasks-*.xml
    #
    # Read in tags.xml
    # For each tag, create a ZIM Notebook in the output folder.
    #
    # Read in gtg projects.xml file
    #
    # For each <backend..> where module="backend_localfile", read in the file pointed to by the path attribute

if __name__ == '__main__':
    args = docopt(__doc__, version='GtG2Zim 0.1')

    # print args

    if args['--output'] and args['--input']:
        if os.path.isdir(os.path.expanduser(args['--output'])) and os.path.isdir(os.path.expanduser(args['--input'])):
            # TODO: Check that we can write to output folder
            output_path = os.path.expanduser(args['--output'])
            input_path = os.path.expanduser(args['--input'])
            gtg2zim(args['TAG'], input_path, output_path)
