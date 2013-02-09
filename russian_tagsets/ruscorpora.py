# -*- coding: utf-8 -*-
"""
Conversion between Russian National Corpus (www.ruscorpora.com)
tagset and other tagsets (currently OpenCorpora tagset).

Limitations:

* OpenCorpora has grammemes for active/passive voices; RNC
  has active/passive/middle voices. "Passive" is reliable,
  "active/middle" are not.

* tagsets differ in pronoun/adverb/numeral/predicative/transitions handling;
  this module tries not to be too smart: it only applies unambiguous
  transformations;

* Abbr mean different things in OpenCorpora and RNC;

* RNC's adnum is not the same as OpenCorpora's Coun;

* OpenCorpora Comparative is always converted to A, while it may be
  A, ADV, NUM and PRAEDIC in RNC (there is not enough information to make
  the 1-to-1 conversion);
"""

from __future__ import absolute_import, unicode_literals
from russian_tagsets import rule_engine
from russian_tagsets import converters

OPENCORPORA_CONVERSION_RULES = rule_engine.parse("""
# part of speech
NOUN => S

ADJF,Apro => A-PRO
ADJF,Anum => ANUM
ADJF => A,plen
ADJS => A,brev

COMP,Cmp2 => A,comp2
COMP,Supr => A,supr
COMP => A,comp

# INFN => V,inf,med
# INFN => V,inf,act
INFN => V,inf

PRTF,inan => V,partcp,plen
PRTF,anim => V,partcp,plen
PRTF => V,partcp,plen

PRTS,intr => V,intr,partcp,plen
PRTS => V,tran,partcp,brev

GRND => V,ger

VERB,impr,excl => V,2p,imper
VERB,impr,incl => V,1p,imper
VERB => V

NUMR,inan => NUM
NUMR => NUM

PRED,pres => PRAEDIC
PRED => PRAEDIC

ADVB,Ques => ADV-PRO
ADVB => ADV

NPRO => S-PRO
PREP => PR
PRCL => PART
INTJ => INTJ

CONJ,Prnt => PARENTH
CONJ => CONJ

# animacy
anim => anim
inan => inan

# gender
femn,Ms-f => m-f
masc,Ms-f => m-f
neut,Ms-f => m-f
Ms-f => m-f

masc => m
femn => f
neut => n

# number
sing => sg
plur => pl
Fixd => 0

# case
nomn => nom
gent => gen
datv => dat
accs => acc
ablt => ins
loct => loc
voct => voc
gen1 => gen
gen2 => gen2
acc2 => acc2
loc1 => loc
loc2 => loc2

# Abbr doesn't mean the same
# Abbr => abbr

Name => persn
Surn => famn
Patr => patrn
Dist => distort
Arch => anom

# ??
Litr => anom
# Infr => anom
# V-oy => anom
V-be => distort

Supr => supr

# --
# ??
Coun => adnum

# aspect
perf => pf
impf => ipf

# transitivity
tran => tran
intr => intr

# voice
actv => act
pssv => pass

# person
1per => 1p
2per => 2p
3per => 3p

# tense
pres => praes
past => praet
futr => fut

# mood
indc => indic
impr => imper

# hack to preserve whitespace info:
| => =
""")

def from_opencorpora_int(open_tag):
    """
    Convert OpenCorpora tag to www.ruscorpora.com tag::

        >>> print(from_opencorpora_int('NOUN,inan,masc sing,nomn'))
        S,inan,m=sg,nom

    """

    # Whitespace is replaced with ",|,"
    # then "|" is treated as token and replaced with "=",
    # then commas around "=" are removed in result.
    # This way space is converted to "=".

    tag = open_tag.replace(' ', ',|,').split(',')
    result = rule_engine.apply_rules(OPENCORPORA_CONVERSION_RULES, tag)
    return ','.join(result).replace(',=,', '=').replace(',=', '')


converters.add('opencorpora-int', 'ruscorpora', from_opencorpora_int)