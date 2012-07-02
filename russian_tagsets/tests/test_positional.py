# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import unittest
from russian_tagsets import positional

class TagTest(unittest.TestCase):
    def test_validate(self):
        self.assertFalse(positional.Tag('sdgdhsgdhdgavbhk').is_valid())

        tag = positional.Tag('NNFIS7-------A--')
        self.assertTrue(tag.is_valid())

    def test_str(self):
        tag_txt = 'NNFIS7-------A--'
        tag = positional.Tag(tag_txt)
        self.assertEqual(str(tag), tag_txt)

    def test_attributes(self):
        tag = positional.Tag('NNFIS7-------A--')
        self.assertEqual(tag.POS, 'NN')
        tag.POS = 'VV'
        self.assertEqual(str(tag), 'VVFIS7-------A--')

