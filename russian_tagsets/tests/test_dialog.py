# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters
from russian_tagsets import aot #, dialog2010
from .dialog2010_data import TEST_DATA

def _gram_info_match(expected, actual_tag_set):
    #actual_tags = set(gr for gr in actual.split(',') if gr)

    if expected.startswith('[') and expected.endswith(']'):
        # all tags are optional
        expected = expected.strip('[]').replace('[,', ',[').split(',')
        must_tags = set([])
        allowed_tags = set(gr.strip('[]') for gr in expected)
    else:
        expected = expected.replace('[,', ',[').split(',')
        must_tags = set([gr for gr in expected if not gr.startswith('[')])
        allowed_tags = set([gr.strip('[]') for gr in expected])

#    print actual_grammems, ' || ', must_grammems, ' | ' , allowed_grammems

    return must_tags.issubset(actual_tag_set) and \
           allowed_tags.issuperset(actual_tag_set)


class TestConversion(object):

#    def assertPositionalEqual(self, converted, gold):
#        assert _remove_unsupported_pos(converted) == _remove_unsupported_pos(gold)

    def assertTagEqual(self, converted, gold):
        pos_gold, info_gold = aot.split_tag_raw(gold)
        pos_got, info_got = aot.split_tag(converted)
        assert pos_gold == pos_got
        assert _gram_info_match(info_gold, info_got)

        #assert aot.split_tag(converted) == aot.split_tag(gold)

    @pytest.mark.parametrize(("word", "dialog_tag", "aot_tag"), TEST_DATA)
    def test_from_aot(self, word, dialog_tag, aot_tag):
        converted = converters.convert(aot_tag, 'aot', 'dialog2010')
        self.assertTagEqual(converted, dialog_tag)

#    @pytest.mark.parametrize(("word", "dialog_tag", "aot_tag"), TEST_DATA)
#    def test_to_aot(self, word, pos_tag_txt, aot_tag):
#        converted = converters.convert(aot_tag, 'aot', 'positional')
#        self.assertPositionalEqual(converted, pos_tag_txt)
