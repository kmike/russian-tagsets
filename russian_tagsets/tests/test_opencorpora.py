# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters, aot
from .opencorpora_aot_data import PARSE_RESULTS

class TestInternalConversion(object):
    TEST_DATA = [
        ['власть', 'NOUN,inan,femn sing,nomn', 'СУЩ,неод,жр ед,им'],
        ['поменяться', 'INFN,perf,intr', 'ИНФ,сов,неперех'],
        ['.', 'PNCT', 'PNCT'],
    ]

    @pytest.mark.parametrize(("word", "internal", "external"), TEST_DATA)
    def test_from_internal(self, word, internal, external):
        converted = converters.convert(internal, 'opencorpora-int', 'opencorpora-ext')
        assert converted == external

    @pytest.mark.parametrize(("word", "internal", "external"), TEST_DATA)
    def test_to_internal(self, word, internal, external):
        converted = converters.convert(external, 'opencorpora-ext', 'opencorpora-int')
        assert converted == internal


def _remove_unsupported(aot_tag):
    pos, info = aot.split_tag(aot_tag)
    info.difference_update(
        set(['од', 'но', '2', 'имя', 'фам', 'лок', 'кач', 'разг'])
    )
#    if pos == 'ДЕЕПРИЧАСТИЕ':
    info.discard('дст')

    if pos == 'С':
        if 'аббр' in info:
            info.difference_update(set(aot.CASES.keys()))

    return aot.join_tag(pos, info)


class TestAotConversion(object):

    @pytest.mark.parametrize(("word", "open_tag", "aot_tag"), PARSE_RESULTS)
    def test_to_aot(self, word, open_tag, aot_tag):
        converted = converters.convert(open_tag, 'opencorpora-ext', 'aot')
        assert aot.split_tag(_remove_unsupported(converted)) == aot.split_tag(_remove_unsupported(aot_tag))