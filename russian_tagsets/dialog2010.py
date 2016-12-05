# -*- coding: utf-8 -*-
"""
Conversion between Dialog-2010 (http://ru-eval.ru/) and aot.ru tags.

Dialog-2010 tags are less detailed than aot tags so aot -> dialog2010
conversion discards information.
"""
from __future__ import absolute_import, unicode_literals
import itertools
from russian_tagsets import converters
from russian_tagsets import aot
from russian_tagsets.utils import invert_mapping

POS = {
    'С':              'S',
    'П':              'A',
    'МС':             '-',
    'Г' :             'V',
    'ПРИЧАСТИЕ' :     'V',
    'ДЕЕПРИЧАСТИЕ' :  'V',
    'ИНФИНИТИВ':      'V',
    'МС-ПРЕДК':       '-',
    'МС-П':           '-',
    'ЧИСЛ':           '-',
    'ЧИСЛ-П':         '-',
    'Н':              'ADV',
    'ПРЕДК':          '-',
    'ПРЕДЛ':          'PR',
    'СОЮЗ':           'CONJ',
    'МЕЖД':           'ADV',
    'ЧАСТ':           'ADV',
    'ВВОДН':          'ADV',
    'КР_ПРИЛ':        'A',
    'КР_ПРИЧАСТИЕ':   'V',  # FIXME: ?
    'ПОСЛ':           '-',
    'ФРАЗ':           '-',
}
POS_INV = {
    'S': 'С',
    'A': 'П',
    'V': 'Г',
    'ADV': 'Н',
    'PR': 'ПРЕДЛ',
    'CONJ': 'СОЮЗ',
}

GENDERS = {
    'мр': 'm',
    'жр': 'f',
    'ср': 'n',
    'мр-жр': '',  # FIXME: ?
}

CASES = {
    'им': 'nom',
    'рд': 'gen',
    'дт': 'dat',
    'вн': 'acc',
    'тв': 'ins',
    'пр': 'loc',
    'зв': 'voc',
}

NUMBERS = {'ед': 'sg', 'мн': 'pl'}
PERSONS = {'1л': '1p', '2л': '2p', '3л': '3p'}
VOICES = {'дст': 'act', 'стр': 'pass'}
TENSES = {
    'нст': 'pres',
    'прш': 'past',
    'буд': 'pres',
}
EXTRA = {
    'сравн': 'comp',
    'прев': 'supr',
    'пвл': 'imper',
}

GRAMINFO_MAP = dict(itertools.chain(
    GENDERS.items(), CASES.items(), NUMBERS.items(), PERSONS.items(),
    TENSES.items(), VOICES.items(), EXTRA.items(),
))
GRAMINFO_MAP_INV = invert_mapping(GRAMINFO_MAP)

def from_aot(aot_tag, word=None):
    pos, info = aot.split_tag(aot_tag)
    extra_info = set()
    if pos in ['ПРИЧАСТИЕ', 'КР_ПРИЧАСТИЕ']:
        extra_info.add('partcp')
    else:
        info.discard('дст')
        info.discard('стр')

    if pos == 'ИНФИНИТИВ':
        extra_info.add('inf')
    elif pos == 'ДЕЕПРИЧАСТИЕ':
        extra_info.add('ger')

    new_form = (GRAMINFO_MAP[attr] for attr in info if attr in GRAMINFO_MAP)
    return ",".join(itertools.chain([POS[pos]], extra_info, new_form))


def to_aot(dialog_tag, word=None):
    pos, info = aot.split_tag(dialog_tag)
    new_form = (GRAMINFO_MAP_INV[tag] for tag in info if tag in GRAMINFO_MAP_INV)
    new_pos = POS_INV[pos]
    if pos == 'V':
        if 'inf' in info:
            new_pos = 'ИНФИНИТИВ'
        elif 'partcp' in info:
            new_pos = 'ПРИЧАСТИЕ'
        elif 'ger' in info:
            new_pos = 'ДЕЕПРИЧАСТИЕ'

    return ",".join(itertools.chain([new_pos], new_form))


converters.add('dialog2010', 'aot', to_aot)
converters.add('aot', 'dialog2010', from_aot)
