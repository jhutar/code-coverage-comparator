#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import csv

MARKER = 'report.csv'

class JaCoCo(object):

    # Explain what columns in the self.data means
    header = "INSTRUCTION_MISSED,INSTRUCTION_COVERED,BRANCH_MISSED,BRANCH_COVERED,LINE_MISSED,LINE_COVERED,COMPLEXITY_MISSED,COMPLEXITY_COVERED,METHOD_MISSED,METHOD_COVERED".split(',')
    # Explain if "bigger is better" (==True) or "smaller is better"
    # (==False) for individual columns in self.data
    meaning = [False,True,False,True,False,True,False,True,False,True]

    def __init__(self, directory):
        self.directory = directory
        self.data = {}
        # Load data from 'report.csv'
        fp = open(os.path.join(self.directory, MARKER), 'r')
        all_data = list(csv.reader(fp))   # first row is header
        fp.close()
        # Transform the data to our format
        for item in all_data[1:]:
            identifier = "%s / %s / %s" % tuple(item[:3])
            self.data[identifier] = item[3:]
