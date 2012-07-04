# -*- coding: utf-8 -*-
from __future__ import absolute_import

def invert_mapping(dct):
    return dict([v,k] for k,v in dct.items())
