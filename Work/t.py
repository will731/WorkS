#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@author:Eric.xin
"""
import os
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(parentdir)



for i in range(1,1000000):
    time.sleep(1)
    print i