# -*- coding: utf-8 -*-
"""
Python implementation of http://ufal.mff.cuni.cz/~hana/morph/rutags.html

(Jirka Hana and Anna Feldman (2010). A Positional Tagset for Russian.
In: Proceedings of the 7th International Conference on Language Resources
and Evaluation ({LREC} 2010)}. European Language Resources
Association. pp. 1277-1284.)

"""
from __future__ import absolute_import, unicode_literals, print_function
import collections
import array

TagInfo = collections.namedtuple('TagInfo', 'position letter name full_name values')

TAGS_POSITIONS = [
    TagInfo(1, 'p', 'POS', 'Part of Speech', {
        'N': 'Noun',
        'A': 'Adjective',
        'P': 'Pronoun',
        'C': 'Numeral',
        'V': 'Verb',
        'D': 'Adverb',
        'R': 'Preposition',
        'J': 'Conjunction',
        'I': 'Interjection',
        'T': 'Particle',
        'Z': 'Punctuation',
        'X': 'Unknown, special use',
    }),

    TagInfo(2, 's', 'subPOS', 'SubPOS (Detailed Part of Speech)', {
        '#': 'Z: Sentence boundary',
        ',': 'J: Subordinate conjunction (esli, čto, kotoryj)',
        '0': 'X: Part of a multiword foreign phrase',
        '5': 'P: 3rd person pronoun in prepositional forms (nego, nej, ...)',
        ':': 'Z: Punctuation',
        '=': 'C: Number written using digits',
        'A': 'A: Adjective (long, non-participle) (xorosij, ploxoj)',
        'B': 'V: Verb in present, past or rarely future form (čitaju, splju, pišum, spal, ždal)',
        'C': 'A: Short adjective (non-participle) (surov, krasiv)',
        'D': 'P: Pronoun demonstrative (ètot, tot, sej, takoj, èkij, ... )',
        'F': 'R: Part of a preposition; never appears isolated (nesmotrja)',
        'G': 'A: Participle, active or long passive (čitajuscij, čitavsij, pročitavšij, čitaemyj; but not pročitannyj (AA), pročitan (Ac)',
        'I': 'I: Interjection (oj, aga, m-da)',
        'N': 'N: Noun',
        'P': 'P: Personal pronoun (ja, my, ty, vy, on, ona, ono, oni, sebja)',
        'Q': 'P: Relative/interrogative pronoun with nominal declension (kto, čto)',
        'R': 'R: Nonvocalized preposition (ob, pered, s, v, ...)',
        'S': 'P: Possessive pronoun (moj, ego, svoj, ..)',
        'T': 'T: Particle (li)',
        'U': "A: Possessive adjective (mamin, oveč'ju)",
        'V': 'R: Vocalized preposition (obo, peredo, so, vo, ...)',
        'W': 'P: Negative pronoun with nominal declension (nicto, nikto)',
        'X': 'X: Unknown, special use',
        'Z': "P: Indefinite pronoun with nominal declension (kto-to, kto-nibud', cto-to, ...)",
        '^': 'J: Non-subordinate conjunction (i, a, xotja, pricem)',
        'a': "C: Indefinite numeral (mnogo, neskol'ko)",
        'b': 'D: Adverb without a possibility to form negation and degrees of comparison (vverxu, vnizu, potom)',
        'c': 'A: Short passive participle (procitan)',
        'e': 'V: Gerund (delaja; pridja, otpisav)',
        'f': "V: Infinitive (delat', spat')",
        'g': 'D: Adverb forming negation and degrees of comparison (vysoko, daleko)',
        'i': 'V: Imperative (spi, sdelaj, pročti)',
        'j': 'C: Generic/collective numeral (dvoje, četvero)',
        'n': 'C: Cardinal numeral (odin, tri, sorok)',
        'q': 'P: Relative/interrogative pronoun with adjectival declension (kakoj, kotoryj, cej, ...)',
        'r': 'C: Ordinal numeral (pervyj, tretij)',
        'u': "C: Interrogative numeral (skol'ko)",
        'v': 'C: Multiplicative numeral (dvaždy, triždy)',
        'w': 'P: Negative pronoun with adjectival declension (nikakoj, nicej)',
        'z': "P: Indefinite pronoun with adjectival declension (samyj, ves', ...)",
        '}': 'C: Number written using Roman numerals (XIV)',
    }),

    TagInfo(3, 'g', 'gender', 'Gender', {
        'F': 'Feminine',
        'M': 'Masculine',
        'N': 'Neuter',
        'X': 'Any gender',
    }),
    TagInfo(4, 'y', 'animacy', 'Animacy', {
        'A': 'Animate',
        'I': 'Inanimate',
        'X': 'Either',
    }),
    TagInfo(5, 'n', 'number', 'Number', {
        'P': 'Plural',
        'S': 'Singular',
        'X': 'Any number'
    }),
    TagInfo(6, 'c', 'case', 'Case', {
        '1': 'Nominative',
        '2': 'Genitive',
        '3': 'Dative',
        '4': 'Accusative',
        '6': 'Locative',
        '7': 'Instrumental',
        'X': 'Any case'
    }),
    TagInfo(7, 'f', 'possessors_gender', "Possessor's Gender", {
        'F': 'Feminine possessor',
        'M': 'Masculine possessor',
        'N': 'Neuter possessor',
        'X': 'Possessor of any gender',
    }),
    TagInfo(8, 'm', 'possessors_number', "Possessor's Number", {
        'S': 'Singular possessor',
        'P': 'Plural possessor',
    }),
    TagInfo(9, 'e', 'person', 'Person', {
        '1': '1st person',
        '2': '2nd person',
        '3': '3rd person',
        'X': 'Any person',
    }),
    TagInfo(10, 'r', 'reflexivity', 'Reflexivity', {
        'I': 'Irreflexive',
        'R': 'Reflexive',
    }),
    TagInfo(11, 't', 'tense', 'Tense', {
        'F': 'Future',
        'P': 'Present',
        'R': 'Past',
        'X': 'Any (Past, Present, or Future)',
    }),
    TagInfo(12, 'b', 'verbal_aspect', 'Verbal aspect', {
        'P': 'perfective',
        'I': 'imperfective',
        'X': 'either aspect',
    }),
    TagInfo(13, 'd', 'degree_of_comparison', 'Degree of comparison', {
        '1': 'Positive',
        '2': 'Comparative',
        '3': 'Superlative',
    }),
    TagInfo(14, 'a', 'negation', 'Negation', {
        'A': 'Affirmative (not negated)',
        'N': 'Negated',
    }),
    TagInfo(15, 'v', 'voice', 'Voice', {
        'A': 'Active',
        'P': 'Passive',
    }),
    TagInfo(16, 'i', 'variant', 'Variant, Abbreviation', {
        '1': 'Variant (generally less frequent)',
        '2': 'Variant (generally rarely used, bookish, or archaic)',
        '3': 'Variant (very archaic)',
        '5': 'Variant (colloquial)',
        '6': 'Variant (colloquial, generally less frequent)',
        '7': 'Variant (colloquial, generally less frequent)',
        '8': 'Abbreviations'
    }),
]

