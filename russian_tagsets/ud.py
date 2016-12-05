# -*- coding: utf-8 -*-
"""
Conversion between inner OpenCorpora format and Universal Dependencies 1.4
(http://universaldependencies.org/ru/pos/all.html)

Known issues:
TODO
"""

from __future__ import absolute_import, unicode_literals
from russian_tagsets import converters
from russian_tagsets.utils import invert_mapping

def to_ud14(oc_tag, word=None):
    return oc_tag

converters.add('opencorpora-int', 'ud14', to_ud14)
