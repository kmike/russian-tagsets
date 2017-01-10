# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import collections
from .utils import bigrams, find_shortest_path

class NoConvertPath(Exception):
    pass

class Registry(object):

    def __init__(self):
        # Directed graph of all possible transformations.
        # _registry['from']['to'] -> transformation function
        self._registry = collections.defaultdict(dict)

    def add(self, type_from, type_to, method):
        """
        Register :param:``method`` as conversion method from
        :param:``type_from`` to :param:``type_to``.

        :param:``method`` signature should receive object of type ``type_from``
        and return an object of type ``type_to``.
        """
        self._registry[type_from][type_to] = method

    def path(self, type_from, type_to):
        """
        Return a list of conversion steps.
        """
        _path = find_shortest_path(self._registry, type_from, type_to)
        if _path is None:
            raise NoConvertPath()
        return _path

    def steps(self, type_from, type_to):
        """
        Return a list of conversion functions that should be applied to
        translate from ``type_from`` to ``type_to``.
        """
        for from_, to_ in bigrams(self.path(type_from, type_to)):
            yield self._registry[from_][to_]

    def convert(self, obj, type_from, type_to, word=None):
        """
        Convert object from ``type_from`` to ``type_to``.
        """
        for func in self.steps(type_from, type_to):
            obj = func(obj, word)
        return obj

    def get_supported(self):
        res = []
        for type_from in self._registry:
            for type_to in self._registry[type_from]:
                res.append((type_from, type_to))
        return res


_registry = Registry()

class ConversionError(Exception):
    pass

def add(type_from, type_to, method):
    """
    Register :param:``method`` as conversion method from
    :param:``type_from`` to :param:``type_to``.

    :param:``method`` signature should receive object of type ``type_from``
    and return an object of type ``type_to``.
    """
    _registry.add(type_from, type_to, method)

def steps(type_from, type_to):
    """
    Return a list of conversion functions that should be applied to
    convert from ``type_from`` to ``type_to``; raises ConversionError
    if conversion is not possible.
    """
    return _registry.steps(type_from, type_to)

def convert(obj, type_from, type_to, word=None):
    """ Convert object from ``type_from`` to ``type_to`` optionally using ``word`` """
    for func in steps(type_from, type_to):
        obj = func(obj, word)
    return obj

def get_supported():
    """ Return a list of directly supported conversions """
    return _registry.get_supported()

def converter(type_from, type_to):
    """ Return conversion function. """
    def conversion_func(tag, word=None):
        return convert(tag, type_from, type_to, word)

    conversion_func.__doc__ = """
    Converts ``tag`` with optional ``word`` from '%s' to '%s'.
    """ % (type_from, type_to)
    return conversion_func
