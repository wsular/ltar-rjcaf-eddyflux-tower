# Script for retrieving third-party documentation from the internet
#
# Originally from long-term canister-based relaxed eddy accumulation project.

from __future__ import print_function

import sys
import os
import os.path as osp

from urllib import urlretrieve

def report_progress(a, b, c):
    # https://stackoverflow.com/a/2003565/2946116
    print("% 3.1f%% of %d bytes\r" % (min(100, float(a*b) / c*100), c), end='')

if __name__ == '__main__':
    os.chdir(osp.dirname(sys.argv[0]))
    print("Destination directory: " + os.getcwd())
    raw_input("Press <enter> to continue or Ctrl+C to exit")

    try:
        srcfile = sys.argv[1]
        f = open(srcfile, mode='r')
    except IndexError, IOError:
        print("Could not find accessible source file!")
        raw_input("Press <enter> to exit.")
        sys.exit(1)

    for line in f.readlines():
        try:
            url, fname = [s.strip() for s in line.split('    ')]
        except ValueError:
            if len(line.strip()):
                if not line.lstrip().startswith('#'):
                    print("Could not parse this input: " + line.strip('\n'))
            continue
        if osp.isfile(fname):
            print('Skipping existing file %s' % fname)
        else:
            print('Downloading %s to %s' % (url, fname))
            urlretrieve(url, fname, report_progress)

    raw_input("\nPress <enter> to exit.")
