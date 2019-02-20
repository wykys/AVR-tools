#!/usr/bin/env python3
# wykys 2019
# Returns the string created from the header file commentary.

import argparse


def desc(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()

    doc = []
    for line in lines:
        if line[0] is '#':
            if not ('wykys' in line) and not ('#!/' in line):
                if len(doc):
                    doc.append(' ')
                doc.append(line[1:-1].strip())
        else:
            break

    return ''.join(doc)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='desc',
        description=desc(__file__)
    )
    parser.add_argument(
        '-p',
        '--path',
        dest='path',
        action='store',
        default=__file__,
        help='the path of the python file'
    )

    print(desc(parser.parse_args().path))
