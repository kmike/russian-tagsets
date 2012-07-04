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

    # pronouns
    if tag.POS in ['PP', 'P5', 'PQ', 'PW', 'PZ', 'PD']:
        tag.POS = 'P-'
    if tag.POS in ['Pq', 'PS', 'Pw', 'Pz']:
        tag.POS = 'Pq'

    # numerals
    if tag.POS in ['Cu', 'Cn']:
        tag.number = '-'
    if tag.POS in ['Cj', 'Ca', 'Cu', 'Cv']:
        tag.POS = 'Cn'


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

        # pronouns
        ['нам',         'PP--P3--1I------', 'МС,1л,мн,дт'],
        ['он',          'PPM-S1--3I------', 'МС,3л,мр,ед,им'],
        ['себя',        'PP---4---R------', 'МС,вн'],
        ['него',        'P5M-S2--3-------', 'МС,3л,мр,ед,рд'],
        #['эту',         'PDFXS4----------', 'МС-П,жр,ед,вн,од,но'],
        #['ничто',       'PW---1----------', 'МС,ср,ед,им'],
        ['никакой',     'PwMXS1----------', 'МС-П,мр,ед,им,од,но'],
        #['моя',         'PSFXS1-S1I------', 'МС-П,жр,ед,им,од,но'], # aot returns it without '1л'
        #['его',         'PSXXXXMS3I------', 'МС-П,3л,мр,ед,рд'],
        ['свой',        'PSMXS1---R------', 'МС-П,мр,ед,им,од,но'],
        #['что',         'PQ---1----------', 'МС,ср,ед,им'],
        ['какой',       'PqMXS1----------', 'МС-П,мр,ед,им,од,но'],
        #['кого-то',     'PZ---4----------', 'МС,мр,ед,вн'],
        ['какой-то',    'PzMXS1----------', 'МС-П,мр,ед,им,од,но'],

        # numerals
        ['одному',      'CnMXS3----------', 'ЧИСЛ,мр,дт'],
        ['двух',        'CnMX-2----------', 'ЧИСЛ,мр,рд'],
        ['трех',        'Cn-A-4----------', 'ЧИСЛ,вн'],
        ['пяти',        'Cn---2----------', 'ЧИСЛ,рд'],
        ['первый',      'CrMXS1----------', 'ЧИСЛ-П,мр,ед,им,од,но'],
        ['двоих',       'Cj-A-2----------', 'ЧИСЛ,рд'], # Cj-A-3---------- Dative?
        ['сколько',     'Cu---1----------', 'ЧИСЛ,им'], # original: Cu---x----------
        ['несколько',   'Ca---1----------', 'ЧИСЛ,им'],
        #['многому',     'CaMXS3----------', 'МС-П,мр,ед,дт,од,но'], # online example was incorrect
        #['трижды',      'Cv--------------', 'Н'], # online example was incorrect

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
