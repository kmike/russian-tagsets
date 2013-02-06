# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from russian_tagsets import rule_engine

RULES1 = """
NOUN => S

# comment:
# ADJS => A,brev

COMP,Cmp2 => A,comp2
| => =
"""

RULES2 = """
NOUN => S

ADJS => A,brev
ADJF => A

COMP,Cmp2 => A
COMP,Supr => A,supr,dupr
COMP => A,comp

VERB => V
PRTF => V,partcp
PRTS => V,partcp,brev

sing => sg
plur => pl
"""

def _transform_tag(tag):
    rules = rule_engine.parse(RULES2)
    return ','.join(
        rule_engine.apply_rules(rules, tag.split(','))
    )

def test_parsing():
    assert rule_engine.parse(RULES1) == [
        (['NOUN'], ['_S']),
        (['COMP', 'Cmp2'], ['_A', '_comp2']),
        (['|'], ['_='])
    ]

TEST_DATA = [
    ('NOUN,sing,foo', 'S,sg'),
    ('ADJS', 'A,brev'),
    ('ADJS,sing', 'A,brev,sg'),
    ('COMP', 'A,comp'),
    ('COMP,sing,Cmp2,plur', 'A,sg,pl'),
    ('COMP,sing,Supr,plur,vupr', 'A,sg,supr,dupr,pl'),
]

@pytest.mark.parametrize(("in_tag", "out_tag"), TEST_DATA)
def test_apply(in_tag, out_tag):
    assert _transform_tag(in_tag) == out_tag