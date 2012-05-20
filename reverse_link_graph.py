#!/usr/bin/env python

import os
import sys

link_dict = {} 
for line in sys.stdin:
  parts = line.rstrip().split(" ")
  word = parts[0]
  for link in parts[1:]:
    link_dict.setdefault(link,[]).append(word)

for k,v in link_dict.items():
  print k," ".join(v)