def _fget(ind):
    def fget(self):
        return self._data[ind]
    return fget

def _fset(ind):
    def fset(self, value):
        if value != '-' and value not in TAGS_POSITIONS[ind].values:
            raise ValueError('Invalid value %s' % value)
        self._data[ind] = value
    return fset

def _prop(ind):
    return _fget(ind), _fset(ind)


class Tag(object):
    def __init__(self, txt='-'*16):
        if isinstance(txt, bytes):
            txt = txt.decode('ascii')
        self._data = array.array(str('u'), txt)

    mainPOS = property(*_prop(0))
    subPOS = property(*_prop(1))
    gender = property(*_prop(2))
    animacy = property(*_prop(3))
    number = property(*_prop(4))
    case = property(*_prop(5))
    possessors_gender = property(*_prop(6))
    possessors_number = property(*_prop(7))
    person = property(*_prop(8))
    reflexivity = property(*_prop(9))
    tense = property(*_prop(10))
    verbal_aspect = property(*_prop(11))
    degree_of_comparison = property(*_prop(12))
    negation = property(*_prop(13))
    voice = property(*_prop(14))
    variant = property(*_prop(15))

    # 2-letter POS
    def _get_pos(self):
        return self._data[0:2].tounicode()
    def _set_pos(self, txt):
        self.mainPOS, self.subPOS = txt[0], txt[1]
    POS = property(_get_pos, _set_pos)


    def is_valid(self):
        if len(self._data) != 16:
            return False

        for index, c in enumerate(self):
            if c == '-':
                continue
            if c not in TAGS_POSITIONS[index].values:
                return False

        return True

    def verbose_info(self):
        return dict((
            (TAGS_POSITIONS[index].name, TAGS_POSITIONS[index].values[tag])
            for index, tag in enumerate(self) if tag != '-'
        ))

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return self._data.tounicode() # this is not correct under python 2.x

    def __repr__(self):
        return 'Tag("%s")' % self


if __name__ == '__main__':
    print(Tag("NNFIS7-------A--").verbose_info())
