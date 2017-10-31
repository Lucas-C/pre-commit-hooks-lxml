from __future__ import print_function
import argparse, sys
from lxml.etree import iterparse


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    parser.add_argument('--forbidden-tags', type=lambda s: s.split(','), default=[],
                        help='Comma-separated list of forbidden HTML tag names')
    args = parser.parse_args(argv)
    matches = list(iterate_forbidden_tags(args.filenames, args.forbidden_tags))
    return_error_code = 0
    for filename, tag_name in matches:
        print('Forbidden HTML tag "{}" found in {}'.format(tag_name, filename))
        return_error_code = 1
    return return_error_code

def iterate_forbidden_tags(html_filenames, forbidden_tags):
    forbidden_tags = set(forbidden_tags)
    for html_filename in html_filenames:
        with open(html_filename, 'rb') as html_file:
            for _, elem in iterparse(html_file, html=True, remove_comments=True):
                if elem.tag in forbidden_tags:
                    yield html_filename, elem.tag  # sadly elem.sourceline is None :(

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
