# -*- coding: utf-8 -*-
"""
Conversion between aot.ru/pymorphy and positional
(http://ufal.mff.cuni.cz/~hana/morph/rutags.html) tags.

Both "aot -> positional" and "positional -> aot" conversions discard
some information because of tagset differences.

AOT tags are generally less detailed than positional tags so
"aot -> positional" conversion is about safe and
"positional -> aot" conversion is more lossy.

"aot -> positional" issues
--------------------------

* "безл", "указат", "вопр", "мр-жр", "имя", "отч" tags are discarded;
* "МС-ПРЕДК", "ПРЕДК" tags are lost in "aot -> positional -> aot"
  conversion (they become "Н");
* animacy is sometimes discarded.

"positional -> aot issues"
--------------------------

* possessor's gender, possessor's number, reflexivity, verbal aspect and
  negation are discarded because they don't have counterparts in aot tagset;
* pronounce, numeral, conjunction, preposition and
  participle classification is much simpler in aot;
* punctuation is not supported;
* possession information for adjectives is discarded;
* adverb classification criteria is different in aot;
* 'X' ("any number") number is not supported.

"""

from __future__ import absolute_import, unicode_literals
from russian_tagsets import converters
from russian_tagsets import positional
from russian_tagsets.utils import invert_mapping

def split_tag_raw(aot_tag):
    if ',' in aot_tag:
        return aot_tag.split(',', 1)
    else:
        return aot_tag, ''

def split_tag(aot_tag):
    pos, info = split_tag_raw(aot_tag)
    if info:
        return pos, set(info.split(','))
    else:
        return pos, set()

def join_tag(pos, info_set):
    return  ",".join([pos] + list(info_set))

_POS_MAP = {
    'N': 'С',

    'A': 'П',
    'AG': 'ПРИЧАСТИЕ',
    'Ac': 'КР_ПРИЧАСТИЕ',
    'AC': 'КР_ПРИЛ',

    'P': 'МС',
    'Pq': 'МС-П',
    'PS': 'МС-П',
    'Pw': 'МС-П',
    'Pz': 'МС-П',

    'C': 'ЧИСЛ',
    'Cr': 'ЧИСЛ-П',

    'V': 'Г',
    'VB': 'Г',
    'Vi': 'Г,пвл',
    'Ve': 'ДЕЕПРИЧАСТИЕ',
    'Vf': 'ИНФИНИТИВ',

    'D': 'Н',

    'R': 'ПРЕДЛ',
    'RF': 'ФРАЗ',
    'J': 'СОЮЗ',
    'I': 'МЕЖД',
    'T': 'ЧАСТ',
    'Z': 'ЗНАК', # non-standard
}

TENSES = {
    'нст': 'P',
    'прш': 'R',
    'буд': 'F',
}
TENSES_INV = invert_mapping(TENSES)

CASES = {
    'им': '1',
    'рд': '2',
    'дт': '3',
    'вн': '4',
    'тв': '7',
    'пр': '6',
}
CASES_INV = invert_mapping(CASES)

GENDERS = {
    'мр': 'M',
    'жр': 'F',
    'ср': 'N',
}
GENDERS_INV = invert_mapping(GENDERS)

PERSONS = {'1л': '1', '2л': '2', '3л': '3'}
PERSONS_INV = invert_mapping(PERSONS)


def to_positional(aot_tag, word=None):
    """
    Convert AOT.ru tag to positional.Tag format.
    This is lossy because of format differences.
    """

    pos, info = split_tag(aot_tag)

    tag = positional.Tag()

    # ==== 1,2: POS tag ====
    if pos == 'С':
        tag.POS = 'NN'

    elif pos == 'П':
        tag.POS = 'AA'
        # lossy: possessive adjective (мамин, овечью) should be AU
        # some comparative adjectives should be adverbs

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

        # fixme
        # 3rd person pronoun in prepositional forms (nego, nej, ...)
        # tag.POS = 'P5'

        # Relative/interrogative pronoun with nominal declension (kto, čto)
        # tag.POS = 'PQ'

        # Negative pronoun with nominal declension (nicto, nikto)
        # tag.POS = 'PW'

        # Indefinite pronoun with nominal declension (kto-to, kto-nibud', cto-to, ...)
        # tag.POS = 'PZ'

        # Pronoun demonstrative (ètot, tot, sej, takoj, èkij, ... )
        # tag.POS = 'PD'

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

        # fixme: Negative pronoun with adjectival declension (nikakoj, nicej)
        # tag.POS = 'Pw'

        # fixme: Indefinite pronoun with adjectival declension (samyj, ves', ...)
        # tag.POS = 'Pz'

    elif pos == 'Н':
        # Adverb without a possibility to form negation
        # and degrees of comparison (vverxu, vnizu, potom)
        tag.POS = 'Db'

