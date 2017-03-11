# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import pytest

from russian_tagsets import converters, ud
#from .opencorpora_aot_data import PARSE_RESULTS

class TestInternalConversion(object):
    TEST_DATA = [
        #Noun, Verb, ADJF, ADVB, PRTF, PRTS, NUMB, COMP, NPRO, GRND, CONJ, PRCL, PREP
        #GNdr, Pltm, Sgtm, Ms-f, Inmx, Name, Surn, Patr, Fixd
        #inan, anim - Noun, anim, inan - ADJF/PRTF
        #femn, masc, neut; sing plur; nomn, gent, datv, accs, ablt, loct; voct, loc2, gen2, gen1
        #Anum, Qual, Apro
        #perf, impr; intr, tran; pres, past, futr; indc, impr; actv pssv; 1per, 2per, 3per; excl, incl
        ['власть', 'NOUN,inan,femn sing,nomn', 'NOUN Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing'],
        # в UD род у Pltm проставлен, но в рамках соревнования не просим его определять (то же про мн.ч прил)
        ['суток', 'NOUN,inan,GNdr,Pltm,plur,gent', 'NOUN Animacy=Inan|Case=Gen|Number=Ptan'],
        ['лесу', 'NOUN,inan,masc,sing,loc2', 'NOUN Animacy=Inan|Case=Loc|Gender=Masc|Number=Sing'],
        ['боку', 'NOUN,inan,masc,sing,gen2', 'NOUN Animacy=Inan|Case=Gen|Gender=Masc|Number=Sing'],
        ['бока', 'NOUN,inan,masc,sing,gen1', 'NOUN Animacy=Inan|Case=Gen|Gender=Masc|Number=Sing'],
        ['ань', 'NOUN,anim,femn,sing,voct', 'NOUN Animacy=Anim|Case=Nom|Gender=Fem|Number=Sing'],
        #МИКРОБ!!! у нас выбираем одуш у леммы, а у формы вин ставим другую одуш - у них видимо две леммы
        ['персонаж', 'NOUN,anim,masc,Inmx,sing,inan,accs', 'NOUN Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing'],
        ['персонажа', 'NOUN,anim,masc,Inmx,sing,accs', 'NOUN Animacy=Anim|Case=Acc|Gender=Masc|Number=Sing'],
        ['персонаж', 'NOUN,anim,masc,Inmx,sing,nomn', 'NOUN Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing'],
        #['персонаж', 'NOUN,anim,masc,Inmx,sing,nomn', 'NOUN Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing'],
        ['ивана', 'NOUN,anim,masc,Name sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Masc|Number=Sing'],
        #непоянтно, какое число должно быть у них у фамилий sing или Coll
        ['иванова', 'NOUN,anim,masc,Sgtm,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Masc|Number=Sing'],
        ['гиппиус', 'NOUN,anim,femn,Sgtm,Fixd,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Fem|Number=Sing'],
        #похоже, что мн у фамилий только в мр (нужно проверить)
        #['ивановы', 'NOUN,anim,GNdr,Ms-f,Pltm,Surn,plur,nomn', 'PROPN Animacy=Anim|Case=Nom|Gender=Masc|Number=Plur'],
        ['ивановичем', 'NOUN,anim,masc,Patr,sing,ablt', 'PROPN Animacy=Anim|Case=Ins|Gender=Masc|Number=Sing'],
        #если не изменяемая фам по обоим родам, то у нам одна лемма Sgtm, у них видимо две леммы (проверить)
        #странно, что у нам только ед ч
        #['винчи', 'NOUN,anim,GNdr,Ms-f,Sgtm,Fixd,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Masc|Number=Sing'],
        #['винчи', 'NOUN,anim,GNdr,Ms-f,Sgtm,Fixd,Surn,sing,gent', 'PROPN Animacy=Anim|Case=Gen|Gender=Fem|Number=Sing'],
        ['москвы', 'NOUN,inan,femn,Sgtm,Geox,sing,gent', 'PROPN Animacy=Inan|Case=Gen|Gender=Fem|Number=Sing'],
        ['оон', 'NOUN,inan,femn,Sgtm,Fixd,Abbr,Orgn,sing,gent', 'PROPN Animacy=Inan|Case=Gen|Gender=Fem|Number=Sing'],
        #['а', 'NOUN,anim,GNdr,Ms-f,Sgtm,Fixd,Abbr,Name,Init,sing,nomn', 'PROPN Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing'], # инициал

        ['я', 'NPRO,1per,sing,nomn', 'PRON Case=Nom|Number=Sing|Person=1'],
        ['вами', 'NPRO,2per,plur,ablt', 'PRON Case=Ins|Number=Plur|Person=2'],


        ['поменяться', 'INFN,perf,intr', 'VERB Aspect=Perf|VerbForm=Inf'],
        ['было', 'VERB,impf,intr neut,sing,past,indc,Auxt', 'AUX Aspect=Imp|Gender=Neut|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin'], #"было сделано" (вспм) vs. "было уязвимо" (глагол); в OpenCorpora помета на токене
        ['было', 'VERB,impf,intr neut,sing,past,indc', 'VERB Aspect=Imp|Gender=Neut|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin'], #"было дано" (вспм) vs. "в классе было 20 человек" (глагол)
        ['смогут', 'VERB,perf,intr,plur,3per,futr,indc', 'VERB Aspect=Perf|Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin'],
        #['подойди', 'VERB,perf,intr,sing,impr,excl', 'VERB Aspect=Perf|Mood=Imp|Number=Sing|Person=2|VerbForm=Fin|Voice=Act'],
        #['пройдемте', 'VERB,perf,intr,plur,impr,incl', 'VERB Aspect=Imp|Mood=Imp|Number=Plur|Person=1|VerbForm=Fin|Voice=Act'],
        #['отражая', 'GRND,impf,tran,pres', 'VERB Aspect=Imp|Tense=Pres|VerbForm=Trans|Voice=Act'],
        #['выстрадав', 'GRND,perf,tran,past', 'VERB Aspect=Perf|Tense=Past|VerbForm=Trans|Voice=Act'],
        ['голодающими', 'PRTF,impf,intr,pres,actv,plur,ablt', 'ADJ Aspect=Imp|Case=Ins|Number=Plur|Tense=Pres|VerbForm=Part|Voice=Act'],
        #по инструкции должно быть прил
        ['сделанный', 'PRTF,perf,tran,past,pssv,inan,masc,sing,accs', 'ADJ Animacy=Inan|Aspect=Perf|Case=Acc|Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass'],
        ['написана', 'PRTS,perf,past,pssv,femn,sing', 'ADJ Aspect=Perf|Gender=Fem|Number=Sing|Tense=Past|Variant=Brev|VerbForm=Part|Voice=Pass'],

        ['первом', 'ADJF,Anum,masc,sing,loct', 'ADJ Case=Loc|Gender=Masc|Number=Sing'],
        ['первого', 'ADJF,Anum,anim,masc,sing,accs', 'ADJ Animacy=Anim|Case=Acc|Gender=Masc|Number=Sing'],
        ['большая', 'ADJF,Qual,femn,sing,nomn', 'ADJ Case=Nom|Gender=Fem|Number=Sing'],
        ['студенческих', 'ADJF,plur,loct', 'ADJ Case=Loc|Number=Plur'],
        ['лучшим', 'ADJF,Supr,Qual,masc,sing,ablt', 'ADJ Case=Ins|Degree=Sup|Gender=Masc|Number=Sing'],
        #по инструкции должно быть прил
        ['неприкосновенны', 'ADJS,plur', 'ADJ Number=Plur|Variant=Brev'],
        ['бела', 'ADJS,sing,masc,gent', 'ADJ Case=Gen|Gender=Masc|Number=Sing|Variant=Brev'],
        #у нас неправильно
        #['1', 'NUMB', 'ADJ Animacy=Inan|Case=Nom|Gender=Neut|Number=Sing'], # 1 декабря
        #['XX', 'ROMN', 'ADJ Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing'], # XX век
        #['выше', 'COMP', 'ADJ Degree=Cmp'], # он выше меня vs подняться выше
        #['выше', 'COMP', 'ADV Degree=Cmp'], # есть идея создать пул и ставить помету на токен
        ['мой', 'ADJF,Apro,sing,masc,nomn', 'DET Case=Nom|Gender=Masc|Number=Sing'],

        #['2', 'NUMB', 'NUM Case=Nom|Gender=Masc'], # два мальчика
        ['2', 'NUMB,intg', 'NUM _'],  # pymorphy2 result
        ['двум', 'NUMR,femn,datv', 'NUM Case=Dat|Gender=Fem'],
        ['пяти', 'NUMR,loct', 'NUM Case=Loc'],
        ['три', 'NUMR,inan,accs', 'NUM Animacy=Inan|Case=Acc'],

        ['громко', 'ADVB', 'ADV _'],

        ['ах', 'INTJ', 'INTJ _'],
        ['у', 'PREP', 'ADP _'],
        ['и', 'CONJ', 'CONJ _'],
        #['если', 'CONJ', 'SCONJ'],  # нам нужны списки
        ['же', 'PRCL', 'PART _'],

        ['.', 'PNCT', 'PUNCT _'],
        #['%', 'PNCT', 'SYM _'],
    ]

    @pytest.mark.parametrize(("word", "internal", "ud14"), TEST_DATA)
    def test_from_internal(self, word, internal, ud14):
        converted = converters.convert(internal, 'opencorpora-int', 'ud14')
        assert converted == ud14
