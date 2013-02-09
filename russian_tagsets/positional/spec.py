# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

# THIS IS UNUSED AND DOESN'T WORK

from fnmatch import fnmatchcase

_RESTRICTIONS = [
    # only nouns distinguish gender in plural
    '[FNM].P.* => N.*',

    # for non-nouns, animacy is specified only for masc.sg.acc and pl.acc.
    '[^N]..[AI].* => ..M.S4.* ....P4.*',

    # AG (long participle) => tv \in {PA,RA,XP}
    'AG.* => AG....---.P.-.A- AG....---.R.-.A- AG....---.X.-.P-',

    # PP (personal pronoun)
    'PP--..--.I------ => PP--..--[12]I------',
    'PP......3.* => .....[^6].*',   # locative only after preposition
    'P5.* => .....[^1].*',   # nominative only without preposition

    # 3rd person possessive pronouns
    'PS......3.* => PSXXXX[MFN]S3.* PSXXXXXP3.*',

    # imperative only in 2nd person
    'Vi.* => .{8}2.*',

    # past tense
    '10 R => AG.* VB.*',

    # X gender
    #   no agr gender in plural
    #   plural tantum noun
    #   foreign/abbr
    #   3rd person pers. pronoun
    #   "CnXP.*",    # !! TODO check
    '2 X => A.X.P.* P[8DSqwz]X.P.* PSXXXX..3.* CnX.P.* CrX.P.* VBX.P.*    NNX.P.*    NNXXXX.* AAXXXX.*    P[P5]X-P.--3.*',

    # X animacy. TODO what else. Plural agreement?
    #3 X => AAXXXX.* NNXXXX.* PSXXXX..3.*

    # X number - foreign/abbr  PP
    '4 X => NN..XX.* AAXXXX.* VB--X---XP..*   PSXXXX..3.*',

    # X case - foreign/abbr PS
    '5 X => NN..[PSX]X.* AAXXXX.*     PSXXXX..3.*',

    # .......X.......
    # X possessor's gender
    '6 X => PSXXXXXP3.*',

    # person .......X....... - # foreign
    '8 X => VB--X---X.P.*',

    # tense # TODO check voice
    '10 X => AG.*',
]

def split_parts(restriction):
    condition, conclusions = restriction.split(' => ')
    return condition.strip(), conclusions.strip().split()

def normalize_condition(condition):
    if condition[0].isdigit():
        num, value = condition.split()
        condition = '.'*(int(num)) + value + '*'
    return condition

def prepare_for_fnmatch(pattern):
    return pattern.replace('X', '[!-]').replace('^', '!').replace('.', '?')

RESTRICTIONS = [
    [
        prepare_for_fnmatch(normalize_condition(condition)),
        map(prepare_for_fnmatch, conclusions)
    ]
    for condition, conclusions in map(split_parts, _RESTRICTIONS)
]

class TagValidationError(Exception):
    pass


def validate(tag_string):
    if len(tag_string) == 15:
        tag_string += '-'

    if len(tag_string) != 16:
        raise TagValidationError('length is incorrect')

    for condition, conclusions in RESTRICTIONS:
        print("Matching ", condition)
        if fnmatchcase(tag_string, condition):
            print("Matched, checking condition ...")

            if not any([fnmatchcase(tag_string, conclusion) for conclusion in conclusions]):
                raise TagValidationError("%s is not matched by %s" % (tag_string, conclusions))

            print('passed')


SPEC = """
// =============================================================================
// Specification of the (new) Russian tagset (16 slots)
// =============================================================================

// =============================================================================
// Note that the variant slot is ignored except abbrs.

// =============================================================================
// values for individual slots;
// =============================================================================
// slots with <null> are fully specified by templates below
// psgyncfmertbdavi

null
null
FMNX
AIX
PSX
123467X
FMNX
PS
123X
RI
FPRX
PIX
123
AN
AP
null
}



// =============================================================================
// Templates
// =============================================================================
// ? are replace by all values satisfying restrictions


NN????-------?--
AA????------??--
AC?-?--------?--
AG????---???-??-
AU?????------?--
Ac?-?--------?P-
PP--??--?I------
PP?-??--3I------
PP---?---R------
P5?-??--3I------
PD????----------
PW---?----------
Pw????----------
PS????-??I------
PSXXXX??3I------
PS????---R------
PQ---?----------
Pq????----------
PZ---?----------
Pz????----------
C=--------------
C}--------------
Cn????----------
Cn??-?----------
Cn-?-?----------
Cn--??----------
Cr????----------
Cj-?-?----------
Cu---?----------
Ca---?----------
Ca????----------
Cv--------------
VB--?---????----
VB?-?----?R?----
Ve-------?-?----
Vf-------?-?----
Vi--?---??-?----
Db--------------
Dg----------??--
RR---?----------
RV---?----------
RF--------------
J^--------------
J,--------------
TT--------------
II--------------
Z#--------------
Z:--------------
X0--------------
XX--------------


// abbreviations
AAXXXX------1A-8
Db-------------8
J^-------------8
NNFAPX-------A-8
NNFIPX-------A-8
NNFASX-------A-8
NNFISX-------A-8
NNFAXX-------A-8
NNFIXX-------A-8
NNMIPX-------A-8
NNMAPX-------A-8
NNMISX-------A-8
NNMASX-------A-8
NNMIXX-------A-8
NNMAXX-------A-8
NNNIPX-------A-8
NNNAPX-------A-8
NNNISX-------A-8
NNNASX-------A-8
NNNIXX-------A-8
NNNAXX-------A-8
NNXXXX-------A-8
}
"""