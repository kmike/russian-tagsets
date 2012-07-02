# -*- coding: utf-8 -*-
from __future__ import absolute_import
from russian_tagsets.convert_engine import Registry

_registry = Registry()

class ConversionError(Exception):
    pass

def add(type_from, type_to, method):
    """
    Registers :param:``method`` as conversion method from
    :param:``type_from`` to :param:``type_to``.

    :param:``method`` signature should receive object of type ``type_from``
    and return an object of type ``type_to``.
    """
    _registry.add(type_from, type_to, method)

def steps(type_from, type_to):
    """
    Returns a list of conversion functions that should be applied to
    convert from ``type_from`` to ``type_to``; raises ConversionError
    if conversion is not possible.
    """
    return _registry.steps(type_from, type_to)

def convert(obj, type_from, type_to):
    """
    Converts object from ``type_from`` to ``type_to``.
    """
    for func in steps(type_from, type_to):
        obj = func(obj)
    return obj

