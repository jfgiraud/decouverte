#!/usr/bin/python

import argparse
import difflib
import fileinput
import io
import os
import re
import sys
import time

def print_separator(text):
    if sys.version_info >= (3, 3, 0):
        import shutil
        columns = shutil.get_terminal_size().columns
    else:
        import subprocess
        tput = subprocess.Popen(['tput', 'cols'], stdout=subprocess.PIPE)
        columns = int(tput.communicate()[0].strip())
    sys.stderr.write('-- ' + text + ' ' + '-' * (columns - len(text) - 5) + '\n')

#def process_files(func, filepaths=[], inplace=False, confirm=False):
#    if len(filepaths) == 0:
#        filepaths = [ '-' ]
#    for path in filepaths:
#        if path == '-':
#            (filename, filepath) = ('<stdin>', 0)
#        else:
#            (filename, filepath) = (path, path)
#        if inplace:
#            if filepath == 0:
#                outfilepath = 1
#            else:
#                outfilepath = filepath + ".new"     
#        with io.open(filepath, 'r', encoding='utf-8') as ifd:
#            if not inplace or filepath == 0:
#                print_separator(filename)
#            else:
#                print("Process file %s..." % filename, file=sys.stderr)
#            with io.open(outfilepath, 'w', encoding='utf-8') as ofd:
#                for line in ifd:
#                    ofd.write(line)
#
#process_files(None, sys.argv[1:], True)
#
#sys.exit(1)
#        


def extract(search, replace, force, files):
    words = { search }
    with fileinput.input(files, mode='r') as fd:
        for line in fd:
            for word in re.findall(search, line, flags=re.IGNORECASE):
                words.add(word)
    for word in words:
        if word == search:
            result = replace
        elif word.istitle():
            result = replace.title()
        elif word.islower() or (force and word[0].islower()):
            result = replace.lower()
        elif word.isupper() or (force and word[0].isupper()):
            result = replace.upper()
        elif force:
            result = replace
        else:
            result = ''
        print('%s: %s' % (word, result))


def replace(mapping_file, files, simulate):
    mapping = {}
    missing = set()
    with io.open(mapping_file, 'r', encoding="UTF-8") as fd:
        for line in fd:
            (k, v) = [x.strip() for x in line.split(':', 2)]
            mapping[k]=v
            if not v:
                missing.add(k)
    if missing:
        print("Missing mapping entry. Please edit file '%s' and complete it." % mapping_file, file=sys.stderr)
        sys.exit(1)
    else:
        func = lambda matchobj: mapping[matchobj.group(0)]
        pattern = '(' + '|'.join(mapping.keys()) + ')'
        inplace=not simulate
        with fileinput.input(files, inplace=inplace) as fd:
            for line in fd:
                if not inplace and fileinput.isfirstline():
                    filename = fileinput.filename()
                    print_separator(filename)
                sys.stdout.write(re.sub(pattern, func, line))

       
 
def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     add_help=True,
                                     description='Perform replacement in FILE(s) or standard input.', 
                                     epilog='''---\nWritten by Jean-François Giraud.\n\nCopyright © 2012-2014 Jean-François Giraud.\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.''')

    #parser.add_argument('files', metavar='FILE', type=str, nargs='*', help='a file to modify')

    subparsers = parser.add_subparsers(help='Help for subcommand', dest='command')

    parser_extract = subparsers.add_parser('extract', help='Extract matches to a translation map')
            
    parser_extract.add_argument('--force', help="Force a default replace entry for all matches", action='store_true')
    parser_extract.add_argument('search', metavar='SEARCH', help='The string to search (ignoring case)')
    parser_extract.add_argument('replacement', metavar='REPLACEMENT', help='The string used to initialize values of the translation map')
    parser_extract.add_argument('files', metavar='FILE', type=str, nargs='*', help='The file(s) where performing operation')

    parser_replace = subparsers.add_parser('replace', help='Use a translation map to modify files')

    #parser_replace.add_argument('--confirm', help="When files differ, prompt confirmation before overwrite", action='store_true')
    parser_replace.add_argument('--simulate', help="Simulate replacement. Print results on the standard output", action='store_true')
    parser_replace.add_argument('mapping', metavar='MAPPING', help='The file containing the translation map to use')
    parser_replace.add_argument('files', metavar='FILE', type=str, nargs='*', help='The file(s) where performing operation')

    if len(sys.argv)==1: 
        parser.print_help()
        sys.exit(1)

    namespace = parser.parse_args()

    if namespace.command == 'extract':
        extract(namespace.search, namespace.replacement, namespace.force, namespace.files)
    elif namespace.command == 'replace':
        replace(namespace.mapping, namespace.files, namespace.simulate)
    else:
        print('Unknown command %s' % namespace.command, file=sys.stderr)
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
