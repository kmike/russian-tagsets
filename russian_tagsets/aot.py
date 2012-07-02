# -*- coding: utf-8 -*-
"""
Conversion from aot.ru tags to positional tags.
AOT tags should be tuple(POS, gram_info), e.g.::

    (u'П', u'мр,ед,им,од,но')

POS->AOT conversion is lossy.
"""

from __future__ import absolute_import, unicode_literals
from russian_tagsets import converters
from russian_tagsets import positional

def to_positional(aot_tag):
    pos, info = aot_tag
    info = set(info.split(','))
    tag = positional.Tag()

    # ==== POS tag ====
    if pos == 'С':
        tag.POS = 'NN'

    elif pos == 'П':
        tag.POS = 'AA'
        # lossy: possessive adjective (мамин, овечью) should be AU

    elif pos == 'Г':
        tag.POS = 'VB'
        if 'пвл' in info:
            tag.POS = 'Vi'

    elif pos == 'ПРИЧАСТИЕ':
        # Participle, active or long passive
        # (читающий, читавший, прочитавший, читаемый;
        # but not прочитанный (AA), прочитан (Ac)
        tag.POS = 'AG'

    elif pos == 'КР_ПРИЧАСТИЕ':
        tag.POS = 'Ac'

    elif pos == 'КР_ПРИЛ':
        tag.POS = 'AC'

    elif pos == 'ДЕЕПРИЧАСТИЕ':
        tag.POS = 'Ve'

    elif pos == 'ИНФИНИТИВ':
        tag.POS = 'Vf'

    elif pos == 'МС':
        # Personal pronoun (ja, my, ty, vy, on, ona, ono, oni, sebja)
        tag.POS = 'PP'

    elif pos == 'МС-ПРЕДК':
        # e.g. нечего
        tag.POS = 'Db' # lossy

    elif pos == 'МС-П':
        # e.g. всякий

        # Relative/interrogative pronoun with adjectival
        # declension (kakoj, kotoryj, cej, ...)
        tag.POS = 'Pq'

        # fixme/hack: Possessive pronoun (moj, ego, svoj, ..)
        if 'од' in info:
            tag.POS = 'PS'

    elif pos == 'Н':
        # Adverb without a possibility to form negation
        # and degrees of comparison (vverxu, vnizu, potom)
        tag.POS = 'Db'

        # fixme: adverb forming negation and degrees of
        # comparison (vysoko, daleko). Idea: pymorphy.get_graminfo
        # returns 'КР_ПРИЛ' and 'Н' variants for such adverbs.
        # tag.POS == 'Dg'

        # fixme: Multiplicative numeral (dvaždy, triždy) are adverbs

    elif pos == 'ПРЕДК':
        # e.g. интересно
        tag.POS = 'Dg' # ?

    elif pos == 'ЧИСЛ':
        # Cardinal numeral (odin, tri, sorok)
        tag.POS = 'Cn'

        # fixme: Generic/collective numeral (dvoje, četvero)
        # tag.POS = 'Cj'

    elif pos == 'ЧИСЛ-П':
        tag.POS = 'Cr'

    elif pos == 'ПРЕДЛ':
        # Nonvocalized preposition (ob, pered, s, v, ...)
        tag.POS = 'RR'

        # fixme: Part of a preposition; never appears isolated (nesmotrja)
        # tag.POS = 'PF'

        # fixme: Vocalized preposition (obo, peredo, so, vo, ...)
        # tag.POS = 'RV'

    elif pos == 'СОЮЗ':
        # Non-subordinate conjunction (i, a, xotja, pricem)
        tag.POS = 'J^'
        # fixme: Subordinate conjunction (esli, čto, kotoryj)
        # tag.POS = 'J,'

    elif pos == 'МЕЖД':
        tag.POS = 'II'

    elif pos == 'ЧАСТ':
        tag.POS = 'TT'

    elif pos == 'ВВОДН':
        # e.g. конечно
        tag.POS = 'Db' # ?

    # ==== gender ====

    if 'мр' in info:
        tag.gender = 'M'
    elif 'жр' in info:
        tag.gender = 'F'
    elif 'ср' in info:
        tag.gender = 'N'
    elif 'мр-жр' in info:
        tag.gender = 'X' # fixme?

    # ==== animacy ====
    # FIXME
    # X should be used: except for nouns, in all
    # forms except accusative masculine singular and accusative
    # plural of all genders. Non-declinable words in all forms.
    if info.issuperset(['од', 'но']):
        tag.animacy = 'X' # fixme
    elif 'од' in info:
        tag.animacy = 'A'
    elif 'но' in info:
        tag.animacy = 'I'
    else:
        tag.animacy = '-' # fixme?

    # ======== number =======
    if 'ед' in info:
        tag.number = 'S'
    elif 'мн' in info:
        tag.number = 'P'
    # FIXME
    # non-declinable nouns, adjectives and verbs,
    # 3rd person possessive pronouns:
    # tag.number = 'X'

    # ======== case ==========
    CASES = {
        'им': '1',
        'рд': '2',
        'дт': '3',
        'вн': '4',
        'тв': '7',
        'пр': '6',
    }
    for case in CASES:
        if case in info:
            tag.case = CASES[case]
        if '2' in info:
            tag.variant = '1'
    if 'зв' in CASES:
        tag.case = '1'
        tag.variant = '1'

    # TODO: possessor's gender
    # TODO: possessor's number

    # ======= person ========
    # fixme: it should be X for non-declinable verbs
    PERSONS = {'1л': '1', '2л': '2', '3л': '3'}
    for person in PERSONS:
        if person in info:
            tag.person = PERSONS[person]
            break

    # ======= reflexivity ========
    if tag.POS in ['AG', 'PP', 'P5', 'PS'] or tag.mainPOS == 'V':
        tag.reflexivity = 'I'
        # fixme: lossy! e.g. for "получиться" it should be 'R'.

    # ======= tense =========
    TENSES = {
        'нст': 'P',
        'прш': 'R',
        'буд': 'F',
    }
    for tense in TENSES:
        if tense in info:
            tag.tense = TENSES[tense]
            break

    # TODO: verbal_aspect

    # ========== degree of comparison =========
    if tag.POS in ['AA', 'Dg']:
        if 'сравн' in info:
            tag.degree_of_comparison = '2'
        elif 'прев' in info:
            tag.degree_of_comparison = '3'
        else:
            tag.degree_of_comparison = '1'

    # ========= negation =========
    if tag.mainPOS in ['N', 'A'] or tag.POS == 'Dg':
        tag.negation = 'A'
        # fixme: lossy! e.g. for ""


    return tag

def from_positional(positional_tag):
    pass

converters.add('positional', 'aot', from_positional)
converters.add('aot', 'positional', to_positional)