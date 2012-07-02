# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters
from russian_tagsets import positional


class TestConversion(object):

    TAGS = [
        [('МС', '3л,мр,ед,им'), 'PPM-S1--3I------'], # он
        [('Г', 'дст,прш,мр,ед'), 'VBM-S----IR-----'], # купил

        #[('МС-П', 'жр,ед,вн,од,но'), 'PSFIS4-P1I------'], # нашу:
        [('МС-П', 'жр,ед,вн,од,но'), 'PSFXS4---I------'], # not enough info

        [('П', 'жр,ед,вн,од,но'), 'AAFXS4------1A--'], # старую
        [('С', 'жр,ед,вн'), 'NNF-S4-------A--'], # фотографию
    ]

    @pytest.mark.parametrize(("aot_tag", "pos_tag_txt"), TAGS)
    def test_from_positional(self, aot_tag, pos_tag_txt):
        converted = converters.convert(
            positional.Tag(pos_tag_txt),
            'positional', 'aot'
        )
        assert converted == aot_tag

    @pytest.mark.parametrize(("aot_tag", "pos_tag_txt"), TAGS)
    def test_to_positional(self, aot_tag, pos_tag_txt):
        converted = converters.convert(aot_tag, 'aot', 'positional')
        assert str(converted) == pos_tag_txt
