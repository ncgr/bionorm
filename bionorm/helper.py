#!/usr/bin/env python
# -*- coding: utf-8 -*-

# standard library imports
import errno
import gzip
import logging
import os
import subprocess
import sys


def check_busco_dependencies():
    """attempts to run samtools, tabix and bgzip"""
    subprocess.check_call("which run_BUSCO.py", shell=True)  # check in env
    subprocess.check_call("which augustus", shell=True)  # check in env
    return True


def return_filehandle(open_me):
    """return file handle for gz compressed or text file"""
    magic_dict = {  # headers for compression
        b"\x1f\x8b\x08": "gz",
        #                 '\x42\x5a\x68': 'bz2',
        #                 '\x50\x4b\x03\x04': 'zip'
    }
    max_bytes = max(len(t) for t in magic_dict)
    with open(open_me, "rb") as f:
        s = f.read(max_bytes)
    for m in magic_dict:
        if s.startswith(m):  # check file header for match with m
            t = magic_dict[m]
            if t == "gz":
                return gzip.open(open_me, "rt")
    return open(open_me)


def check_file(f):
    """check for file using os.path.isfile"""
    try:
        os.path.isfile(f)
    except OSError:
        raise
    return os.path.isfile(f)


def create_directories(dirpath):
    """make directory path"""
    try:
        os.makedirs(dirpath)
    except OSError as e:
        if e.errno != errno.EEXIST:  # ignore if error is exists else raise
            raise


def change_directories(dirpath):
    """cd to path, does not modify calling process CWD"""
    try:
        os.chdir(dirpath)
    except OSError as e:
        raise


if __name__ == "__main__":
    print("import me to use check_file and return_filehandle." + "This should be in a class probably")
    sys.exit(1)
