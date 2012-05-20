#!/usr/bin/env python

import os
import sys

len_dict={}
for line in sys.stdin:
  parts = line.rstrip().split(" ")
  len_dict[len(parts)] = 1 + len_dict.get(len(parts), 0)

for k,v in sorted(len_dict.items()):
  print k, v
