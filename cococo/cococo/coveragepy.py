#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os.path
import json

MARKER = 'status.json'

class CoveragePy(object):
    def __init__(self, directory):
        self.directory = directory
        self.header = ['files','statements','excluded','missing','branches',
                       'partial branches','missing branches', 'coverage [%]']
        self.data = {}
        # Load data from 'status.json'
        fp = open(os.path.join(self.directory, MARKER), 'r')
        all_data = json.load(fp)
        fp.close()
        # Transform the data to our format
        for item in all_data['files'].values():
            item = item['index']
            # Add summary 'coverage' column which is in HTML report
            # http://stackoverflow.com/questions/34191571/how-does-coverage-calculate-its-percentages
            executed = item['nums'][1] - item['nums'][3]
            executed_branches = item['nums'][4] - item['nums'][6]
            try:
                coverage = int(round(100*float(executed + executed_branches)/(item['nums'][1] + item['nums'][4])))
            except ZeroDivisionError:
                coverage = 100
            self.data[item['relative_filename']] = item['nums']+[coverage]
