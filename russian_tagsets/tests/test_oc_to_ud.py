# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters, ud
#from .opencorpora_aot_data import PARSE_RESULTS

class TestInternalConversion(object):
    TEST_DATA = [
        #Noun, Verb, ADJF, ADVB, PRTF, PRTS, NUMB, COMP
        #GNdr, Pltm, Sgtm, Ms-f, Inmx, Name, Surn, Patr, Fixd
        #inan, anim - Noun, anim, inan - ADJF/PRTF
        #femn, masc, neut; sing plur; nomn, gent, datv, accs, ablt, loct
        #Anum, Qual,
        #perf, impr; intr, tran; pres, past, !!!; indc, !!!; actv pssv;
        ['власть', 'NOUN,inan,femn sing,nomn', 'NOUN Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing'],
        #непонятно, как они приписали род
        ['суток', 'NOUN,inan,GNdr,Pltm,plur,gent', 'NOUN Animacy=Inan|Case=Gen|Gender=Fem|Number=Plur'],
        #МИКРОБ!!! у нас выбираем одуш у леммы, а у формы вин ставим другую одуш - у них видимо две леммы
        ['персонаж', 'NOUN,anim,masc,Inmx,sing,inan,accs', 'NOUN Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing'],
        ['персонажа', 'NOUN,anim,masc,Inmx,sing,accs', 'NOUN Animacy=Anim|Case=Acc|Gender=Masc|Number=Sing'],
        ['персонаж', 'NOUN,anim,masc,Inmx,sing,nomn', 'NOUN Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing'],
        ['персонаж', 'NOUN,anim,masc,Inmx,sing,nomn', 'NOUN Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing'],
        ['ивана', 'NOUN,anim,masc,Name sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Masc|Number=Sing'],
        ['иванова', 'NOUN,anim,masc,Sgtm,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Masc|Number=Sing'],
        ['гиппиус', 'NOUN,anim,femn,Sgtm,Fixd,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Fem|Number=Sing'],
        #похоже, что мн у фамилий только в мр (нужно проверить)
        ['ивановы', 'NOUN,anim,GNdr,Ms-f,Pltm,Surn,plur,nomt', 'PROPN Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing'],
        ['ивановичем', 'NOUN,anim,masc,Patr,sing,ablt', 'PROPN Animacy=Anim|Case=Ins|Gender=Masc|Number=Sing'],
        #если не изменяемая фам по обоим родам, то у нам одна лемма Sgtm, у них видимо две леммы (проверить)
        #странно, что у нам только ед ч
        ['винчи', 'NOUN,anim,GNdr,Ms-f,Sgtm,Fixd,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Masc|Number=Sing'],
        ['винчи', 'NOUN,anim,GNdr,Ms-f,Sgtm,Fixd,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Fem|Number=Sing'],
        

        ['поменяться', 'INFN,perf,intr', 'VERB Aspect=Perf|VerbForm=Inf'],
        ['было', 'VERB,impf,intr neut,sing,past,indc', 'AUX Aspect=Imp|Gender=Neut|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin'], #"было сделано" (вспм) vs. "было уязвимо" (глагол)
        ['было', 'VERB,impf,intr neut,sing,past,indc', 'VERB Aspect=Imp|Gender=Neut|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin'], #"было дано" (вспм) vs. "в классе было 20 человек" (глагол)
        ['написана', 'PRTS,perf,past,pssv,femn,sing', 'VERB Animacy=Inan|Aspect=Perf|Case=Nom|Gender=Fem|Number=Sing|Tense=Past|Variant=Brev|VerbForm=Part|Voice=Pass'],

        ['первом', 'ADJF,Anum,masc,sing,loct', 'ADJ Animacy=Inan|Case=Loc|Gender=Masc|Number=Sing'],
        ['первого', 'ADJF,Anum,anim,masc,sing,accs', 'ADJ Animacy=Anim|Case=Acc|Gender=Masc|Number=Sing'],
        ['большая', 'ADJF,Qual,femn,sing,nomn', 'ADJ Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing|Variant=Full'],
        ['студенческих', 'ADJF,plur,loct', 'ADJ Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing|Variant=Full'],
        #по инструкции должно быть прил
        ['сделанный', 'PRTF,perf,tran,past,pssv,inan,masc,sing,accs', 'VERB Animacy=Inan|Aspect=Perf|Case=Acc|Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass']
        #по инструкции должно быть прил
        ['голодающими', 'PRTF,impf,intr,pres,actv,plur,ablt', 'VERB Animacy=Anim|Aspect=Imp|Case=Ins|Number=Plur|Tense=Pres|VerbForm=Part|Voice=Act']
        ['неприкосновенны', 'ADJS,plur', 'ADJ Animacy=Inan|Case=Nom|Number=Plur|Variant=Brev'],
        #у нас неправильно
        ['1', 'NUMB', 'ADJ Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing'], #остался 1 км.
        ['выше', 'COMP', 'ADJ Degree=Cmp'], #он выше меня vs подняться выше
        ['выше', 'COMP', 'ADV Degree=Cmp'],

        #у нас у числ одуш только в вин падеже, у них непонятно когда
        ['двум', 'NUMR,femn,datv', 'NUM Animacy=Inan|Case=Dat|Gender=Fem'],
        ['пяти', 'NUMR,loct', 'NUM Case=Loc'],
        ['три', 'NUMR,inan,accs', 'NUM Animacy=Inan|Case=Acc'],

        ['громко', 'ADVB', 'ADV _'],

        ['.', 'PNCT', 'PUNCT _'],
    ]

    @pytest.mark.parametrize(("word", "internal", "ud14"), TEST_DATA)
    def test_from_internal(self, word, internal, ud14):
        converted = converters.convert(internal, 'opencorpora-int', 'ud14')
        assert converted == ud14


def _remove_unsupported(ud_tag):
    pos, info = ud.split_tag(ud_tag)
#    info.difference_update(
#        set(['од', 'но', '2', 'имя', 'фам', 'лок', 'кач', 'разг'])
#    )
#    if pos == 'ДЕЕПРИЧАСТИЕ':
#    info.discard('дст')
#
#    if pos == 'С':
#        if 'аббр' in info:
#            info.difference_update(set(aot.CASES.keys()))

    return ud.join_tag(pos, info)


#class TestAotConversion(object):
#
#    @pytest.mark.parametrize(("word", "open_tag", "ud_tag"), PARSE_RESULTS)
#    def test_to_aot(self, word, open_tag, ud_tag):
#        converted = converters.convert(open_tag, 'opencorpora-int', 'ud')
#        assert ud.split_tag(_remove_unsupported(converted)) == ud.split_tag(_remove_unsupported(ud_tag))
