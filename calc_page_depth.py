#!/usr/bin/env python

import os
import sys

link_dict = {} 
for line in sys.stdin:
  parts = line.rstrip().split(" ")
  word = parts[0]
  for link in parts[1:]:
    link_dict.setdefault(word,[]).append(link)

depth_dict = {"Main_Page":0}
page_front = ["Main_Page"]

while len(page_front) > 0:
  new_front = []
  for page in page_front:
    links = link_dict.get(page,[])
    for link in links:
      if depth_dict.has_key(link):
        if depth_dict[link] > depth_dict[page] + 1:
          new_front.append(link)
          depth_dict[link] = depth_dict[page] + 1
      else:
        depth_dict[link] = depth_dict[page] + 1
        new_front.append(link)

  page_front = new_front

for k,v in depth_dict.items():
  print k, v