#        if 'указат' in info or 'вопр' in info:
#            tag.POS = 'Db'
#        else:
#            tag.POS = 'Dg'

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

        # Indefinite numeral (mnogo, neskol'ko)
        # tag.POS = 'Ca'

        # Interrogative numeral (skol'ko)
        # tag.POS = 'Cu'

        # Multiplicative numeral (dvaždy, triždy)
        # tag.POS = 'Cv'

    elif pos == 'ЧИСЛ-П':
        tag.POS = 'Cr'

    elif pos == 'ПРЕДЛ':
        # Nonvocalized preposition (ob, pered, s, v, ...)
        tag.POS = 'RR'

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

    elif pos == 'ФРАЗ':
        # e.g. несмотря
        tag.POS = 'RF'

    # ==== 3: gender ====

    for gender in GENDERS:
        if gender in info:
            tag.gender = GENDERS[gender]
            break
    else:
        if 'мр-жр' in info:
            tag.gender = 'X' # fixme?

    # ==== 4: animacy ====
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

    # ======== 5: number =======
    if 'ед' in info:
        tag.number = 'S'
    elif 'мн' in info:
        tag.number = 'P'
    # FIXME
    # non-declinable nouns, adjectives and verbs,
    # 3rd person possessive pronouns:
    # tag.number = 'X'

    # ======== 6: case ==========
    for case in CASES:
        if case in info:
            tag.case = CASES[case]
        if '2' in info:
            tag.variant = '1'
    if 'зв' in info:
        tag.case = '1'
        tag.variant = '1'

    if '0' in info:
        tag.case = 'X'
        tag.number = 'X'

    # TODO: 7: possessor's gender
    # TODO: 8: possessor's number

    # ======= 9: person ========
    # fixme: it should be X for non-declinable verbs
    for person in PERSONS:
        if person in info:
            tag.person = PERSONS[person]
            break

    # ======= 10: reflexivity ========
    if tag.POS in ['AG', 'PP', 'P5', 'PS'] or tag.mainPOS == 'V':
        tag.reflexivity = 'I'
        # fixme: lossy! e.g. for "получиться" it should be 'R'.

    # ========= 15: voice ===========
    # XXX: this is out of order because tense needs it
    if tag.POS in ['AG', 'Ac']: # ??
        if 'дст' in info:
            tag.voice = 'A'
        elif 'стр' in info:
            tag.voice = 'P'

    # ======= 11: tense =========
    if tag.POS in ['AG', 'VB', 'Vp']: # ?
        for tense in TENSES:
            if tense in info:
                tag.tense = TENSES[tense]
                break
        # passive long participles
        if tag.POS == 'AG' and tag.tense == '-' and tag.voice == 'P':
            tag.tense = 'X'


    # TODO: 12: verbal_aspect

    # ========== 13: degree of comparison =========
    if tag.POS in ['AA', 'Dg']:
        if 'сравн' in info:
            tag.degree_of_comparison = '2'
        elif 'прев' in info:
            tag.degree_of_comparison = '3'
        else:
            tag.degree_of_comparison = '1'

    # ========= 14: negation =========
    if tag.mainPOS in ['N', 'A'] or tag.POS == 'Dg':
        tag.negation = 'A'
        # fixme: lossy!

    # ======== 16: variant ===========
    if 'арх' in info:
        tag.variant = '2'
    elif 'разг' in info:
        tag.variant = '5'
    elif 'аббр' in info:
        tag.variant = '8'

    return tag


def from_positional(positional_tag, word=None):
    """
    Convert positional.Tag to AOT format.
    This is lossy because of format differences.
    """
    if not isinstance(positional_tag, positional.Tag):
        positional_tag = positional.Tag(positional_tag)

    tag = positional_tag
    pos, info = '', set()

    if tag.POS in _POS_MAP:
        pos = _POS_MAP[tag.POS]
    elif tag.mainPOS in _POS_MAP:
        pos = _POS_MAP[tag.mainPOS]
    else:
        pos = tag.mainPOS

    # ==== 3. gender ======
    if tag.gender in GENDERS_INV:
        info.add(GENDERS_INV[tag.gender])

    # ==== 4. animacy =====
    if tag.animacy == 'A':
        info.add('од')
    elif tag.animacy == 'I':
        info.add('но')
    elif tag.animacy == 'X':
        info.update(['од', 'но'])

    # ===== 5. number =======
    if tag.number == 'P':
        info.add('мн')
    elif tag.number == 'S':
        info.add('ед')
    elif tag.number == 'X':
        pass # fixme

    # ====== 6. case =========
    if tag.case in CASES_INV:
        if tag.variant == '1':
            if tag.case == '1':
                info.add('зв')
            else:
                info.add(CASES_INV[tag.case])
                info.add('2')
        else:
            info.add(CASES_INV[tag.case])

    if tag.case == 'X' and tag.number == 'X':
        info.add('0')

    # 7. possessor's gender
    # 8. possessor's number

    # ====== 9. person ========
    if tag.person in PERSONS_INV:
        info.add(PERSONS_INV[tag.person])

    # 10. reflexivity

    # ====== 11. tense ========
    if tag.tense in TENSES_INV:
        info.add(TENSES_INV[tag.tense])

    # 12. verbal aspect

    # ====== 13. degree of comparison ======
    if tag.degree_of_comparison == '2':
        info.add('сравн')
    elif tag.degree_of_comparison == '3':
        info.add('прев')
    if tag.POS == 'Dg' and tag.degree_of_comparison == '2': # hack?
        pos = 'П'

    # 14. negation

    # ====== 15. voice ==========
    if tag.voice == 'A':
        info.add('дст')
    elif tag.voice == 'P':
        info.add('стр')
    elif tag.mainPOS == 'V' and tag.tense != 'F': # hack?
        info.add('дст')

    # ====== 16. variant ========
    if tag.variant in ['2', '3']:
        info.add('арх')
    elif tag.variant in ['5', '6', '7']:
        info.add('разг')
    elif tag.variant == '8':
        info.add('аббр')

    return ",".join([pos] + list(info))

converters.add('positional', 'aot', from_positional)
converters.add('aot', 'positional', to_positional)
