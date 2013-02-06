# -*- coding: utf-8 -*-
from __future__ import absolute_import

def invert_mapping(dct):
    return dict((v, k) for k,v in dct.items())

def bigrams(iterable):
    _first = object()
    prev = _first
    for current in iterable:
        if prev is not _first:
            yield prev, current
        prev = current

def find_shortest_path(graph, start, end, cost=lambda path: len(path), path=[]):
    # adopted from http://www.python.org/doc/essays/graphs/
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, cost, path)
            if newpath:
                if not shortest or cost(newpath) < cost(shortest):
                    shortest = newpath
    return shortest

