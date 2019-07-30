#!/usr/bin/env python3
# wykys 2018
# The script changes MCU in project files.

import sys
import json
from avr import Database, NotDefinedMCUError


PATH_MAKEFILE = 'Makefile'
PATH_VSCODE = '.vscode/c_cpp_properties.json'


def makefile_mcu(mcu=None):
    with open(PATH_MAKEFILE, 'r') as fr:
        data = fr.readlines()

    for i, line in enumerate(data):
        if 'CHIP =' in line:
            if mcu is None:
                return line.split('=')[1].strip()
            else:
                data[i] = 'CHIP = {}\n'.format(mcu)
                break

    if not (mcu is None):
        with open(PATH_MAKEFILE, 'w') as fw:
            data = fw.writelines(data)


def vscode_mcu(mcu=None):
    with open(PATH_VSCODE, 'r') as fr:
        data = json.load(fr)

    for i, define in enumerate(data['configurations'][0]['defines']):
        if '__AVR_' in define:
            if mcu is None:
                return define[6:-2].lower()
            else:
                break

    if not (mcu is None):
        data['configurations'][0]['defines'][i] = mcu
        data = json.dumps(data, indent=4, sort_keys=True)

        with open(PATH_VSCODE, 'w') as fw:
            fw.write(data)


if __name__ == '__main__':
    try:
        print('Makefile MCU: {}'.format(makefile_mcu()))
        print('VS Code  MCU: {}'.format(vscode_mcu()))

        mcu_name = input('Enter new MCU >>> ')
        mcu = Database.get_mcu(mcu_name)
        print(mcu)

        makefile_mcu(mcu_name)
        vscode_mcu(mcu.define)

    except NotDefinedMCUError as e:
        print(str(e), file=sys.stderr)
        Database.print_table()
        exit(-1)
