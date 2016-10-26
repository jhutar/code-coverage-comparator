#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import tabulate
import cococo

# Diff two reports
differ = cococo.Differ(sys.argv[1], sys.argv[2])
diff = differ.diff_it()

table = []
for fil, val in differ.diff_it().iteritems():
    row = []
    row.append(fil)

    # If file was measured only in first report
    if val[1] == None:
        for a in val[0]:
            row.append("%s-" % a)
    # If file was measured only in second report
    elif val[0] == None:
        for b in val[1]:
            row.append("-%s" % b)
    # If file was measured in both reports
    else:
        for a, b in zip(val[0], val[1]):
            if b == a:
                row.append("%s-%s" % (a, b))
            elif b > a:
                row.append("%s/%s" % (a, b))
            elif b < a:
                row.append("%s\%s" % (a, b))

    table.append(row)

print tabulate.tabulate(table, headers=differ.header)
print
print "Legend:"
print "  x/y ... means that value got bigger from first to second report"
print "  x-y ... means that value did not changed from first to second report"
print "  x\y ... means that value got smaller from first to second report"
