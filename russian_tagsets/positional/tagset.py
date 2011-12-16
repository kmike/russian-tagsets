# -*- coding: utf-8 -*-
from __future__ import absolute_import
import collections


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
        '#': u'Z: Sentence boundary',
        ',': u'J: Subordinate conjunction (esli, čto, kotoryj)',
        '0': u'X: Part of a multiword foreign phrase',
        '5': u'P: 3rd person pronoun in prepositional forms (nego, nej, ...)',
        ':': u'Z: Punctuation',
        '=': u'C: Number written using digits',
        'A': u'A: Adjective (long, non-participle) (xorosij, ploxoj)',
        'B': u'V: Verb in present, past or rarely future form (čitaju, splju, pišum, spal, ždal)',
        'C': u'A: Short adjective (non-participle) (surov, krasiv)',
        'D': u'P: Pronoun demonstrative (ètot, tot, sej, takoj, èkij, ... )',
        'F': u'R: Part of a preposition; never appears isolated (nesmotrja)',
        'G': u'A: Participle, active or long passive (čitajuscij, čitavsij, pročitavšij, čitaemyj; but not pročitannyj (AA), pročitan (Ac)',
        'I': u'I: Interjection (oj, aga, m-da)',
        'N': u'N: Noun',
        'P': u'P: Personal pronoun (ja, my, ty, vy, on, ona, ono, oni, sebja)',
        'Q': u'P: Relative/interrogative pronoun with nominal declension (kto, čto)',
        'R': u'R: Nonvocalized preposition (ob, pered, s, v, ...)',
        'S': u'P: Possessive pronoun (moj, ego, svoj, ..)',
        'T': u'T: Particle (li)',
        'U': u"A: Possessive adjective (mamin, oveč'ju)",
        'V': u'R: Vocalized preposition (obo, peredo, so, vo, ...)',
        'W': u'P: Negative pronoun with nominal declension (nicto, nikto)',
        'X': u'X: Unknown, special use',
        'Z': u"P: Indefinite pronoun with nominal declension (kto-to, kto-nibud', cto-to, ...)",
        '^': u'J: Non-subordinate conjunction (i, a, xotja, pricem)',
        'a': u"C: Indefinite numeral (mnogo, neskol'ko)",
        'b': u'D: Adverb without a possibility to form negation and degrees of comparison (vverxu, vnizu, potom)',
        'c': u'A: Short passive participle (procitan)',
        'e': u'V: Gerund (delaja; pridja, otpisav)',
        'f': u"V: Infinitive (delat', spat')",
        'g': u'D: Adverb forming negation and degrees of comparison (vysoko, daleko)',
        'i': u'V: Imperative (spi, sdelaj, pročti)',
        'j': u'C: Generic/collective numeral (dvoje, četvero)',
        'n': u'C: Cardinal numeral (odin, tri, sorok)',
        'q': u'P: Relative/interrogative pronoun with adjectival declension (kakoj, kotoryj, cej, ...)',
        'r': u'C: Ordinal numeral (pervyj, tretij)',
        'u': u"C: Interrogative numeral (skol'ko)",
        'v': u'C: Multiplicative numeral (dvaždy, triždy)',
        'w': u'P: Negative pronoun with adjectival declension (nikakoj, nicej)',
        'z': u"P: Indefinite pronoun with adjectival declension (samyj, ves', ...)",
        '}': u'C: Number written using Roman numerals (XIV)',
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
    TagInfo(7, 'f', 'possessors_gender', 'Possessor\'s Gender', {
        'F': 'Feminine possessor',
        'M': 'Masculine possessor',
        'N': 'Neuter possessor',
        'X': 'Possessor of any gender',
    }),
    TagInfo(8, 'm', 'possessors_number', 'Possessor\'s Number', {
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


_PositionalTag = collections.namedtuple(
    'PositionalTag', [pos.name for pos in TAGS_POSITIONS]
)


class PositionalTag(_PositionalTag):

    @classmethod
    def fromstr(cls, string):
        assert len(string) == 16
        return cls(*string)


    def is_valid(self):
        if len(self) != 16:
            return False

        for index, c in enumerate(self):
            if c == '-':
                continue
            if c not in TAGS_POSITIONS[index].values:
                return False

        return True


    def verbose_info(self):
        return [
            [TAGS_POSITIONS[index].name, TAGS_POSITIONS[index].values[tag]]
            for index, tag in enumerate(self) if tag != '-'
        ]



if __name__ == '__main__':
    print PositionalTag.fromstr("NNFIS7-------A--").verbose_info()
