from __future__ import print_function
import argparse, os, re, sys
from lxml.etree import iterparse
from tinycss2 import parse_stylesheet_bytes

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    parser.add_argument('--css-files-dir', required=True,
                        help='Directories containing CSS files to check')
    parser.add_argument('--css-lib-files-dir', default='',
                        help='Directories containing CSS files of librairies: unused classes from those files will not be reported')
    parser.add_argument('--html-files-dir', required=True,
                        help='Directories containing HTML files to check')
    parser.add_argument('--ignored-missing-class-defs-pattern',
                        help='Regular expression matching CSS class names')
    parser.add_argument('--ignored-unused-class-defs-pattern',
                        help='Regular expression matching CSS class names')
    args = parser.parse_args(argv)

    html_files = []
    for directory in args.html_files_dir.split(','):
        html_files.extend(scandir(directory, ('.hbs', '.html')))
    searched = 'directories {}'.format(args.html_files_dir) if ',' in args.html_files_dir else 'directory {}'.format(args.html_files_dir)
    print('{} HTML files found in {}'.format(len(html_files), searched))
    css_files = []
    for directory in args.css_files_dir.split(','):
        css_files.extend(scandir(directory, ('.css',)))
    searched = 'directories {}'.format(args.css_files_dir) if ',' in args.css_files_dir else 'directory {}'.format(args.css_files_dir)
    print('{} CSS files found in {}'.format(len(css_files), searched))
    css_lib_files = []
    for directory in args.css_lib_files_dir.split(','):
        css_lib_files.extend(scandir(directory, ('.css',)))
    searched = 'directories {}'.format(args.css_lib_files_dir) if ',' in args.css_lib_files_dir else 'directory {}'.format(args.css_lib_files_dir)
    print('{} library CSS files found in {}'.format(len(css_lib_files), searched))

    css_classes_used = set(sum([list(extract_css_classes_usages(html_file)) for html_file in html_files], []))
    print('Found {} CSS classes usages in HTML files'.format(len(css_classes_used)))
    css_classes_defined = set(sum([list(extract_css_classes_definitions(css_file)) for css_file in css_files], []))
    print('Found {} CSS classes definitions in CSS files'.format(len(css_classes_defined)))
    css_lib_classes_defined = set(sum([list(extract_css_classes_definitions(css_lib_file)) for css_lib_file in css_lib_files], []))
    print('Found {} CSS classes definitions in library CSS files'.format(len(css_lib_classes_defined)))

    unused_css_classes = css_classes_defined - css_classes_used
    if args.ignored_unused_class_defs_pattern:
        unused_css_classes = sorted(css_class for css_class in unused_css_classes
                                    if not re.search(args.ignored_unused_class_defs_pattern, css_class))
    missing_css_classes = css_classes_used - css_classes_defined - css_lib_classes_defined
    if args.ignored_missing_class_defs_pattern:
        missing_css_classes = sorted(css_class for css_class in missing_css_classes
                                     if not re.search(args.ignored_missing_class_defs_pattern, css_class))

    return_error_code = 0
    for css_class in unused_css_classes:
        print('WARNING: No usage found for CSS class {}'.format(css_class))
    for css_class in missing_css_classes:
        print('ERROR: Missing definition for CSS class {}'.format(css_class))
        return_error_code = 1
    return return_error_code

def scandir(dirname, file_extensions):
    for dirpath, _, fnames in os.walk(dirname):
        for fname in fnames:
            if any(fname.endswith(ext) for ext in file_extensions):
                yield os.path.join(dirpath, fname)

def extract_css_classes_definitions(css_file):
    with open(css_file, 'rb') as open_file:
        rules, _ = parse_stylesheet_bytes(open_file.read())
    next_is_class_name = False
    while rules:
        rule = rules.pop(0)
        if rule.type == 'at-rule' and rule.content:
            rules.extend(rule.content)
        elif rule.type == 'qualified-rule':
            rules.extend(rule.prelude)
        elif rule.type == 'ident' and next_is_class_name:
            yield rule.value
        next_is_class_name = (rule.type == 'literal' and rule.value == '.')

def extract_css_classes_usages(html_file):
    # CAN BE IMPROVED: extract (data-)ng-class & (data-)ng-style
    for _, elem in iterparse(html_file, html=True, remove_comments=True):
        if 'class' not in elem.attrib.keys():
            continue
        for css_class in elem.attrib['class'].split(' '):
            if css_class:
                yield css_class

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
