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

class Tag(object):

    GRAM_MAP = {
        '_POS': {
            'NOUN': 'NOUN',
            'PNCT': 'PUNCT',
        },
        'Animacy': {
            'inan': 'Inan',
        },
        'Aspect': {
            'perf': 'Perf',
        },
        'Case': {
            'nomn': 'Nom',
        },
        'Gender': {
            'femn': 'Fem',
        },
        'Number': {
            'sing': 'Sing',
        },
    }

    def __init__(self, oc_tag):
        self.pos = 'Unknown'  # ???
        self.grammemes = set()
        self._fill_from_oc(oc_tag)

    def _try_apply_exceptions(self, gram):
        if gram == 'INFN':
            self.pos = 'VERB'
            self.grammemes.add(("VerbForm", "Inf"))
            return True
        return False

    def _fill_one_gram_oc(self, gram):
        if self._try_apply_exceptions(gram):
            return

        for categ, gmap in self.GRAM_MAP.items():
            if gram in gmap:
                if categ == '_POS':
                    self.pos = gmap[gram]
                else:
                    self.grammemes.add((categ, gmap[gram]))

    def _fill_from_oc(self, oc_tag):
        grams = oc_tag.replace(' ', ',').split(',')
        for g in grams:
            self._fill_one_gram_oc(g)

    def __str__(self):
        grams = '|'.join("{}={}".format(c, v) for c, v in sorted(list(self.grammemes)))
        return "{} {}".format(self.pos, grams if grams else '_')


def to_ud14(oc_tag, word=None):
    tag = Tag(oc_tag)
    return str(tag)

converters.add('opencorpora-int', 'ud14', to_ud14)
