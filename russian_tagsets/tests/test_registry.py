# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from russian_tagsets import converters

class TransformTest(unittest.TestCase):

    def test_transform_path(self):
        reg = converters.Registry()

        ident = lambda obj: obj
        reg.add('A', 'B', ident)
        reg.add('C', 'B', ident)
        reg.add('A', 'C', ident)
        reg.add('B', 'A', ident)
        reg.add('C', 'D', ident)

        self.assertEqual(reg.path('A', 'B'), ['A', 'B'])
        self.assertEqual(reg.path('A', 'C'), ['A', 'C'])
        self.assertEqual(reg.path('B', 'C'), ['B', 'A', 'C'])
        self.assertEqual(reg.path('A', 'A'), ['A'])
        self.assertEqual(reg.path('C', 'A'), ['C', 'B', 'A'])
        self.assertEqual(reg.path('B', 'D'), ['B', 'A', 'C', 'D'])
        self.assertRaises(converters.NoConvertPath, reg.path, 'D', 'A')

    def test_transform(self):
        reg = converters.Registry()
        reg.add('lower', 'upper', lambda s, _: s.upper())
        reg.add('upper', 'none', lambda s, _: None)
        reg.add('upper', 'lower', lambda s, _: s.lower() if s.isupper() else 'Error')

        self.assertEqual(reg.convert('foo', 'lower', 'upper'), 'FOO')
        self.assertEqual(reg.convert('foo', 'lower', 'lower'), 'foo')
        self.assertEqual(reg.convert('FOO', 'upper', 'lower'), 'foo')
        self.assertEqual(reg.convert('foo', 'lower', 'none'), None)
