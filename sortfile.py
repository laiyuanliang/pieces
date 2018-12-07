#!/usr/bin/env python
# -*- coding: utf_8 -*-

import os

basepath = os.getcwd()

with open('旦渊客户.txt','r') as f:
    for line in f:
        if not os.path.exists(basepath +'/' +line.strip()):
            os.mkdir(line.strip())

for path, dirlist, filelist in os.walk('.'):
    for dirs in dirlist:
        for files in filelist:
            if dirs in files:
                os.rename(basepath +'/' +files, basepath +'/' +dirs +'/' +files)
