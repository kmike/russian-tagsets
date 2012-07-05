# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters

class TestInternalConversion(object):
    TEST_DATA = [
        ['власть', 'NOUN,inan,femn,sing,nomn', 'СУЩ,неод,жр,ед,им'],
        ['поменяться', 'INFN,perf,intr', 'ИНФ,сов,неперех'],
        ['.', 'PNCT', 'PNCT'],
    ]

    @pytest.mark.parametrize(("word", "internal", "external"), TEST_DATA)
    def test_from_internal(self, word, internal, external):
        converted = converters.convert(internal, 'opencorpora-int', 'opencorpora')
        assert converted == external

    @pytest.mark.parametrize(("word", "internal", "external"), TEST_DATA)
    def test_to_internal(self, word, internal, external):
        converted = converters.convert(external, 'opencorpora', 'opencorpora-int')
        assert converted == internal
