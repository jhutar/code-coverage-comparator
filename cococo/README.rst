CoCoCo - code coverage reports comparator
=========================================

High level (does not compare coverage of individual lines in the code) comparation of a code coverage reports.

Here we are comparing two coverage.py reports:

.. code:: sh

    $ cococo/cococo-diff.py https://.../logs/python-coverage-html.tar.gz https://.../logs/python-coverage-html.tar.gz
    filename                                                             files    statements    excluded    missing    branches    partial branches    missing branches    coverage [%]
    -------------------------------------------------------------------  -------  ------------  ----------  ---------  ----------  ------------------  ------------------  --------------
    /usr/share/rhn/server/handlers/xmlrpc/getMethod.py                   1→1      65→65         0→0         19→19      34→34       11→11               13→13               68→68
    /usr/share/rhn/wsgi/package_push.py                                  1→1      3→3           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/wsgi/__init__.py                                      1→1      0→0           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/applet/applet.py                      1→1      118→118       0→0         100→100    36→36       0→0                 36→36               12→12
    /usr/share/rhn/server/handlers/config_mgmt/rhn_config_management.py  1→1      238→238       0→0         45→45      58→58       18→18               24→24               77→77
    /usr/share/rhn/wsgi/config_tool.py                                   1→1      3→3           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/upload_server/handlers/package_push/package_push.py   1→1      88→88         0→0         30→30      22→22       7→7                 11→11               63→63
    /usr/share/rhn/wsgi/xmlrpc.py                                        1→1      3→3           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/xmlrpc/registration.py                1→1      591→591       0→0         272↗278    222→222     41→41               141→141             49↘48
    /usr/share/rhn/server/handlers/config/rhn_config_management.py       1→1      117→117       0→0         52→52      28→28       5→5                 15→15               54→54
    /usr/share/rhn/upload_server/handlers/package_push/__init__.py       1→1      3→3           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/upload_server/__init__.py                             1→1      1→1           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/xmlrpc/errata.py                      1→1      102→102       0→0         54→54      32→32       7→7                 23→23               43→43
    /usr/share/rhn/wsgi/wsgiHandler.py                                   1→1      33→33         0→0         3→3        16→16       2→2                 4→4                 86→86
    /usr/share/rhn/server/handlers/xmlrpc/proxy.py                       1→1      128→128       0→0         99→99      14→14       0→0                 14→14               20→20
    /usr/share/rhn/wsgi/app.py                                           1→1      3→3           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/xmlrpc/scap.py                        1→1      54→54         0→0         9→9        14→14       5→5                 5→5                 79→79
    /usr/share/rhn/wsgi/applet.py                                        1→1      3→3           0→0         3→3        0→0         0→0                 0→0                 0→0
    /usr/share/rhn/wsgi/sat_dump.py                                      1→1      3→3           0→0         3→3        0→0         0→0                 0→0                 0→0
    /usr/share/rhn/server/handlers/config/__init__.py                    1→1      4→4           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/xmlrpc/up2date.py                     1→1      140→140       0→0         60→60      26→26       0→0                 18→18               53→53
    /usr/share/rhn/server/handlers/xmlrpc/country.py                     1→1      6→6           0→0         6→6        2→2         0→0                 2→2                 0→0
    /usr/share/rhn/server/handlers/xmlrpc/states.py                      1→1      5→5           0→0         5→5        2→2         0→0                 2→2                 0→0
    /usr/share/rhn/server/handlers/xmlrpc/abrt.py                        1→1      192→192       0→0         45→45      52→52       10→10               18→18               74→74
    /usr/share/rhn/server/handlers/sat/__init__.py                       1→1      4→4           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/upload_server/handlers/__init__.py                    1→1      1→1           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/app/__init__.py                       1→1      4→4           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/config_mgmt/__init__.py               1→1      4→4           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/xmlrpc/get_handler.py                 1→1      3→3           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/app/packages.py                       1→1      345→345       0→0         109→109    78→78       19→19               37→37               65→65
    /usr/share/rhn/server/handlers/applet/__init__.py                    1→1      4→4           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/wsgi/sat.py                                           1→1      3→3           0→0         3→3        0→0         0→0                 0→0                 0→0
    /usr/share/rhn/wsgi/config.py                                        1→1      3→3           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/wsgi/wsgiRequest.py                                   1→1      92→92         0→0         9→9        22→22       2→2                 4→4                 89→89
    /usr/share/rhn/server/__init__.py                                    1→1      0→0           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/__init__.py                           1→1      1→1           0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/sat/cert.py                           1→1      21→21         0→0         14→14      2→2         0→0                 2→2                 30→30
    /usr/share/rhn/server/handlers/xmlrpc/queue.py                       1→1      294→294       0→0         108→108    92→92       20→20               46→46               60→60
    /usr/share/rhn/server/handlers/xmlrpc/__init__.py                    1→1      11→11         0→0         0→0        0→0         0→0                 0→0                 100→100
    /usr/share/rhn/server/handlers/sat/auth.py                           1→1      41→41         0→0         27→27      6→6         0→0                 6→6                 30→30
    
    Legend:
      x↗y ... means that value got bigger from first to second report
      x→y ... means that value did not changed from first to second report
      x↘y ... means that value got smaller from first to second report
      Note: Colour codes depends on how value changed and how is given column
            change supposed to be interpretter - i.e. 'bigger the better'
            or 'smaller the better'
