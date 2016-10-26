#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

import jacoco
import coveragepy

# When given file is found, consider the containing directory 
MARKERS = {
    jacoco.MARKER: jacoco.JaCoCo,
    coveragepy.MARKER: coveragepy.CoveragePy,
}

class Differ:
    def __init__(self, first, second):
        self.first = self.guess_type(first)
        self.second = self.guess_type(second)
        assert type(self.first) == type(self.second), \
          "Type of first and second report does not match"

    def __str__(self):
        return "CoCoCo differ for %s (%s) and %s (%s)" \
          % (self.first.directory, type(self.first), self.second.directory, type(self.second))

    def guess_type(self, starting_dir):
        for root, dirs, files in os.walk(starting_dir):
            for marker in MARKERS:
                if marker in files:
                    return MARKERS[marker](root)
