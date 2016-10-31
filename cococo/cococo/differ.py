#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import requests
import tempfile
import tarfile
import difflib
import io

import jacoco
import coveragepy

# When given file is found, consider the containing directory a base
# directlry for code coverate report of given type
MARKERS = {
    jacoco.MARKER: jacoco.JaCoCo,
    coveragepy.MARKER: coveragepy.CoveragePy,
}

class Differ:
    """Diff two code coverage reports"""

    def __init__(self, first, second):
        """Load first and second code coverage report, ensure they are both
           the same type, determine diff header"""
        self.first = self.guess_type(self.prepare(first))
        self.second = self.guess_type(self.prepare(second))
        assert type(self.first) == type(self.second), \
          "Type of first and second report does not match"
        self.header = ['filename'] + self.first.header
        self.meaning = [None] + self.first.meaning

    def __str__(self):
        return "CoCoCo differ for %s (%s) and %s (%s)" \
          % (self.first.directory, type(self.first), \
             self.second.directory, type(self.second))

    def prepare(self, location):
        """Accepts either directory, tarball or http location of tarball. If
           tarball is thrown at it, it obtains it and unpacks. Returns
           directory with unpacked code coverage."""
        if os.path.isdir(location):
            return location
        else:
            extracted = 0
            tempdir = tempfile.mkdtemp()
            # Maybe it is file or something on http://...
            if os.path.isfile(location):
                fp = open(location, 'r')
                tar = tarfile.open(fileobj=fp, mode='r:*')
            else:
                fp = requests.get(location)
                tar = tarfile.open(fileobj=io.BytesIO(fp.content), mode='r:*')
            # Unzip only files interesting for use. These are markers only now
            for member in tar.getmembers():
                for marker in MARKERS.keys():
                    if member.name.endswith(marker):
                        tar.extract(member, tempdir)
                        extracted += 1
            # If we have extracted succesfully, return directory location
            if extracted > 0:
                return tempdir
            else:
                raise Exception("Failed to extract expected files for '%s'" % location)


    def guess_type(self, starting_dir):
        """Return object representing correct type of code coverage report"""
        # Go through whole tree as maybe we have packed the report as
        # 'var/www/html/python-report/status.json'
        for root, dirs, files in os.walk(starting_dir):
            # Return report with corresponding type if we have found its marker
            for marker in MARKERS:
                if marker in files:
                    return MARKERS[marker](root)
        raise Exception("I was not able to determine code coverage report type in '%s'" % starting_dir)

    def diff_it(self):
        """Return code coverage numbers per file from first and second
           report"""
        data = {}
        differ = difflib.Differ()
        first = self.first.data.keys()
        first.sort()
        second = self.second.data.keys()
        second.sort()
        # Save data differently if file was measured only in first, only
        # in second or in both reports
        for item in differ.compare(first, second):
            fil = item[2:]
            mode = item[:1]
            if mode == ' ':
                data[fil] = [self.first.data[fil], self.second.data[fil]]
            elif mode == '+':
                data[fil] = [None, self.second.data[fil]]
            elif mode == '-':
                data[fil] = [self.first.data[fil], None]
        return data
