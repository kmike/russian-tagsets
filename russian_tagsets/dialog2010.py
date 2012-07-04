# -*- coding: utf-8 -*-
"""
Conversion from Dialog-2010 (http://ru-eval.ru/) tags to aot.ru tags.
"""
from __future__ import absolute_import, unicode_literals
import itertools
from russian_tagsets import converters
from russian_tagsets import aot

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
    'КР_ПРИЧАСТИЕ':   'V',  #FIXME: ?
    'ПОСЛ':           '-',
    'ФРАЗ':           '-',
}

GENDERS = {
    'мр': 'm',
    'жр': 'f',
    'ср': 'n',
    'мр-жр': '', #FIXME: ?
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
    'буд': 'pres',          #FIXME: ?
}

EXTRA = {
    'partcp': 'partcp',
    'ger': 'ger',
    'inf': 'inf',
    'сравн': 'comp',
    'прев': 'supr',
    'пвл': 'imper',
}

GRAMINFO_MAP = dict(itertools.chain(
    GENDERS.items(), CASES.items(), NUMBERS.items(), PERSONS.items(),
    TENSES.items(), VOICES.items(), EXTRA.items(),
))

def from_aot(aot_tag):
    pos, info = aot.split_tag(aot_tag)
    if pos in ['ПРИЧАСТИЕ', 'КР_ПРИЧАСТИЕ']:
        info.add('partcp')
    else:
        info.discard('дст')
        info.discard('стр')

    if pos == 'ИНФИНИТИВ':
        info.add('inf')
    elif pos == 'ДЕЕПРИЧАСТИЕ':
        info.add('ger')

    new_form = (GRAMINFO_MAP[attr] for attr in info if attr in GRAMINFO_MAP)
    return ",".join(itertools.chain([POS[pos]], new_form))


def to_aot(dialog_tag):
    pass

converters.add('dialog2010', 'aot', to_aot)
converters.add('aot', 'dialog2010', from_aot)