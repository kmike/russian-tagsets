# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters
from russian_tagsets import positional

def _remove_unsupported(tag):
    if not isinstance(tag, positional.Tag):
        tag = positional.Tag(tag)

    if tag.POS == 'AU':
        tag.POS = 'AA'

    tag.animacy = '-'
    tag.possessors_gender = '-'
    tag.possessors_number = '-'
    tag.reflexivity = '-'
    tag.verbal_aspect = '-'

    if tag.degree_of_comparison == '1':
        tag.degree_of_comparison = '-'

    if tag.POS == 'Dg' and tag.degree_of_comparison != '-':
        tag.POS = 'AA'

    # prepositions
    if tag.POS in ['RR', 'RV']:
        tag.POS = 'R-'
        tag.case = '-'

    # conjunctions
    if tag.POS in ['J,', 'J^']:
        tag.POS = 'J-'


    return str(tag)

class TestConversion(object):

    TAGS = [ # word, positional tag, pymorphy tag
        # example sentence
        ['он',          'PPM-S1--3I------', 'МС,3л,мр,ед,им'],
        ['купил',       'VBM-S----IR-----', 'Г,дст,прш,мр,ед'],
       #['нашу',        'PSFIS4-P1I------', 'МС-П,жр,ед,вн,од,но'], # not enough info
        ['нашу',        'PSFIS4-P-I------', 'МС-П,жр,ед,вн,од,но'],
        ['старую',      'AAFXS4------1A--', 'П,жр,ед,вн,од,но'],
        ['фотографию',  'NNF-S4-------A--', 'С,жр,ед,вн'],

        # nouns
        ['голос',       'NNMIS4-------A--', 'С,мр,ед,вн'], # online example tag was incorrect

        # adjectives
        ['тяжелый',     'AAMIS4------1A--', 'П,мр,ед,вн,од,но'],
        ['красив',      'ACM-S--------A--', 'КР_ПРИЛ,мр,ед,од,но'],
        ['читающий',    'AGMXS1---IPI-AA-', 'ПРИЧАСТИЕ,од,но,нст,дст,ед,мр,им'],
        ['читаемый',    'AGMXS1---IXI-AP-', 'ПРИЧАСТИЕ,од,но,стр,ед,мр,им'],
        ['мужнин',      'AUMXS4M------A--', 'П,мр,ед,вн,но'],
        ['прочитан',    'AcM-S----I-P-AP-', 'КР_ПРИЧАСТИЕ,од,но,прш,стр,ед,мр'],

        # verbs
        ['отрываешь',   'VB--S---2IPI----', 'Г,дст,нст,2л,ед'],
        ['читал',       'VBM-S----IRI----', 'Г,дст,прш,мр,ед'],
        ['грозя',       'Ve-------I-I----', 'ДЕЕПРИЧАСТИЕ,дст,нст'],
        ['написав',     'Ve-------I-P----', 'ДЕЕПРИЧАСТИЕ,дст,прш'],
        ['спать',       'Vf-------I-I----', 'ИНФИНИТИВ,дст'],
        ['работай',     'Vi--S---2I-I----', 'Г,дст,пвл,2л,ед'],

        # adverbs
        ['там',         'Db--------------', 'Н,указат'],
        ['сильнее',     'Dg----------2A--', 'П,сравн,од,но'], # online example was incorrect

        # prepositions
        ['над',         'RR---7----------', 'ПРЕДЛ'],
        ['надо',        'RV---7----------', 'ПРЕДЛ'],
        ['несмотря',    'RF--------------', 'ФРАЗ'],

        # conjunctions, particles, interjenctions
        ['и',           'J^--------------', 'СОЮЗ'],
        ['что',         'J,--------------', 'СОЮЗ'],
        ['нет',         'TT--------------', 'ЧАСТ'],
        ['ой',          'II--------------', 'МЕЖД'],
    ]

    def assertPositionalEqual(self, converted, gold):
        assert _remove_unsupported(converted) == _remove_unsupported(gold)

#    @pytest.mark.parametrize(("word", "pos_tag_txt", "aot_tag"), TAGS)
#    def test_from_positional(self, word, pos_tag_txt, aot_tag):
#        converted = converters.convert(
#            positional.Tag(pos_tag_txt),
#            'positional', 'aot'
#        )
#        assert converted == aot_tag

    @pytest.mark.parametrize(("word", "pos_tag_txt", "aot_tag"), TAGS)
    def test_to_positional(self, word, pos_tag_txt, aot_tag):
        converted = converters.convert(aot_tag, 'aot', 'positional')
        self.assertPositionalEqual(converted, pos_tag_txt)
