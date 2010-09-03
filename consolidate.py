#!/usr/bin/python
#: consolidate.py : consolidate data from different version
#
#  Copyright (c) 2000,2001,2007-2010  Giacomo A. Catenazzi <cate@cateee.net>
#  This is free software, see GNU General Public License v2 for details

import sys
import optparse
import os
import os.path
import subprocess
import fnmatch
import glob

import lkddb
import lkddb.linux
import lkddb.tables


def make(options, args):

    tree = lkddb.linux.linux_kernel(lkddb.TASK_CONSOLIDATE, None, [])
    lkddb.init(options)
    lkddb.log.phase("read files to consolidate")
    for f in args:
	tree.read_consolidate(f)

    lkddb.log.phase("write consolidate main file")
    tree.write_consolidate(filename=options.consolidated)

#
# main
#

if __name__ == "__main__":
    
    usage = "Usage: %prog [options] file-to-consolidate..."
    parser = optparse.OptionParser(usage=usage)
    parser.set_defaults(verbose=1, consolidated="clkddb")
    parser.add_option("-q", "--quiet",	dest="verbose",
                      action="store_const", const=0,
                      help="inhibit messages")
    parser.add_option("-v", "--verbose", dest="verbose",
                      action="count",
                      help="increments verbosity")
    parser.add_option("-o", "--output", dest="consolidated",
                      action="store",	type="string",
                      help="base FILE name to read and write data", metavar="FILE")
    parser.add_option("-l", "--log",	dest="log_filename",
                      action="store",	type="string",
                      help="FILE to put log messages (default is stderr)", metavar="FILE")
    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("missing mandatory argument: on or more files to consolidate")

    options.versioned = False
    make(options, args)

