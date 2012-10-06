# -*- coding: utf-8 -*-
from __future__ import absolute_import
import collections

class NoConvertPath(Exception):
    pass

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

class Registry(object):

    def __init__(self):
        # Directed graph of all possible transformations.
        # _registry['from']['to'] -> transformation function
        self._registry = collections.defaultdict(dict)

    def add(self, type_from, type_to, method):
        """
        Registers :param:``method`` as conversion method from
        :param:``type_from`` to :param:``type_to``.

        :param:``method`` signature should receive object of type ``type_from``
        and return an object of type ``type_to``.
        """
        self._registry[type_from][type_to] = method

    def path(self, type_from, type_to):
        """
        Returns a list of conversion steps.
        """
        _path = find_shortest_path(self._registry, type_from, type_to)
        if _path is None:
            raise NoConvertPath()
        return _path

    def steps(self, type_from, type_to):
        """
        Returns a list of conversion functions that should be applied to
        translate from ``type_from`` to ``type_to``.
        """
        for from_, to_ in bigrams(self.path(type_from, type_to)):
            yield self._registry[from_][to_]

    def convert(self, obj, type_from, type_to):
        """
        Converts object from ``type_from`` to ``type_to``.
        """
        for func in self.steps(type_from, type_to):
            obj = func(obj)
        return obj

    def get_supported(self):
        res = []
        for type_from in self._registry:
            for type_to in self._registry[type_from]:
                res.append((type_from, type_to))
        return res