#!/usr/bin/env python3
# wykys 2018
# The script translates the names of the microcontrollers
# used by the AVR toolchain into the format for avrdude.
# Another option is to translate the gcc parameter -mmcu
# to define for <avr/io.h>.

import sys
import argparse
from desc import desc
from avr import Database, NotDefinedMCUError


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='avr-transtale-mcu',
        description=desc(__file__)
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
        print(Database.get_mcu(parser.parse_args().mcu)
              [parser.parse_args().format])

    except NotDefinedMCUError as e:
        print(str(e), file=sys.stderr)
        Database.print_table()
        exit(-1)
