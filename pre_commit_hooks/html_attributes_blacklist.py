from __future__ import print_function
import argparse, sys
from lxml.etree import iterparse


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    parser.add_argument('--forbidden-attributes', type=lambda s: s.split(','), default=[],
                        help='Comma-separated list of forbidden attribute names')
    args = parser.parse_args(argv)
    matches = list(iterate_forbidden_attributes(args.filenames, args.forbidden_attributes))
    return_error_code = 0
    for filename, attr_name in matches:
        print('Forbidden HTML attribute "{}" found in {}'.format(attr_name, filename))
        return_error_code = 1
    return return_error_code

def iterate_forbidden_attributes(html_filenames, forbidden_attributes):
    forbidden_attributes = set(forbidden_attributes)
    for html_filename in html_filenames:
        with open(html_filename, 'rb') as html_file:
            for _, elem in iterparse(html_file, html=True, remove_comments=True):
                for attribute_name in elem.attrib.keys():
                    if attribute_name in forbidden_attributes:
                        yield html_filename, attribute_name  # sadly elem.sourceline is None :(


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
