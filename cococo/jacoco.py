#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv

MARKER = 'report.csv'

class JaCoCo(object):
    def __init__(self, directory):
        self.directory = directory
        pass
