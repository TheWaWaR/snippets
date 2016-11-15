#!/usr/bin/env python
# coding: utf-8

import re
import sys
from pprint import pprint


stmt_regexp = r'^<[-a-zA-Z0-9 ]+>'
substmt_regexp = r'[^^](<[-a-zA-Z0-9 ]+>)'


def main():
    stmts = {}
    current_stmt = None
    substmt_all = set()
    with open(sys.argv[1]) as f:
        for line in f:
            if not line.strip() or line[0] == '#': continue
            stmt_items = re.findall(stmt_regexp, line)
            if stmt_items:
                current_stmt = stmt_items[0]
                if current_stmt in stmts:
                    print('Duplicated: {}'.format(current_stmt))
            if current_stmt not in stmts:
                stmts[current_stmt] = set()
            substmt_items = re.findall(substmt_regexp, line)
            for item in substmt_items:
                stmts[current_stmt].add(item)
                substmt_all.add(item)

    missings = set()
    for stmt, substmts in stmts.iteritems():
        if stmt not in substmt_all and stmt != '<query specification>':
            print('[Unused stmt]: {}'.format(stmt))
        for substmt in substmts:
            if substmt not in stmts:
                missings.add(substmt)
    if missings:
        pprint(missings)
    else:
        print('Well DONE!')


if __name__ == '__main__':
    main()
