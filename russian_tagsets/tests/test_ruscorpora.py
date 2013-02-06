# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from russian_tagsets import ruscorpora

TEST_DATA = [
    # 0
    ("СССР", "S,m,inan,0=sg,gen", "NOUN,inan,masc,Sgtm,Fixd,Abbr,Geox sing,gent"),
    # ("Пеано", "S,famn,m,anim,0=sg,ins", "NOUN,anim,masc,Sgtm,Fixd,Surn sing,ablt"),
    # ("Кинзмараули", "S,0=pl,nom", "NOUN,inan,neut,Sgtm,Fixd sing,nomn"),

    # 1p
    ("мы", "S-PRO,pl,1p=nom", "NPRO,1per plur,nomn"),
    ("будем", "V,ipf,intr,act=pl,fut,1p,indic", "VERB,impf,intr plur,1per,futr,indc"),
    ("мне", "S-PRO,sg,1p=dat", "NPRO,1per sing,datv"),
    ("я", "S-PRO,sg,1p=nom", "NPRO,1per sing,nomn"),
    ("допустим", "V,pf,tran=pl,act,fut,1p,indic", "VERB,perf,tran plur,1per,futr,indc"),
    ("нас", "S-PRO,pl,1p=gen", "NPRO,1per plur,gent"),
    ("люблю", "V,ipf,tran=sg,act,praes,1p,indic", "VERB,impf,tran sing,1per,pres,indc"),

    # 2p
    ("Кормите", "V,ipf,tran=pl,act,praes,2p,indic", "VERB,impf,tran plur,2per,pres,indc"),
    ("Давайте", "V,ipf,tran=pl,2p,act,imper", "VERB,impf,tran plur,impr,excl"),
    ("Ты", "S-PRO,sg,2p=nom", "NPRO,2per sing,nomn"),
    ("Вы", "S-PRO,pl,2p=nom", "NPRO,2per plur,nomn"),
    ("любишь", "V,ipf,tran=sg,act,praes,2p,indic", "VERB,impf,tran sing,2per,pres,indc"),
    ("Понимаете", "V,ipf,tran=pl,act,praes,2p,indic", "VERB,impf,tran plur,2per,pres,indc"),
    ("ноешь", "V,ipf,intr,act=sg,praes,2p,indic", "VERB,impf,intr sing,2per,pres,indc"),
    ("помните", "V,ipf,tran=pl,act,praes,2p,indic", "VERB,impf,tran plur,2per,pres,indc"),
    ("можете", "V,ipf,intr,act=pl,praes,2p,indic", "VERB,impf,intr plur,2per,pres,indc"),
    ("Тебя", "S-PRO,sg,2p=gen", "NPRO,2per sing,gent"),
    ("найдёте", "V,pf,tran=pl,act,fut,2p,indic", "VERB,perf,tran plur,2per,futr,indc"),
    ("Выразите", "V,pf,tran=pl,act,2p,imper", "VERB,perf,tran plur,impr,excl"),

    # 3p
    ("растёт", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("Оказывается", "V,ipf,intr,med=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("ней", "S-PRO,f,sg,3p=dat", "NPRO,femn,3per sing,datv,Af-p"),
    ("них", "S-PRO,pl,3p=acc", "NPRO,3per plur,accs,Af-p"),
    ("она", "S-PRO,f,sg,3p=nom", "NPRO,femn,3per sing,nomn"),
    ("ему", "S-PRO,m,sg,3p=dat", "NPRO,masc,3per sing,datv"),
    ("Будут", "V,ipf,intr,act=pl,fut,3p,indic", "VERB,impf,intr plur,3per,futr,indc"),
    ("осуществляет", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("рассматриваются", "V,ipf,intr,med=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("являются", "V,ipf,intr,med=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("чистят", "V,ipf,tran=pl,act,praes,3p,indic", "VERB,impf,tran plur,3per,pres,indc"),
    ("попадает", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("его", "S-PRO,m,sg,3p=acc", "NPRO,masc,3per sing,accs"),
    ("их", "S-PRO,pl,3p=acc", "NPRO,3per plur,accs"),
    ("Они", "S-PRO,pl,3p=nom", "NPRO,3per plur,nomn"),

    # A
    ("дикая", "A=f,sg,nom,plen", "ADJF,Qual femn,sing,nomn"),
    ("собачья", "A=f,sg,nom,plen", "ADJF,Poss femn,sing,nomn"),
    ("лавровый", "A=m,sg,nom,plen", "ADJF masc,sing,nomn"),
    ("плоская", "A=f,sg,nom,plen", "ADJF,Qual femn,sing,nomn"),
    ("мёртвое", "A=n,sg,nom,plen", "ADJF,Qual neut,sing,nomn"),
    ("стартовой", "A=f,sg,gen,plen", "ADJF,Qual femn,sing,gent"),
    ("общих", "A=pl,loc,plen", "ADJF plur,loct"),
    ("труднее", "A=comp", "COMP,Qual"),
    # ("Вронского", "A=sg,m,acc,anim,plen", "NOUN,anim,masc,Sgtm,Surn sing,accs"),
    # ("политическое", "A=n,sg,acc,inan,plen", "ADJF neut,sing,accs"),
    ("страховых", "A=pl,gen,plen", "ADJF plur,gent"),
    ("ходячей", "A=f,sg,gen,plen", "ADJF femn,sing,gent"),
    ("Постоянное", "A=n,sg,nom,plen", "ADJF,Qual neut,sing,nomn"),

    # A-PRO
    # ("его", "A-PRO", "ADJF,Fixd,Apro masc,sing,nomn | ADJF,Fixd,Apro masc,sing,gent | ADJF,Fixd,Apro masc,sing,datv | ADJF,Fixd,Apro masc,sing,accs | ADJF,Fixd,Apro masc,sing,ablt | ADJF,Fixd,Apro masc,sing,loct | ADJF,Fixd,Apro femn,sing,nomn | ADJF,Fixd,Apro femn,sing,gent | ADJF,Fixd,Apro femn,sing,datv | ADJF,Fixd,Apro femn,sing,accs | ADJF,Fixd,Apro femn,sing,ablt | ADJF,Fixd,Apro femn,sing,loct | ADJF,Fixd,Apro neut,sing,nomn | ADJF,Fixd,Apro neut,sing,gent | ADJF,Fixd,Apro neut,sing,datv | ADJF,Fixd,Apro neut,sing,accs | ADJF,Fixd,Apro neut,sing,ablt | ADJF,Fixd,Apro neut,sing,loct | ADJF,Fixd,Apro plur,nomn | ADJF,Fixd,Apro plur,gent | ADJF,Fixd,Apro plur,datv | ADJF,Fixd,Apro plur,accs | ADJF,Fixd,Apro plur,ablt | ADJF,Fixd,Apro plur,loct | NPRO,masc,3per sing,gent | NPRO,masc,3per sing,accs | NPRO,neut,3per sing,gent | NPRO,neut,3per sing,accs"),
    ("нашего", "A-PRO=m,sg,gen", "ADJF,Apro masc,sing,gent"),
    ("все", "A-PRO=pl,nom", "ADJF,Apro plur,nomn"),
    ("которыми", "A-PRO=pl,ins", "ADJF,Apro plur,ablt"),
    ("своих", "A-PRO=pl,acc,anim", "ADJF,Apro anim,plur,accs"),
    ("всем", "A-PRO=m,sg,ins", "ADJF,Apro masc,sing,ablt"),
    ("наш", "A-PRO=m,sg,acc,inan", "ADJF,Apro inan,masc,sing,accs"),
    ("которой", "A-PRO=f,sg,loc", "ADJF,Apro femn,sing,loct"),
    ("другим", "A-PRO=pl,dat", "ADJF,Apro plur,datv"),
    ("которую", "A-PRO=f,sg,acc", "ADJF,Apro femn,sing,accs"),
    ("своего", "A-PRO=n,sg,gen", "ADJF,Apro neut,sing,gent"),
    ("многих", "A-PRO=pl,loc", "ADJF,Apro plur,loct"),
    ("все", "A-PRO=pl,acc,inan", "ADJF,Apro inan,plur,accs"),
    ("которому", "A-PRO=m,sg,dat", "ADJF,Apro masc,sing,datv"),
    # ("всё", "A-PRO=n,sg,acc,inan", "ADJF,Apro neut,sing,accs"),

    # ADV
    ("Изредка", "ADV", "ADVB"),
    ("Наверху", "ADV", "ADVB"),
    ("возможно", "ADV", "ADVB,Prdx"),
    ("Наиболее", "ADV", "ADVB"),
    # ("самозабвенно", "ADV", "ADJS,Qual neut,sing"),

    # ADV-PRO
    # ("так", "ADV-PRO", "ADVB,Dmns"),
    # ("здесь", "ADV-PRO", "ADVB,Prdx"),
    # ("всегда", "ADV-PRO", "ADVB"),
    ("где", "ADV-PRO", "ADVB,Ques"),
    # ("теперь", "ADV-PRO", "ADVB"),
    # ("всегда", "ADV-PRO", "ADVB"),
    # ("никогда", "ADV-PRO", "ADVB"),
    # ("потом", "ADV-PRO", "ADVB"),
    # ("Поэтому", "ADV-PRO", "ADVB"),
    # ("Теперь", "ADV-PRO", "ADVB"),
    ("как", "ADV-PRO", "ADVB,Ques"),

    # ANUM
    # ("одного", "ANUM=m,gen", "ADJF,Apro masc,sing,gent"),
    ("второй", "ANUM=m,sg,nom", "ADJF,Anum masc,sing,nomn"),
    # ("III", "ANUM=ciph", ""),
    # ("одна", "ANUM=f,nom", "ADJF,Apro femn,sing,nomn"),
    ("первый", "ANUM=m,sg,nom", "ADJF,Anum masc,sing,nomn"),
    ("десятые", "ANUM=pl,nom", "ADJF,Anum plur,nomn"),
    ("третьей", "ANUM=f,sg,ins", "ADJF,Subx,Anum femn,sing,ablt"),
    ("пятый", "ANUM=m,sg,nom", "ADJF,Anum masc,sing,nomn"),

    # CONJ
    ("и", "CONJ", "CONJ"),

    # INIT
    # ("Д", "INIT=abbr", "NOUN,inan,masc sing,accs | ADJS masc,sing | ADVB"),

    # INTJ
    ("О", "INTJ", "INTJ"),
    # ("О-о-о", "INTJ=distort", ""),
    # ("Эхх", "INTJ=distort", ""),
    # ("здравствуй", "INTJ", "VERB,impf,intr sing,impr,excl"),
    # ("Господи", "INTJ", "NOUN,anim,masc,Sgtm sing,voct"),

    # NUM
    ("сорока", "NUM=loc", "NUMR loct"),
    ("три", "NUM=acc", "NUMR inan,accs"),
    # ("меньше", "NUM=comp", "COMP,Qual"),
    ("трех", "NUM=gen", "NUMR gent"),
    ("Десять", "NUM=nom", "NUMR nomn"),

    # PARENTH
    ("По-видимому", "PARENTH", "CONJ,Prnt"),
    ("Говорят", "PARENTH", "CONJ,Prnt"),
    ("видно", "PARENTH", "CONJ,Prnt"),
    ("вообще", "PARENTH", "CONJ,Prnt"),
    ("Во-вторых", "PARENTH", "CONJ,Prnt"),
    #("Короче", "PARENTH", "NOUN,inan,femn,Sgtm,Geox sing,datv | NOUN,inan,femn,Sgtm,Geox sing,loct | COMP,Qual"),
    ("Словом", "PARENTH", "CONJ,Prnt"),
    #("мол", "PARENTH", "PRCL | NOUN,inan,masc sing,nomn | NOUN,inan,masc sing,accs"),

    # PART
    ("же", "PART", "PRCL"),
    ("ли", "PART", "PRCL"),
    ("не", "PART", "PRCL"),
    ("Ну", "PART", "PRCL"),
    ("вроде", "PART", "PRCL"),
    ("всё-таки", "PART", "PRCL"),
    ("Да", "PART", "PRCL"),
    ("даже", "PART", "PRCL"),

    # PNCT

    # PR
    ("с", "PR", "PREP"),
    ("в", "PR", "PREP"),
    ("со", "PR", "PREP Vpre"),

    # PRAEDIC
    # ("негусто", "PRAEDIC", "ADJS,Qual neut,sing"),
    ("можно", "PRAEDIC", "PRED,pres"),
    ("некуда", "PRAEDIC", "PRED,pres"),
    ("Нужно", "PRAEDIC", "PRED,pres"),
    ("охота", "PRAEDIC", "PRED,pres"),
    # ("нет", "PRAEDIC", "INTJ | PRCL"),
    # ("невозможно", "PRAEDIC", "ADVB,Prdx"),
    # ("безопасно", "PRAEDIC", "ADVB | ADJS,Qual neut,sing"),
    # ("легче", "PRAEDIC=comp", "COMP,Qual"),

    # PRAEDIC-PRO
    # ("нечего", "PRAEDIC-PRO,sg=gen", "NPRO sing,gent"),
    # ("нечем", "PRAEDIC-PRO,sg=ins", "NPRO sing,ablt"),
    # ("некому", "PRAEDIC-PRO,sg=dat", "NPRO sing,datv"),

    # S
    ("шиповник", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("роза", "S,f,inan=sg,nom", "NOUN,inan,femn sing,nomn"),
    ("связи", "S,f,inan=sg,loc2", "NOUN,inan,femn sing,loc2"),
    ("недоработками", "S,f,inan=pl,ins", "NOUN,inan,femn plur,ablt"),
    ("Кирилла", "S,persn,m,anim=sg,gen", "NOUN,anim,masc,Name sing,gent"),
    ("страхования", "S,n,inan=sg,gen", "NOUN,inan,neut sing,gent"),
    #("данным", "S,pl=dat", "NOUN,inan,GNdr,Pltm plur,datv"),
    ("хаосе", "S,m,inan=sg,loc", "NOUN,inan,masc sing,loct"),
    ("целей", "S,f,inan=pl,gen", "NOUN,inan,femn plur,gent"),

    # S-PRO
    #("всего", "S-PRO,n,sg=gen", "ADVB | PRCL | ADJF,Apro masc,sing,gent | ADJF,Apro anim,masc,sing,accs | ADJF,Apro neut,sing,gent"),
    ("это", "S-PRO,n,sg=nom", "NPRO,neut sing,nomn"),
    ("ней", "S-PRO,f,sg,3p=dat", "NPRO,femn,3per sing,datv,Af-p"),
    ("них", "S-PRO,pl,3p=acc", "NPRO,3per plur,accs,Af-p"),
    ("этого", "S-PRO,n,sg=gen", "NPRO,neut sing,gent"),

    ("него", "S-PRO,m,sg,3p=gen", "NPRO,masc,3per sing,gent,Af-p"),
    ("Мне", "S-PRO,sg,1p=dat", "NPRO,1per sing,datv"),
    ("них", "S-PRO,pl,3p=gen", "NPRO,3per plur,gent,Af-p"),
    # ("себе", "S-PRO=dat", "NPRO sing,datv"),
    # ("тем", "S-PRO,n,sg=ins", "CONJ | NOUN,inan,femn plur,gent | ADJF,Apro masc,sing,ablt | ADJF,Apro neut,sing,ablt | ADJF,Apro plur,datv | NOUN,inan,femn plur,gent"),
    ("их", "S-PRO,pl,3p=acc", "NPRO,3per plur,accs"),
    ("я", "S-PRO,sg,1p=nom", "NPRO,1per sing,nomn"),
    ("Он", "S-PRO,m,sg,3p=nom", "NPRO,masc,3per sing,nomn"),
    ("этому", "S-PRO,n,sg=dat", "NPRO,neut sing,datv"),

    # V
    ("растёт", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("снят", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("Оказывается", "V,ipf,intr,med=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("попал", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    # ("карающий", "V,ipf,tran=partcp,m,sg,nom,act,praes", "PRTF,impf,tran,pres,actv masc,sing,nomn"),
    # ("сдержался", "V,med,pf=praet,sg,m,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("Подбирали", "V,ipf,tran=pl,act,praet,indic", "VERB,impf,tran plur,past,indc"),
    ("Веришь", "V,ipf,intr,act=sg,praes,2p,indic", "VERB,impf,intr sing,2per,pres,indc"),
    ("может", "V,intr,ipf=praes,sg,3p,act,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("производят", "V,ipf,tran=pl,act,praes,3p,indic", "VERB,impf,tran plur,3per,pres,indc"),
    ("разошлись", "V,pf,intr,med=pl,praet,indic", "VERB,perf,intr plur,past,indc"),
    ("набрать", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("отбросил", "V,pf,tran=m,sg,act,praet,indic", "VERB,perf,tran masc,sing,past,indc"),
    ("упомянут", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("поддерживает", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),

    # abbr
    #("тыс", "S,f,inan=sg,gen=abbr", ""),
    #("мес", "S,m,inan=pl,gen=abbr", "NOUN,inan,masc sing,nomn"),
    #("руб", "S,m,inan=pl,gen=abbr", "NOUN,inan,masc sing,nomn | ADJS,Qual masc,sing"),
    #("А", "INIT=abbr", "CONJ | INTJ | PRCL"),
    #("млн", "S,m,inan=pl,gen=abbr", "NOUN,inan,femn plur,gent"),
    #("мм", "S,m,inan=pl,gen=abbr", "INTJ"),
    #("млрд", "S,m,inan=pl,gen=abbr", "NOUN,anim,masc,Name sing,nomn | ADJS masc,sing"),
    #("математич", "A=f,sg,loc,plen=abbr", "NOUN,anim,masc sing,nomn"),

    # acc
    ("Закон", "S,m,inan=sg,acc", "NOUN,inan,masc sing,accs"),
    ("имущество", "S,n,inan=sg,acc", "NOUN,inan,neut sing,accs"),
    ("тарелку", "S,f,inan=sg,acc", "NOUN,inan,femn sing,accs"),
    ("голубей", "S,m,anim=pl,acc", "NOUN,anim,masc plur,accs"),
    ("школу", "S,f,inan=sg,acc", "NOUN,inan,femn sing,accs"),
    ("московские", "A=pl,acc,inan,plen", "ADJF inan,plur,accs"),
    ("бюджет", "S,m,inan=sg,acc", "NOUN,inan,masc sing,accs"),
    ("систему", "S,f,inan=sg,acc", "NOUN,inan,femn sing,accs"),
    # ("всё", "S-PRO,n,sg=acc", "ADJF,Apro neut,sing,accs"),
    ("право", "S,n,inan=sg,acc", "NOUN,inan,neut sing,accs"),
    ("меня", "S-PRO,sg,1p=acc", "NPRO,1per sing,accs"),
    ("выполнение", "S,n,inan=sg,acc", "NOUN,inan,neut sing,accs"),
    ("нормативную", "A=f,sg,acc,plen", "ADJF femn,sing,accs"),
    ("отношения", "S,n,inan=pl,acc", "NOUN,inan,neut plur,accs"),
    ("расцвет", "S,m,inan=sg,acc", "NOUN,inan,masc sing,accs"),

    # acc2
    # ("гости", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn | VERB,impf,intr sing,impr,excl"),
    # ("понятые", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn"),
    # ("академики", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn"),
    # ("губернаторы", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn"),
    # ("почтальоны", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn"),
    # ("нижегородские", "A=pl,acc2,anim,plen", "ADJF plur,nomn | ADJF inan,plur,accs"),
    # ("сотоварищи", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn"),
    # ("президенты", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn"),
    # ("академики", "S,m,anim=pl,acc2", "NOUN,anim,masc plur,nomn"),

    # act
    ("растёт", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("попал", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("Кормите", "V,ipf,tran=pl,act,praes,2p,indic", "VERB,impf,tran plur,2per,pres,indc"),
    ("идти", "V,ipf,intr,act=inf", "INFN,impf,intr"),
    ("создать", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("обсудить", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("вырос", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("будут", "V,ipf,intr,act=pl,fut,3p,indic", "VERB,impf,intr plur,3per,futr,indc"),
    ("планирует", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("может", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("существуют", "V,ipf,intr,act=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("формируют", "V,ipf,tran=pl,act,praes,3p,indic", "VERB,impf,tran plur,3per,pres,indc"),
    ("принять", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("скандалят", "V,ipf,intr,act=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),

    # adnum
    # ("часа", "S,m,inan=sg,adnum", "NOUN,inan,masc sing,gen1"),

    # anim
    ("уличных", "A=pl,acc,anim,plen", "ADJF,Qual anim,plur,accs"),
    # ("Я", "S-PRO,sg,anim,1p=nom", "NPRO,1per sing,nomn"),
    ("разбойник", "S,m,anim=sg,nom", "NOUN,anim,masc sing,nomn"),
    ("Островской", "S,famn,f,anim=sg,gen", "NOUN,anim,femn,Sgtm,Surn sing,gent"),
    ("ефрейтор", "S,m,anim=sg,nom", "NOUN,anim,masc sing,nomn"),
    ("Мама", "S,f,anim=sg,nom", "NOUN,anim,femn sing,nomn"),
    ("животным", "S,n,anim=pl,dat", "NOUN,anim,neut plur,datv"),
    ("Марина", "S,persn,f,anim=sg,nom", "NOUN,anim,femn,Name sing,nomn"),
    ("Андреевна", "S,patrn,f,anim=sg,nom", "NOUN,anim,femn,Patr sing,nomn"),
    ("Лорой", "S,persn,f,anim=sg,ins", "NOUN,anim,femn,Name sing,ablt"),
    ("руководитель", "S,m,anim=sg,nom", "NOUN,anim,masc sing,nomn"),

    # anom
    ("Божиих", "A=pl,loc,plen=anom", "ADJF plur,loct,Litr"),
    # ("слышут", "V,ipf,tran=pl,act,praes,3p,indic=anom", "VERB,impf,tran plur,3per,pres,indc,Infr"),
    # ("товарищи", "S,m,anim=pl,ins=anom", "NOUN,anim,masc plur,nomn"),
    # ("скакает", "V,ipf,intr,act=sg,praes,3p,indic=anom", "VERB,impf,intr sing,3per,pres,indc"),
    # ("публицистическою", "A=f,sg,ins,plen=anom", "ADJF femn,sing,ablt,V-oy"),

    # brev
    ("представлена", "V,pf,tran=partcp,f,sg,brev,pass,praet", "PRTS,perf,past,pssv femn,sing"),
    ("даны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("связано", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("должен", "A,brev=m,sg", "ADJS masc,sing"),
    # ("раздавлен", "V,pf=partcp,praet,pass,brev,sg,m", "PRTS,perf,past,pssv masc,sing"),
    ("сведено", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("высок", "A=m,sg,brev", "ADJS,Qual masc,sing"),
    ("изображены", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("горизонтальна", "A=f,sg,brev", "ADJS,Qual femn,sing"),
    ("обломан", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("снят", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("сопричастны", "A=pl,brev", "ADJS,Qual plur"),
    ("подписаны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("сделано", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("закончен", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),

    # ciph
    # ("24", "NUM=ciph", ""),
    # ("54", "NUM=ciph", ""),
    # ("2", "NUM=ciph", ""),
    # ("1300", "NUM=ciph", ""),
    # ("2", "NUM=ciph", ""),

    # comp
    # ("чаще", "ADV=comp", "COMP,Qual"),
    ("труднее", "A=comp", "COMP,Qual"),
    ("малодобычливее", "A=comp", "COMP,Qual"),
    ("больше", "A=comp", "COMP,Qual"),
    # ("привычнее", "PRAEDIC=comp", "COMP,Qual"),
    # ("точнее", "ADV=comp", "COMP,Qual"),
    # ("меньше", "NUM=comp", "COMP,Qual"),
    ("противоречивее", "A=comp", "COMP,Qual"),
    ("лучше", "A=comp", "COMP,Qual"),
    # ("более", "NUM=comp", "ADVB"),
    # ("больше", "NUM=comp", "COMP,Qual"),
    # ("скорее", "ADV=comp", "COMP,Qual"),
    # ("Прямее", "ADV=comp", "COMP,Qual"),
    # ("реже", "ADV=comp", "COMP,Qual"),
    ("выше", "A=comp", "COMP,Qual"),

    # comp2
    # ("подороже", "ADV=comp2", "COMP,Qual Cmp2"),
    # ("поменьше", "NUM=comp2", "COMP,Qual Cmp2"),
    # ("поскорее", "ADV=comp2", "COMP,Qual Cmp2"),
    ("покрупнее", "A=comp2", "COMP,Qual Cmp2"),
    ("помоложе", "A=comp2", "COMP,Qual Cmp2"),
    ("позакавыристей", "A=comp2", "COMP,Qual Cmp2,V-ej"),
    # ("поподробней", "ADV=comp2", "COMP Cmp2,V-ej"),
    ("поспокойнее", "A=comp2", "COMP,Qual Cmp2"),
    ("получше", "A=comp2", "COMP,Qual Cmp2"),
    ("помоложе", "A=comp2", "COMP,Qual Cmp2"),
    ("поменьше", "A=comp2", "COMP,Qual Cmp2"),
    # ("поменьше", "NUM=comp2", "COMP,Qual Cmp2"),
    # ("попозже", "ADV=comp2", "COMP,Qual Cmp2"),

    # dat
    ("твёрдости", "S,f,inan=sg,dat", "NOUN,inan,femn sing,datv"),
    ("силе", "S,f,inan=sg,dat", "NOUN,inan,femn sing,datv"),
    ("двоюродному", "A=m,sg,dat,plen", "ADJF,Qual masc,sing,datv"),
    ("уголовным", "A=pl,dat,plen", "ADJF,Qual plur,datv"),
    ("чтению", "S,n,inan=sg,dat", "NOUN,inan,neut sing,datv"),
    ("всей", "A-PRO=f,sg,dat", "ADJF,Apro femn,sing,datv"),
    ("правительству", "S,n,inan=sg,dat", "NOUN,inan,neut sing,datv"),
    ("уровню", "S,m,inan=sg,dat", "NOUN,inan,masc sing,datv"),
    ("направлениям", "S,n,inan=pl,dat", "NOUN,inan,neut plur,datv"),
    ("Платону", "S,persn,m,anim=sg,dat", "NOUN,anim,masc,Name sing,datv"),

    # distort
    ("недоуменье", "S,n,inan=sg,acc=distort", "NOUN,inan,neut sing,accs,V-be"),

    # f
    ("дикая", "A=f,sg,nom,plen", "ADJF,Qual femn,sing,nomn"),
    ("роза", "S,f,inan=sg,nom", "NOUN,inan,femn sing,nomn"),
    ("собачья", "A=f,sg,nom,plen", "ADJF,Poss femn,sing,nomn"),
    ("связи", "S,f,inan=sg,loc2", "NOUN,inan,femn sing,loc2"),
    ("пассажирка", "S,f,anim=sg,nom", "NOUN,anim,femn sing,nomn"),
    ("ней", "S-PRO,f,sg,3p=ins", "NPRO,femn,3per sing,ablt,Af-p"),
    ("никакой", "A-PRO=f,sg,gen", "ADJF,Apro femn,sing,gent"),
    ("включена", "V,pf,tran=partcp,f,sg,brev,pass,praet", "PRTS,perf,past,pssv femn,sing"),
    ("стены", "S,f,inan=sg,gen", "NOUN,inan,femn sing,gent"),
    ("никакая", "A-PRO=f,sg,nom", "ADJF,Apro femn,sing,nomn"),
    ("мрачной", "A=f,sg,ins,plen", "ADJF,Qual femn,sing,ablt"),
    ("другой", "A-PRO=f,sg,gen", "ADJF,Apro femn,sing,gent"),
    ("недостающей", "V,ipf,intr,act=partcp,f,sg,gen,praes,plen", "PRTF,impf,intr,pres,actv femn,sing,gent"),
    ("Суть", "S,f,inan=sg,nom", "NOUN,inan,femn sing,nomn"),

    # famn
    ("Путин", "S,famn,m,anim=sg,nom", "NOUN,anim,masc,Sgtm,Surn sing,nomn"),
    ("Платонова", "S,famn,m,anim=sg,acc", "NOUN,anim,masc,Sgtm,Surn sing,accs"),
    ("Хоукинга", "S,famn,m,anim=sg,gen", "NOUN,anim,masc,Sgtm,Surn sing,gent"),
    ("Иванова", "S,famn,m,anim=sg,gen", "NOUN,anim,masc,Sgtm,Surn sing,gent"),
    ("Эльконина", "S,famn,m,anim=sg,gen", "NOUN,anim,masc,Sgtm,Surn sing,gent"),
    # ("Копытов", "S,famn,m,anim=sg,nom", "NOUN,inan,masc plur,gent"),

    # fut
    ("будем", "V,ipf,intr,act=pl,fut,1p,indic", "VERB,impf,intr plur,1per,futr,indc"),
    ("стану", "V,pf,intr,act=sg,fut,1p,indic", "VERB,perf,intr sing,1per,futr,indc"),
    ("будут", "V,ipf,intr,act=pl,fut,3p,indic", "VERB,impf,intr plur,3per,futr,indc"),
    ("выпьем", "V,pf,tran=pl,act,fut,1p,indic", "VERB,perf,tran plur,1per,futr,indc"),
    ("позволит", "V,pf,tran=sg,act,fut,3p,indic", "VERB,perf,tran sing,3per,futr,indc"),
    ("загонят", "V,pf,tran=pl,act,fut,3p,indic", "VERB,perf,tran plur,3per,futr,indc"),
    ("станет", "V,pf,intr,act=sg,fut,3p,indic", "VERB,perf,intr sing,3per,futr,indc"),
    ("сможет", "V,pf,intr,act=sg,fut,3p,indic", "VERB,perf,intr sing,3per,futr,indc"),
    ("занесёт", "V,pf,tran=sg,act,fut,3p,indic", "VERB,perf,tran sing,3per,futr,indc"),
    ("потребуется", "V,pf,intr,med=sg,fut,3p,indic", "VERB,perf,intr sing,3per,futr,indc"),
    ("потечёт", "V,pf,intr,act=sg,fut,3p,indic", "VERB,perf,intr sing,3per,futr,indc"),
    ("будете", "V,ipf,intr,act=pl,fut,2p,indic", "VERB,impf,intr plur,2per,futr,indc"),
    ("Отмечу", "V,pf,tran=sg,act,fut,1p,indic", "VERB,perf,tran sing,1per,futr,indc"),
    ("отдам", "V,pf,tran=sg,act,fut,1p,indic", "VERB,perf,tran sing,1per,futr,indc"),

    # gen
    # ("всего", "S-PRO,n,sg=gen", "ADJF,Apro neut,sing,gent"),
    ("рассмотрения", "S,n,inan=sg,gen", "NOUN,inan,neut sing,gent"),
    ("закона", "S,m,inan=sg,gen", "NOUN,inan,masc sing,gent"),
    ("изменений", "S,n,inan=pl,gen", "NOUN,inan,neut plur,gent"),
    ("государственной", "A=f,sg,gen,plen", "ADJF femn,sing,gent"),
    ("наших", "A-PRO=pl,gen", "ADJF,Apro plur,gent"),
    ("тебя", "S-PRO,sg,2p=gen", "NPRO,2per sing,gent"),
    ("соответствующих", "A=pl,gen,plen", "ADJF plur,gent"),
    ("интеллигентных", "A=pl,gen,plen", "ADJF,Qual plur,gent"),
    ("состояния", "S,n,inan=sg,gen", "NOUN,inan,neut sing,gent"),
    ("горки", "S,f,inan=sg,gen", "NOUN,inan,femn sing,gent"),
    ("работы", "S,f,inan=sg,gen", "NOUN,inan,femn sing,gent"),
    ("процентов", "S,m,inan=pl,gen", "NOUN,inan,masc plur,gent"),
    ("движения", "S,n,inan=sg,gen", "NOUN,inan,neut sing,gent"),

    # gen2
    # ("характеру", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,datv"),
    ("коньяку", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),
    ("ходу", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),
    # ("полу", "S,m,inan=sg,gen2", "NOUN,anim,masc,Name sing,datv | NOUN,inan,femn sing,accs | NOUN,inan,masc sing,datv | NOUN,inan,masc sing,loc2"),
    ("сахарку", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),

    # ("разу", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,datv"),
    ("разбегу", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),
    ("коньячку", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),
    ("Лишку", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),
    ("народу", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),
    ("коньяку", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2"),
    # ("разу", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,datv"),
    # ("виду", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2 | NOUN,inan,masc sing,datv | NOUN,inan,masc sing,loc2"),
    ("году", "S,m,inan=sg,gen2", "NOUN,inan,masc sing,gen2,Infr"),

    # ger
    ("затратив", "V,pf,tran=ger,act,praet", "GRND,perf,tran past"),
    ("торопясь", "V,ipf,intr,med=ger,praes", "GRND,impf,intr pres"),
    ("эксплуатируя", "V,ipf,tran=ger,act,praes", "GRND,impf,tran pres"),
    ("Вынося", "V,ipf,tran=ger,act,praes", "GRND,impf,tran pres"),
    ("молча", "V,ipf,intr,act=ger,praes", "GRND,impf,intr pres"),
    ("отвлекаясь", "V,ipf,intr,med=ger,praes", "GRND,impf,intr pres"),
    ("Вспоминая", "V,ipf,tran=ger,act,praes", "GRND,impf,tran pres"),
    ("основываясь", "V,ipf,intr,med=ger,praes", "GRND,impf,intr pres"),
    ("составив", "V,pf,tran=ger,act,praet", "GRND,perf,tran past"),
    ("сползая", "V,ipf,intr,act=ger,praes", "GRND,impf,intr pres"),
    ("Приехав", "V,pf,intr,act=ger,praet", "GRND,perf,intr past"),
    ("Уезжая", "V,ipf,intr,act=ger,praes", "GRND,impf,intr pres"),
    ("ограничиваясь", "V,ipf,intr,med=ger,praes", "GRND,impf,intr pres"),
    ("изображая", "V,ipf,tran=ger,act,praes", "GRND,impf,tran pres"),
    ("управляясь", "V,ipf,intr,med=ger,praes", "GRND,impf,intr pres"),

    # imper
    ("Давайте", "V,ipf,tran=pl,2p,act,imper", "VERB,impf,tran plur,impr,excl"),
    ("выбирайте", "V,ipf,tran=pl,act,2p,imper", "VERB,impf,tran plur,impr,excl"),
    ("берите", "V,ipf,tran,act=pl,2p,imper", "VERB,impf,tran plur,impr,excl"),
    ("вынимайте", "V,ipf,tran=pl,act,2p,imper", "VERB,impf,tran plur,impr,excl"),
    ("читайте", "V,ipf,tran=pl,act,2p,imper", "VERB,impf,tran plur,impr,excl"),
    # ("определим", "V,pf,tran=pl,act,1p,imper", "VERB,perf,tran sing,impr,incl"),
    ("возьми", "V,pf,tran=sg,act,2p,imper", "VERB,perf,tran sing,impr,excl"),
    ("побудьте", "V,pf,intr,act=pl,2p,imper", "VERB,perf,intr plur,impr,excl"),
    ("Идите", "V,ipf,intr,act=pl,2p,imper", "VERB,impf,intr plur,impr,excl"),
    ("Жди", "V,ipf,tran,act=sg,2p,imper", "VERB,impf,tran sing,impr,excl"),
    ("подмети", "V,pf,tran=sg,act,2p,imper", "VERB,perf,tran sing,impr,excl"),
    ("выделяйся", "V,ipf,intr,med=sg,2p,imper", "VERB,impf,intr sing,impr,excl"),
    ("прибедняйтесь", "V,ipf,intr,med=pl,2p,imper", "VERB,impf,intr plur,impr,excl"),
    # ("допустим", "V,pf,tran=pl,act,1p,imper", "VERB,perf,tran sing,impr,incl"),

    # imper2
    # ("Пройдёмте", "V,pf,tran=pl,act,1p,imper2", "VERB,perf,tran plur,impr,incl"),
    # ("пойдёмте", "V,pf,intr,act=pl,1p,imper2", "VERB,perf,intr plur,impr,incl"),

    # inan
    ("шиповник", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn "),
    ("программы", "S,f,inan=sg,gen", "NOUN,inan,femn sing,gent"),
    ("обязательств", "S,n,inan=pl,gen", "NOUN,inan,neut plur,gent"),
    ("поцелуи", "S,m,inan=pl,acc", "NOUN,inan,masc plur,accs"),
    ("поддержание", "S,n,inan=sg,acc", "NOUN,inan,neut sing,accs"),
    ("сопровождении", "S,n,inan=sg,loc", "NOUN,inan,neut sing,loct"),

    # indic
    ("растёт", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("попал", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("Кормите", "V,ipf,tran=pl,act,praes,2p,indic", "VERB,impf,tran plur,2per,pres,indc"),
    ("собиралась", "V,ipf,intr,med=f,sg,praet,indic", "VERB,impf,intr femn,sing,past,indc"),
    ("было", "V,ipf,intr,act=n,sg,praet,indic", "VERB,impf,intr neut,sing,past,indc"),
    ("пригласили", "V,pf,tran=pl,act,praet,indic", "VERB,perf,tran plur,past,indc"),
    ("могла", "V,ipf,intr,act=f,sg,praet,indic", "VERB,impf,intr femn,sing,past,indc"),
    ("халтурили", "V,ipf,intr,act=pl,praet,indic", "VERB,impf,intr plur,past,indc"),
    ("Прошу", "V,ipf,tran=sg,act,praes,1p,indic", "VERB,impf,tran sing,1per,pres,indc"),
    ("решил", "V,pf,tran=m,sg,act,praet,indic", "VERB,perf,tran masc,sing,past,indc"),
    ("заедешь", "V,pf,intr,act=sg,fut,2p,indic", "VERB,perf,intr sing,2per,futr,indc"),
    # ("болят", "V,ipf,intr,act=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc,Dist"),
    ("скликает", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("баловал", "V,ipf,tran=m,sg,act,praet,indic", "VERB,impf,tran masc,sing,past,indc"),

    # inf
    ("идти", "V,ipf,intr,act=inf", "INFN,impf,intr"),
    ("обязать", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("предоставить", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("сделать", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("драться", "V,ipf,intr,med=inf", "INFN,impf,intr"),
    ("шлёпнуть", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("стать", "V,pf,intr,act=inf", "INFN,perf,intr"),
    ("признать", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("Поменять", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("оставить", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("носить", "V,ipf,tran=inf,act", "INFN,impf,tran"),
    ("снять", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("обязать", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("превратиться", "V,pf,intr,med=inf", "INFN,perf,intr"),
    ("разливать", "V,ipf,tran=inf,act", "INFN,impf,tran"),


    # ins
    ("недоработками", "S,f,inan=pl,ins", "NOUN,inan,femn plur,ablt"),
    ("сдобой", "S,f,inan=sg,ins", "NOUN,inan,femn sing,ablt"),
    ("Лорой", "S,persn,f,anim=sg,ins", "NOUN,anim,femn,Name sing,ablt"),
    ("начальником", "S,m,anim=sg,ins", "NOUN,anim,masc sing,ablt"),
    ("успехом", "S,m,inan=sg,ins", "NOUN,inan,masc sing,ablt"),
    ("первым", "ANUM=m,sg,ins", "ADJF,Anum masc,sing,ablt"),
    ("образом", "S,m,inan=sg,ins", "NOUN,inan,masc sing,ablt"),
    ("порою", "S,f,inan=sg,ins", "NOUN,inan,femn sing,ablt,V-oy"),
    ("бывшим", "A=m,sg,ins,plen", "ADJF masc,sing,ablt"),
    ("Людой", "S,persn,f,anim=sg,ins", "NOUN,anim,femn,Name sing,ablt"),
    ("пенсионными", "A=pl,ins,plen", "ADJF,Qual plur,ablt"),
    ("делом", "S,n,inan=sg,ins", "NOUN,inan,neut sing,ablt"),
    ("английским", "A=m,sg,ins,plen", "ADJF masc,sing,ablt"),

    # intr
    ("растёт", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("Оказывается", "V,ipf,intr,med=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("попал", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("собиралась", "V,ipf,intr,med=f,sg,praet,indic", "VERB,impf,intr femn,sing,past,indc"),
    ("идти", "V,ipf,intr,act=inf", "INFN,impf,intr"),
    ("воздействовать", "V,ipf,intr,act=inf", "INFN,impf,intr"),
    ("были", "V,ipf,intr,act=pl,praet,indic", "VERB,impf,intr plur,past,indc"),
    ("пришёл", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("будет", "V,ipf,intr,act=sg,fut,3p,indic", "VERB,impf,intr sing,3per,futr,indc"),
    ("хозяйничают", "V,ipf,intr,act=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("подрядился", "V,pf,intr,med=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("попыталась", "V,pf,intr,med=f,sg,praet,indic", "VERB,perf,intr femn,sing,past,indc"),
    ("присоединилось", "V,pf,intr,med=n,sg,praet,indic", "VERB,perf,intr neut,sing,past,indc"),
    ("смогут", "V,pf,intr,act=pl,fut,3p,indic", "VERB,perf,intr plur,3per,futr,indc"),
    ("добежать", "V,pf,intr,act=inf", "INFN,perf,intr"),

    # ipf
    ("была", "V,ipf,intr,act=f,sg,praet,indic", "VERB,impf,intr femn,sing,past,indc"),
    ("есть", "V,ipf,intr,act=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("готовит", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("рассматривает", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("могу", "V,ipf,intr,act=sg,praes,1p,indic", "VERB,impf,intr sing,1per,pres,indc"),
    ("замечал", "V,ipf,tran=m,sg,act,praet,indic", "VERB,impf,tran masc,sing,past,indc"),
    ("видишь", "V,ipf,tran=sg,act,praes,2p,indic", "VERB,impf,tran sing,2per,pres,indc"),
    ("освежают", "V,ipf,tran=pl,act,praes,3p,indic", "VERB,impf,tran plur,3per,pres,indc"),
    ("был", "V,ipf,intr,act=m,sg,praet,indic", "VERB,impf,intr masc,sing,past,indc"),
    ("будет", "V,ipf,intr,act=sg,fut,3p,indic", "VERB,impf,intr sing,3per,futr,indc"),

    # loc
    ("Федерации", "S,f,inan=sg,loc", "NOUN,inan,femn sing,loct"),
    ("Тверском", "A=m,sg,loc,plen", "ADJF masc,sing,loct"),
    ("памяти", "S,f,inan=sg,loc", "NOUN,inan,femn sing,loct"),
    ("выставке", "S,f,inan=sg,loc", "NOUN,inan,femn sing,loct"),
    ("этом", "S-PRO,n,sg=loc", "NPRO,neut sing,loct"),
    ("хозяйстве", "S,n,inan=sg,loc", "NOUN,inan,neut sing,loct"),
    ("тексте", "S,m,inan=sg,loc", "NOUN,inan,masc sing,loct"),
    ("огромных", "A=pl,loc,plen", "ADJF,Qual plur,loct"),
    ("гамаках", "S,m,inan=pl,loc", "NOUN,inan,masc plur,loct"),
    ("Думе", "S,f,inan=sg,loc", "NOUN,inan,femn sing,loct"),
    ("внесении", "S,n,inan=sg,loc", "NOUN,inan,neut sing,loct"),
    ("налоге", "S,m,inan=sg,loc", "NOUN,inan,masc sing,loct"),
    ("рамках", "S,f,inan=pl,loc", "NOUN,inan,femn plur,loct"),
    ("Вселенной", "S,f,inan=sg,loc", "NOUN,inan,femn sing,loct"),

    # loc2
    ("связи", "S,f,inan=sg,loc2", "NOUN,inan,femn sing,loc2"),
    ("году", "S,m,inan=sg,loc2", "NOUN,inan,masc sing,loc2"),
    ("Крыму", "S,m,inan=sg,loc2", "NOUN,inan,masc,Sgtm,Geox sing,loc2"),
    ("году", "S,m,inan=sg,loc2", "NOUN,inan,masc sing,loc2"),
    ("сети", "S,f,inan=sg,loc2", "NOUN,inan,femn sing,loc2"),
    ("году", "S,m,inan=sg,loc2", "NOUN,inan,masc sing,loc2"),
    # ("шагу", "S,m,inan=sg,loc2", "NOUN,inan,masc sing,datv"),
    ("саду", "S,m,inan=sg,loc2", "NOUN,inan,masc sing,loc2"),
    ("виду", "S,m,inan=sg,loc2", "NOUN,inan,masc sing,loc2"),

    # m
    ("шиповник", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("снят", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("проект", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("закона", "S,m,inan=sg,gen", "NOUN,inan,masc sing,gent"),
    ("Закон", "S,m,inan=sg,acc", "NOUN,inan,masc sing,accs"),
    ("телефонов", "S,m,inan=pl,gen", "NOUN,inan,masc plur,gent"),
    ("столик", "S,m,inan=sg,acc", "NOUN,inan,masc sing,accs"),
    ("контроля", "S,m,inan=sg,gen", "NOUN,inan,masc sing,gent"),
    ("порядок", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("герпетологам", "S,m,anim=pl,dat", "NOUN,anim,masc plur,datv"),
    ("Буйнов", "S,famn,m,anim=sg,nom", "NOUN,anim,masc,Sgtm,Surn sing,nomn"),
    ("нормальному", "A=m,sg,dat,plen", "ADJF,Qual masc,sing,datv"),

    # m-f
    ("коллегами", "S,m-f,anim=pl,ins", "NOUN,anim,femn,Ms-f plur,ablt"),
    ("протеже", "S,m-f,anim,0=sg,gen", "NOUN,anim,GNdr,Ms-f,Fixd sing,gent"),
    # ("КАРАБАШ", "S,famn,m-f,inan=sg,nom", "NOUN,inan,masc,Sgtm,Geox sing,nomn"),
    # ("Ли", "S,famn,m-f,anim,0=sg,gen", "NOUN,anim,masc,Sgtm,Fixd,Name sing,nomn"),
    # ("Лэнсбери", "S,famn,m-f,anim,0=sg,nom", "NOUN,inan,masc,Sgtm,Fixd,Geox sing,nomn"),
    ("пьянчужку", "S,m-f,anim=sg,acc", "NOUN,anim,femn,Ms-f sing,accs"),
    ("коллеги", "S,m-f,anim=sg,gen", "NOUN,anim,femn,Ms-f sing,gent"),
    ("Зинченко", "S,m-f,famn,anim,0=sg,nom", "NOUN,anim,GNdr,Ms-f,Fixd,Surn sing,nomn"),
    #("Кириенко", "S,famn,m-f,anim,0=sg,dat", "NOUN,anim,GNdr,Ms-f,Fixd,Surn sing,datv | NOUN,anim,GNdr,Ms-f,Fixd,Surn plur,datv"),
    ("бедолага", "S,m-f,anim=sg,nom", "NOUN,anim,femn,Ms-f sing,nomn"),
    ("Паша", "S,persn,m-f,anim=sg,nom", "NOUN,anim,masc,Name,Ms-f sing,nomn"),
    ("Пашей", "S,persn,m-f,anim=sg,ins", "NOUN,anim,masc,Name,Ms-f sing,ablt"),

    # med
    ("Оказывается", "V,ipf,intr,med=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("собиралась", "V,ipf,intr,med=f,sg,praet,indic", "VERB,impf,intr femn,sing,past,indc"),
    ("увенчались", "V,pf,intr,med=pl,praet,indic", "VERB,perf,intr plur,past,indc"),
    ("отличающееся", "V,ipf,intr,med=partcp,n,sg,nom,praes,plen", "PRTF,impf,intr,pres,actv neut,sing,nomn"),
    ("драться", "V,ipf,intr,med=inf", "INFN,impf,intr"),
    ("оказалась", "V,pf,intr,med=f,sg,praet,indic", "VERB,perf,intr femn,sing,past,indc"),
    ("оказавшись", "V,pf,intr,med=ger,praet", "GRND,perf,intr past,V-sh"),
    ("удалось", "V,pf,intr,med=n,sg,praet,indic", "VERB,perf,intr neut,sing,past,indc"),
    ("проносятся", "V,intr,med,ipf=praes,pl,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("создавалось", "V,ipf,intr,med=n,sg,praet,indic", "VERB,impf,intr neut,sing,past,indc"),
    ("подался", "V,pf,intr,med=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("назывались", "V,ipf,intr,med=pl,praet,indic", "VERB,impf,intr plur,past,indc"),
    ("выделяются", "V,ipf,intr,med=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("договорились", "V,pf,intr,med=pl,praet,indic", "VERB,perf,intr plur,past,indc"),
    ("называются", "V,ipf,intr,med=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),

    # n
    ("это", "S-PRO,n,sg=nom", "NPRO,neut sing,nomn"),
    ("рассмотрения", "S,n,inan=sg,gen", "NOUN,inan,neut sing,gent"),
    ("внесении", "S,n,inan=sg,loc", "NOUN,inan,neut sing,loct"),
    ("изменений", "S,n,inan=pl,gen", "NOUN,inan,neut plur,gent"),
    ("незаконное", "A=n,sg,nom,plen", "ADJF,Qual neut,sing,nomn"),
    ("назначения", "S,n,inan=sg,gen", "NOUN,inan,neut sing,gent"),
    ("такое", "A-PRO=n,sg,nom", "ADJF,Apro neut,sing,nomn "),
    ("иностранного", "A=n,sg,gen,plen", "ADJF neut,sing,gent"),
    ("Единство", "S,n,inan=sg,nom", "NOUN,inan,neut sing,nomn"),
    ("случилось", "V,pf,intr,med=n,sg,praet,indic", "VERB,perf,intr neut,sing,past,indc"),
    ("аккумулирования", "S,n,inan=sg,gen", "NOUN,inan,neut sing,gent"),
    ("право", "S,n,inan=sg,acc", "NOUN,inan,neut sing,accs"),

    # nom
    ("шиповник", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("промежуточный", "A=m,sg,nom,plen", "ADJF masc,sing,nomn"),
    ("которые", "A-PRO=pl,nom", "ADJF,Apro plur,nomn"),
    ("суд", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("совещание", "S,n,inan=sg,nom", "NOUN,inan,neut sing,nomn"),
    ("подвижная", "A=f,sg,nom,plen", "ADJF,Qual femn,sing,nomn"),
    ("Электорат", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("программа", "S,f,inan=sg,nom", "NOUN,inan,femn sing,nomn"),
    ("вы", "S-PRO,pl,2p=nom", "NPRO,2per plur,nomn"),

    # normal

    # obsc
    # ("мудаками", "S,m,anim,obsc=pl,ins", "NOUN,anim,masc,Sgtm,Fixd,Name sing,nomn | NOUN,anim,masc,Sgtm,Fixd,Name sing,gent | NOUN,anim,masc,Sgtm,Fixd,Name sing,datv | NOUN,anim,masc,Sgtm,Fixd,Name sing,accs | NOUN,anim,masc,Sgtm,Fixd,Name sing,ablt | NOUN,anim,masc,Sgtm,Fixd,Name sing,loct | NOUN,inan,masc plur,ablt"),
    # ("хитрожопой", "A,obsc=f,sg,ins,plen", "NOUN,inan,femn sing,ablt | VERB,perf,tran sing,impr,excl"),
    # ("...баный", "A=obsc=m,sg,nom=abbr", "ADJF masc,sing,nomn"),
    # ("Манда", "S,f,inan,obsc=sg,nom", "NOUN,anim,femn,Name sing,nomn | NOUN,inan,femn sing,nomn"),
    # ("выблядок", "S,m,anim,obsc=sg,nom", "NOUN,anim,masc sing,nomn"),

    # partcp
    ("снят", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("подписаны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("сделано", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("закончен", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("торчащие", "V,ipf,intr,act=partcp,pl,acc,praes,plen", "PRTF,impf,intr,pres,actv inan,plur,accs"),
    ("изложенные", "V,pf,tran=partcp,pl,nom,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,nomn"),
    ("повлёкшим", "V,pf,tran=partcp,n,sg,ins,act,praet,plen", "PRTF,perf,tran,past,actv neut,sing,ablt"),
    ("продиктована", "V,pf,tran=partcp,f,sg,brev,pass,praet", "PRTS,perf,past,pssv femn,sing"),
    ("уполномочена", "V,pf,tran=partcp,f,sg,brev,pass,praet", "PRTS,perf,past,pssv femn,sing"),
    # ("вредящие", "V,ipf,intr,act=partcp,pl,acc,praes", "PRTF,impf,intr,pres,actv inan,plur,accs"),
    ("приняты", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("включённых", "V,pf,tran=partcp,pl,gen,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,gent"),
    ("отмечено", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("умирающей", "V,ipf,intr,act=partcp,f,sg,gen,praes,plen", "PRTF,impf,intr,pres,actv femn,sing,gent"),

    # pass
    ("снят", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("подписаны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("сделано", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("закончен", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("уверен", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("предъявляемые", "V,ipf,tran=partcp,pl,acc,pass,praes,plen", "PRTF,impf,tran,pres,pssv inan,plur,accs"),
    ("предоставлен", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("рассчитанная", "V,pf,tran=partcp,f,sg,nom,pass,praet,plen", "PRTF,perf,tran,past,pssv femn,sing,nomn"),
    ("употребляемая", "V,ipf,tran=partcp,f,sg,nom,pass,praes,plen", "PRTF,impf,tran,pres,pssv femn,sing,nomn"),
    ("сделанная", "V,pf,tran=partcp,f,sg,nom,pass,praet,plen", "PRTF,perf,tran,past,pssv femn,sing,nomn"),
    ("упомянутая", "V,pf,tran=partcp,f,sg,nom,pass,praet,plen", "PRTF,perf,tran,past,pssv femn,sing,nomn"),
    ("обязаны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("описаны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("уплаченных", "V,pf,tran=partcp,pl,gen,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,gent"),
    ("приближенных", "V,pf,tran=partcp,pl,gen,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,gent"),

    # patrn
    ("Андреевна", "S,patrn,f,anim=sg,nom", "NOUN,anim,femn,Patr sing,nomn"),
    ("Ильич", "S,patrn,m,anim=sg,nom", "NOUN,anim,masc,Patr sing,nomn"),
    ("Сергеевич", "S,patrn,m,anim=sg,nom", "NOUN,anim,masc,Patr sing,nomn"),
    ("Петровна", "S,patrn,f,anim=sg,nom", "NOUN,anim,femn,Patr sing,nomn"),
    ("Фёдоровна", "S,patrn,f,anim=sg,nom", "NOUN,anim,femn,Patr sing,nomn"),
    ("Андреевне", "S,patrn,f,anim=sg,dat", "NOUN,anim,femn,Patr sing,datv"),
    ("Алексеевича", "S,patrn,m,anim=sg,gen", "NOUN,anim,masc,Patr sing,gent"),
    ("Михайловна", "S,patrn,f,anim=sg,nom", "NOUN,anim,femn,Patr sing,nomn"),
    ("Абрамовича", "S,patrn,m,anim=sg,acc", "NOUN,anim,masc,Patr sing,accs"),
    ("Фёдоровна", "S,patrn,f,anim=sg,nom", "NOUN,anim,femn,Patr sing,nomn"),
    ("Наумовны", "S,patrn,f,anim=sg,gen", "NOUN,anim,femn,Patr sing,gent"),
    ("Ивановича", "S,patrn,m,anim=sg,gen", "NOUN,anim,masc,Patr sing,gent"),
    ("Петровна", "S,patrn,f,anim=sg,nom", "NOUN,anim,femn,Patr sing,nomn"),
    ("Николаевича", "S,patrn,m,anim=sg,gen", "NOUN,anim,masc,Patr sing,gent"),
    ("Григорьевич", "S,patrn,m,anim=sg,nom", "NOUN,anim,masc,Patr sing,nomn"),

    # persn
    ("Марина", "S,persn,f,anim=sg,nom", "NOUN,anim,femn,Name sing,nomn"),
    ("Лорой", "S,persn,f,anim=sg,ins", "NOUN,anim,femn,Name sing,ablt"),
    ("Лоры", "S,persn,f,anim=sg,gen", "NOUN,anim,femn,Name sing,gent"),
    ("Михаил", "S,persn,m,anim=sg,nom", "NOUN,anim,masc,Name sing,nomn"),
    ("Валерия", "S,persn,m,anim=sg,gen", "NOUN,anim,masc,Name sing,gent"),
    ("Игорь", "S,persn,m,anim=sg,nom", "NOUN,anim,masc,Name sing,nomn"),
    ("Анатолий", "S,persn,m,anim=sg,nom", "NOUN,anim,masc,Name sing,nomn"),
    ("Гена", "S,persn,m,anim=sg,nom", "NOUN,anim,masc,Name sing,nomn"),
    ("Борис", "S,persn,m,anim=sg,nom", "NOUN,anim,masc,Name sing,nomn"),
    ("Маша", "S,persn,f,anim=sg,nom", "NOUN,anim,femn,Name sing,nomn"),
    ("Иван", "S,persn,m,anim=sg,nom", "NOUN,anim,masc,Name sing,nomn"),
    ("Дашка", "S,persn,f,anim=sg,nom", "NOUN,anim,femn,Name sing,nomn"),

    # pf
    ("взять", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("взял", "V,pf,tran=m,sg,act,praet,indic", "VERB,perf,tran masc,sing,past,indc"),
    ("указанные", "V,pf,tran=partcp,pl,nom,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,nomn"),
    ("сумели", "V,pf,intr,act=pl,praet,indic", "VERB,perf,intr plur,past,indc"),
    ("понять", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("прокомментировал", "V,pf,tran=m,sg,act,praet,indic", "VERB,perf,tran masc,sing,past,indc"),
    ("поставлены", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("догадался", "V,pf,intr,med=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("предусмотренным", "V,pf,tran=partcp,pl,dat,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,datv"),
    ("получить", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("снят", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("попал", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("пришли", "V,pf,intr,act=pl,praet,indic", "VERB,perf,intr plur,past,indc"),
    ("дошла", "V,pf,intr,act=f,sg,praet,indic", "VERB,perf,intr femn,sing,past,indc"),
    ("подписаны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),

    # pl
    ("недоработками", "S,f,inan=pl,ins", "NOUN,inan,femn plur,ablt"),
    ("изменений", "S,n,inan=pl,gen", "NOUN,inan,neut plur,gent"),
    ("дополнений", "S,n,inan=pl,gen", "NOUN,inan,neut plur,gent"),
    ("предприятий", "S,n,inan=pl,gen", "NOUN,inan,neut plur,gent"),
    ("Кормите", "V,ipf,tran=pl,act,praes,2p,indic", "VERB,impf,tran plur,2per,pres,indc"),
    ("действуют", "V,ipf,intr,act=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("пистолетными", "A=pl,ins,plen", "ADJF plur,ablt"),
    ("дефекты", "S,m,inan=pl,nom", "NOUN,inan,masc plur,nomn"),
    ("раз", "S,m,inan=pl,gen", "NOUN,inan,masc plur,gent"),
    ("уплачиваются", "V,ipf,intr,med=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("попадут", "V,pf,intr,act=pl,fut,3p,indic", "VERB,perf,intr plur,3per,futr,indc"),
    ("крики", "S,m,inan=pl,nom", "NOUN,inan,masc plur,nomn"),
    ("скважинах", "S,f,inan=pl,loc", "NOUN,inan,femn plur,loct"),
    ("разработанные", "V,pf,tran=partcp,pl,nom,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,nomn"),
    ("профессиональных", "A=pl,gen,plen", "ADJF,Qual plur,gent"),

    # plen
    ("дикая", "A=f,sg,nom,plen", "ADJF,Qual femn,sing,nomn"),
    ("собачья", "A=f,sg,nom,plen", "ADJF,Poss femn,sing,nomn"),
    ("лавровый", "A=m,sg,nom,plen", "ADJF masc,sing,nomn"),
    ("плоская", "A=f,sg,nom,plen", "ADJF,Qual femn,sing,nomn"),
    ("мёртвое", "A=n,sg,nom,plen", "ADJF,Qual neut,sing,nomn"),
    ("мировая", "A=f,sg,nom,plen", "ADJF femn,sing,nomn"),
    ("единственным", "A=n,sg,ins,plen", "ADJF neut,sing,ablt"),
    ("стандартной", "A=f,sg,dat,plen", "ADJF,Qual femn,sing,datv"),
    ("письменный", "A=m,sg,acc,inan,plen", "ADJF,Qual inan,masc,sing,accs"),
    ("надёжными", "A=pl,ins,plen", "ADJF,Qual plur,ablt"),
    ("скромненькая", "A=f,sg,nom,plen", "ADJF femn,sing,nomn"),

    # praes
    ("отличающееся", "V,ipf,intr,med=partcp,n,sg,nom,praes,plen", "PRTF,impf,intr,pres,actv neut,sing,nomn"),
    ("существуют", "V,ipf,intr,act=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("развивается", "V,ipf,intr,med=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("наследуются", "V,ipf,intr,med=pl,praes,3p,indic", "VERB,impf,intr plur,3per,pres,indc"),
    ("ведущих", "V,ipf,tran=partcp,pl,gen,act,praes,plen", "PRTF,Subx,impf,tran,pres,actv plur,gent"),
    ("твердят", "V,ipf,tran=pl,act,praes,3p,indic", "VERB,impf,tran plur,3per,pres,indc"),
    ("плачу", "V,ipf,intr,act=sg,praes,1p,indic", "VERB,impf,intr sing,1per,pres,indc"),
    ("составляющая", "V,ipf,tran=partcp,f,sg,nom,act,praes,plen", "PRTF,impf,tran,pres,actv femn,sing,nomn"),
    ("выплачивается", "V,ipf,intr,med=sg,praes,3p,indic", "VERB,impf,intr sing,3per,pres,indc"),
    ("делают", "V,ipf,tran=pl,act,praes,3p,indic", "VERB,impf,tran plur,3per,pres,indc"),
    ("выкуриваемых", "V,ipf,tran=partcp,pl,gen,pass,praes,plen", "PRTF,impf,tran,pres,pssv plur,gent"),

    # praet
    ("снят", "V,pf,tran=partcp,m,sg,brev,pass,praet", "PRTS,perf,past,pssv masc,sing"),
    ("попал", "V,pf,intr,act=m,sg,praet,indic", "VERB,perf,intr masc,sing,past,indc"),
    ("собиралась", "V,ipf,intr,med=f,sg,praet,indic", "VERB,impf,intr femn,sing,past,indc"),
    ("пришли", "V,pf,intr,act=pl,praet,indic", "VERB,perf,intr plur,past,indc"),
    ("посиживал", "V,ipf,intr,act=m,sg,praet,indic", "VERB,impf,intr masc,sing,past,indc"),
    ("включённом", "V,pf,tran=partcp,m,sg,loc,pass,praet,plen", "PRTF,perf,tran,past,pssv masc,sing,loct"),
    ("вспученного", "V,pf,tran=partcp,m,sg,gen,pass,praet,plen", "PRTF,perf,tran,past,pssv masc,sing,gent"),
    ("учтена", "V,pf,tran=partcp,f,sg,brev,pass,praet", "PRTS,perf,past,pssv femn,sing"),
    ("начисленной", "V,pf,tran=partcp,f,sg,gen,pass,praet,plen", "PRTF,perf,tran,past,pssv femn,sing,gent"),
    ("нашли", "V,pf,tran=pl,act,praet,indic", "VERB,perf,tran plur,past,indc"),
    ("начисленных", "V,pf,tran=partcp,pl,gen,pass,praet,plen", "PRTF,perf,tran,past,pssv plur,gent"),
    ("бросила", "V,pf,tran=f,sg,act,praet,indic", "VERB,perf,tran femn,sing,past,indc"),
    ("погибла", "V,pf,intr,act=f,sg,praet,indic", "VERB,perf,intr femn,sing,past,indc"),
    ("Измаялась", "V,pf,intr,med=f,sg,praet,indic", "VERB,perf,intr femn,sing,past,indc"),
    ("рассчитано", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),

    # sg
    ("была", "V,ipf,intr,act=f,sg,praet,indic", "VERB,impf,intr femn,sing,past,indc"),
    ("ПЕРЕКЛЮЧАТЕЛЬ", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("Германия", "S,f,inan=sg,nom", "NOUN,inan,femn,Sgtm,Geox sing,nomn"),
    ("судебном", "A=n,sg,loc,plen", "ADJF,Qual neut,sing,loct"),
    ("интерес", "S,m,inan=sg,nom", "NOUN,inan,masc sing,nomn"),
    ("большим", "A=n,sg,ins,plen", "ADJF neut,sing,ablt"),
    ("связи", "S,f,inan=sg,loc2", "NOUN,inan,femn sing,loc2"),
    ("бизнесом", "S,m,inan=sg,ins", "NOUN,inan,masc sing,ablt"),
    ("жизни", "S,f,inan=sg,dat", "NOUN,inan,femn sing,datv"),

    # supr

    # tran
    ("подписаны", "V,pf,tran=partcp,pl,brev,pass,praet", "PRTS,perf,past,pssv plur"),
    ("сделано", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("сказала", "V,pf,tran=f,sg,act,praet,indic", "VERB,perf,tran femn,sing,past,indc"),
    ("вызывающий", "V,ipf,tran=partcp,m,sg,acc,act,praes,plen", "PRTF,impf,tran,pres,actv inan,masc,sing,accs"),
    ("забыли", "V,pf,tran=pl,act,praet,indic", "VERB,perf,tran plur,past,indc"),
    ("разрешает", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("оценить", "V,pf,tran=inf,act", "INFN,perf,tran"),
    ("переезжаем", "V,ipf,tran=pl,act,praes,1p,indic", "VERB,impf,tran plur,1per,pres,indc"),
    ("получает", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("объявлено", "V,pf,tran=partcp,n,sg,brev,pass,praet", "PRTS,perf,past,pssv neut,sing"),
    ("даёт", "V,ipf,tran=sg,act,praes,3p,indic", "VERB,impf,tran sing,3per,pres,indc"),
    ("платят", "V,ipf,tran=pl,act,praes,3p,indic", "VERB,impf,tran plur,3per,pres,indc"),

    # voc
    # ("Зинк", "S,persn,f,anim=sg,voc", "NOUN,anim,masc sing,nomn | NOUN,inan,masc sing,nomn"),
    # zoon
]

def test_from_opencorpora():
    def _gr(tag):
        return set(tag.replace('=', ',').split(','))

    total = len(TEST_DATA)
    errors = 0

    # print()
    # print("%-4s %-17s %-45s %-45s %-25s %-30s" % ("", "word", "correct", "converted", "error", "source"))
    for word, ruscorpora_tag, opencorpora_tag in TEST_DATA:
        converted = ruscorpora.from_opencorpora_int(opencorpora_tag)

        gold = _gr(ruscorpora_tag) # - set(['act', 'med'])
        got = _gr(converted)
        diff = gold ^ got

        if gold != got and not diff.issubset(set(['med', 'act'])):
            errors += 1
            OK = 'ERR'
            msg = "%-4s %-17s %-45s %-45s %-25s %-30s" % (
                OK, word, ruscorpora_tag, converted, diff, opencorpora_tag
            )
            print(msg)

    if errors:
        print("Errors: %d/%d = %0.1f%%" % (errors, total, errors/total * 100))
        raise AssertionError()
