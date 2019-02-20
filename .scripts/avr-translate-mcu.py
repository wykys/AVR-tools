#!/usr/bin/env python3
# wykys 2018
# The script translates the names of the microcontrollers
# used by the AVR toolchain into the format for avrdude.

import sys
import argparse
from avr import Database, NotDefinedMCUError


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='avr-transtale-mcu',
        description='The script parses the memory information from the linker '
        'script and the size program, and then displays them in a more readable form.'
    )
    parser.add_argument(
        '-m',
        '--mcu',
        dest='mcu',
        action='store',
        default=None,
        help='the name of the microcontroller'
    )

    parser.add_argument(
        '-f',
        '--format',
        dest='format',
        action='store',
        default='avrdude',
        choices=['avrdude', 'define'],
        help='output string format, avrdude default'
    )

    try:
        print(Database.get_mcu(parser.parse_args().mcu)[parser.parse_args().format])

    except NotDefinedMCUError as e:
        print(str(e), file=sys.stderr)
        Database.print_table()
        exit(-1)
