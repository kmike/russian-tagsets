# -*- coding: utf-8 -*-
"""
Conversion between OpenCorpora and Universal Dependencies dialect
used for http://www.dialog-21.ru/evaluation/2017/morphorueval/.

See https://github.com/dialogue-evaluation/morphoRuEval-2017/blob/master/morphostandard
"""
from __future__ import absolute_import, unicode_literals
from copy import deepcopy

from russian_tagsets import converters
from russian_tagsets.ud import Tag14

__all__ = ['TagDialog2017', 'from_opencorpora']


class TagDialog2017(Tag14):
    GRAM_MAP = deepcopy(Tag14.GRAM_MAP)
    GRAM_MAP['_POS']['PRTF'] = 'ADJ'
    GRAM_MAP['_POS']['PRTS'] = 'ADJ'
    GRAM_MAP['_POS']['PRED'] = 'ADJ'
    GRAM_MAP['Tense']['futr'] = 'Notpast'
    GRAM_MAP['Tense']['pres'] = 'Notpast'
    GRAM_MAP['Degree']['Supr'] = 'Pos'

    def _postprocess(self):
        super(TagDialog2017, self)._postprocess()

        if self.pos in {'ADJ', 'ADV'} and 'Degree' not in self.grammemes:
            self.grammemes['Degree'] = 'Pos'


def from_opencorpora(oc_tag, word=None):
    tag = TagDialog2017(oc_tag)

    if word is not None:
        word = word.lower()

        if word == "более" and 'Degree' not in tag.grammemes:
            tag.grammemes['Degree'] = 'Сmp'

        if word in HARDCODED_PARSES:
            return HARDCODED_PARSES[word]

    return str(tag)


HARDCODED_PARSES = {
    'нет': 'VERB Mood=Ind|Number=Sing|Person=3|Tense=Notpast|VerbForm=Fin',
}


# XXX: this list is currently unused.
# By assigning all words from this list "DET" POS tag evaluation quality of
# pymorphy2 can be improved, but this happens only because pymorphy2
# really likes to assign NPRO tag, while Apro seems more common.
DET_WORDS = set("""
ваш
весь
всякий
всяк
другой
его
её
иной
ихний
их
каждый
каков
какой
какой-либо
какой-нибудь
какой-то
кой
который
который-нибудь
любой
многие
мой
наш
некий
некоторый
немногие
никакой
ничей
оный
прочий
проч.
пр.
свой
сей
таков
такой
твой
тот
чей
чей-либо
чей-нибудь
чей-то
этакий
этот
""".strip().replace('ё', 'е').split())


converters.add('opencorpora-int', 'dialog2017', from_opencorpora)
