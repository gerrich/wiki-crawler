#!/usr/bin/env python

import os
import sys
import operator
import copy

link_dict = {} 
for line in sys.stdin:
  parts = line.rstrip().split(" ")
  word = parts[0]
  for link in parts[1:]:
    link_dict.setdefault(word,[]).append(link)


pr_dict = {}
empty_pr_dict = {}
for page,links in link_dict.items():
  pr_dict[page] = 1.0
  empty_pr_dict[page] = 0.0
  for link in links:
    pr_dict[link] = 1.0
    empty_pr_dict[link] = 0.0

pr_dict["Russia"] = 10.0
pr_dict["Russian_Language"] = 10.0

for i in xrange(10):
  new_pr_dict = copy.copy(empty_pr_dict)
  for page, links in link_dict.items():
    new_pr_dict[page] += pr_dict[page] / (1.0 + len(links))
    for link in links:
      new_pr_dict[link] += pr_dict[page] / (1.0 + len(links))
  pr_dict = copy.copy(new_pr_dict)

for page, pr in sorted(pr_dict.iteritems(), key=operator.itemgetter(1)):
  print page, pr 

