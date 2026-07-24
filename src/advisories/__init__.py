'''Init module.'''

import argparse
from advisories import debian


def parse_args():
    '''Parse commandline arguments.'''

    parser = argparse.ArgumentParser(
        prog = 'advisories',
        description = 'Pulls security advisories from various distros.'
    )

    parser.add_argument('-d', '--distro', help = 'Specify distribution to get security advisories for.')

    return parser.parse_args()


def run():
    '''Run the program.'''

    args = parse_args()
    if not args.distro:
        args.distro = 'all'

    if args.distro == 'all' or args.distro == 'debian':
        debian.fetch()
