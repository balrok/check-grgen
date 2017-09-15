#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import re
import subprocess
import sys
from fnmatch import fnmatch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--exclude', action='append', metavar='PATTERN')
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args()

    global_status = 0
    for filename in args.filenames:
        if any(fnmatch(filename, pat) for pat in args.exclude or ()):
            continue
        status, pr = grg_check(filename)
        global_status |= status
        if status > 0:
            print("\n".join(pr))
            return status
    return global_status


def grg_check(orig_filename):
    """Does a grgencheck on "filename"
    """
    filename = orig_filename
    dir = os.path.abspath(os.path.dirname(filename))
    if filename != "Rules.grg":
        frules = os.path.join(dir, "Rules.grg")
        if os.path.exists(frules):
            filename = "Rules.grg"
    if filename.endswith("Rules.grg"):
        try:
            out = subprocess.check_output(
                ['GrGen', filename],
                cwd=dir,
                stderr=subprocess.STDOUT,
                universal_newlines=True)
        except subprocess.CalledProcessError as e:
            out = e.output
        return process_out(orig_filename, out)
    return 1, ["No .grg file found"]


def process_out(filename, out):
    # GrGen: [ERROR at Rules.grg:4,0] missing EOF at ','
    ret = []
    start = False
    status_code = 0
    for line in out.split("\n"):
        if line.startswith("Error while processing specification"):
            start = True
            status_code = 1
        if start:
            m = re.match("GrGen: \[(\w+) at ([^:]+):([0-9]+),([0-9]+)] (.*)",
                         line)
            if m:
                etype, efile, eline, ecol, emsg = m.groups()
                ret += [
                    etype[0] + " " + efile + ":" + eline + ":" + ecol + " " +
                    emsg
                ]
    return status_code, ret


if __name__ == '__main__':
    sys.exit(main())
