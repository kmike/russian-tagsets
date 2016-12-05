# -*- coding: utf-8 -*-
"""
Conversion between OpenCorpora.org (http://opencorpora.org/dict.php?act=gram)
tagset and other tagsets.
"""
from __future__ import absolute_import, unicode_literals
from russian_tagsets import converters, positional, aot
from russian_tagsets.utils import invert_mapping

GRAM_TABLE = [
    # num, internal tag, external tag, description, parent, aot.ru tag
    ['1', 'POST', 'ЧР', 'часть речи', '—', None],
    ['2', 'NOUN', 'СУЩ', 'имя существительное', 'POST', 'С'],
    ['3', 'ADJF', 'ПРИЛ', 'имя прилагательное (полное)', 'POST', 'П'],
    ['4', 'ADJS', 'КР_ПРИЛ', 'имя прилагательное (краткое)', 'POST', 'КР_ПРИЛ'],
    ['5', 'COMP', 'КОМП', 'компаратив', 'POST', 'П'], # fixme: aot
    ['6', 'VERB', 'ГЛ', 'глагол (личная форма)', 'POST', 'Г'],
    ['7', 'INFN', 'ИНФ', 'глагол (инфинитив)', 'POST', 'ИНФИНИТИВ'],
    ['8', 'PRTF', 'ПРИЧ', 'причастие (полное)', 'POST', 'ПРИЧАСТИЕ'],
    ['10', 'PRTS', 'КР_ПРИЧ', 'причастие (краткое)', 'POST', 'КР_ПРИЧАСТИЕ'],
    ['11', 'GRND', 'ДЕЕПР', 'деепричастие', 'POST', 'ДЕЕПРИЧАСТИЕ'],
    ['12', 'NUMR', 'ЧИСЛ', 'числительное', 'POST', 'ЧИСЛ'],
    ['13', 'ADVB', 'Н', 'наречие', 'POST', 'Н'],
    ['14', 'NPRO', 'МС', 'местоимение-существительное', 'POST', 'МС'],
    ['15', 'PRED', 'ПРЕДК', 'предикатив', 'POST', 'ПРЕДК'],
    ['16', 'PREP', 'ПР', 'предлог', 'POST', 'ПРЕДЛ'],
    ['17', 'CONJ', 'СОЮЗ', 'союз', 'POST', 'СОЮЗ'],
    ['18', 'PRCL', 'ЧАСТ', 'частица', 'POST', 'ЧАСТ'],
    ['19', 'INTJ', 'МЕЖД', 'междометие', 'POST', 'МЕЖД'],

    ['21', 'ANim', 'Од-неод', 'одушевлённость / одушевлённость не выражена', '—', None],
    ['22', 'anim', 'од', 'одушевлённое', 'ANim', 'од'],
    ['23', 'inan', 'неод', 'неодушевлённое', 'ANim', 'но'],

    ['24', 'GNdr', 'хр', 'род / род не выражен', '—', None],
    ['25', 'masc', 'мр', 'мужской род', 'GNdr', 'мр'],
    ['26', 'femn', 'жр', 'женский род', 'GNdr', 'жр'],
    ['27', 'neut', 'ср', 'средний род', 'GNdr', 'ср'],
    ['28', 'Ms-f', 'ор', 'общий род', '—', 'мр-жр'],

    ['29', 'NMbr', 'Число', 'число', '—', None],
    ['30', 'sing', 'ед', 'единственное число', 'NMbr', 'ед'],
    ['31', 'plur', 'мн', 'множественное число', 'NMbr', 'мн'],
    ['32', 'Sgtm', 'sg', 'singularia tantum', '—', None], # fixme: aot?
    ['33', 'Pltm', 'pl', 'pluralia tantum', '—', None], # fixme: aot?
    ['36', 'Fixd', '0', 'неизменяемое', '—', '0'],

    ['37', 'CAse', 'Падеж', 'категория падежа', '—', None],
    ['38', 'nomn', 'им', 'именительный падеж', 'CAse', 'им'],
    ['39', 'gent', 'рд', 'родительный падеж', 'CAse', 'рд'],
    ['40', 'datv', 'дт', 'дательный падеж', 'CAse', 'дт'],
    ['41', 'accs', 'вн', 'винительный падеж', 'CAse', 'вн'],
    ['42', 'ablt', 'тв', 'творительный падеж', 'CAse', 'тв'],
    ['43', 'loct', 'пр', 'предложный падеж', 'CAse', 'пр'],
    ['44', 'voct', 'зв', 'звательный падеж', 'nomn', 'зв'],
    ['45', 'gen1', 'рд1', 'первый родительный падеж', 'gent', 'рд'], # fixme: aot
    ['46', 'gen2', 'рд2', 'второй родительный (частичный) падеж', 'gent', 'рд'], # fixme: aot
    ['47', 'acc2', 'вн2', 'второй винительный падеж', 'accs', 'вн'], # fixme: aot
    ['48', 'loc1', 'пр1', 'первый предложный падеж', 'loct', 'пр'], # fixme: aot
    ['49', 'loc2', 'пр2', 'второй предложный (местный) падеж', 'loct', 'пр'], # fixme: aot

    ['50', 'Abbr', 'аббр', 'аббревиатура', '—', 'аббр'],
    ['51', 'Name', 'имя', 'имя', '—', 'имя'],
    ['52', 'Surn', 'фам', 'фамилия', '—', 'фам'],
    ['53', 'Patr', 'отч', 'отчество', '—', 'отч'],
    ['54', 'Geox', 'гео', 'топоним', '—', 'лок'], # XXX: is aot tag correct?
    ['55', 'Orgn', 'орг', 'организация', '—', None],
    ['56', 'Trad', 'tm', 'торговая марка', '—', None],
    ['57', 'Subx', 'субст?', 'возможна субстантивация', '—', None],
    ['58', 'Supr', 'превосх', 'превосходная степень', '—', 'прев'],
    ['59', 'Qual', 'кач', 'качественное', '—', 'кач'],
    ['60', 'Apro', 'мест-п', 'местоименное', '—', None],
    ['61', 'Anum', 'числ-п', 'порядковое', '—', None],
    ['62', 'Poss', 'притяж', 'притяжательное', '—', 'притяж'],
    ['63', 'V-ey', '*ею', 'форма на -ею', '—', None],
    ['64', 'V-oy', '*ою', 'форма на -ою', '—', None],
    ['65', 'Cmp2', 'сравн2', 'сравнительная степень на по-', '—', None], # fixme: aot
    ['66', 'V-ej', '*ей', 'форма компаратива на -ей', '—', None], # fixme: aot

    ['67', 'ASpc', 'Вид', 'категория вида', '—', None],
    ['68', 'perf', 'сов', 'совершенный вид', 'ASpc', None],
    ['69', 'impf', 'несов', 'несовершенный вид', 'ASpc', None],

    ['70', 'TRns', 'Перех', 'категория переходности', '—', None],
    ['71', 'tran', 'перех', 'переходный', 'TRns', None],
    ['72', 'intr', 'неперех', 'непереходный', 'TRns', None],

    ['73', 'Impe', 'безл', 'безличный', '—', 'безл'],
    ['74', 'Uimp', 'безл-у', 'безличное употребление', '—', 'безл'], # fixme: aot?
    ['75', 'Mult', 'мног', 'многократный', '—', None],
    ['76', 'Refl', 'возвр', 'возвратный', '—', None],

    ['77', 'PErs', 'Лицо', 'категория лица', '—', None],
    ['78', '1per', '1л', '1 лицо', 'PErs', '1л'],
    ['79', '2per', '2л', '2 лицо', 'PErs', '2л'],
    ['80', '3per', '3л', '3 лицо', 'PErs', '3л'],

    ['81', 'TEns', 'Время', 'категория времени', '—', None],
    ['82', 'pres', 'наст', 'настоящее время', 'TEns', 'нст'],
    ['83', 'past', 'прош', 'прошедшее время', 'TEns', 'прш'],
    ['84', 'futr', 'буд', 'будущее время', 'TEns', 'буд'],

    ['85', 'MOod', 'Накл', 'категория наклонения', '—', None],
    ['86', 'indc', 'изъяв', 'изъявительное наклонение', 'MOod', None],
    ['87', 'impr', 'повел', 'повелительное наклонение', 'MOod', 'пвл'],

    ['88', 'INvl', 'Совм', 'категория совместности', '—', None],
    ['89', 'incl', 'вкл', 'говорящий включён в действие', 'INvl', None],
    ['90', 'excl', 'выкл', 'говорящий не включён в действие', 'INvl', None],

    ['91', 'VOic', 'Залог', 'категория залога', '—', None],
    ['92', 'actv', 'действ', 'действительный залог', 'VOic', 'дст'],
    ['93', 'pssv', 'страд', 'страдательный залог', 'VOic', 'стр'],

    ['94', 'Infr', 'разг', 'разговорное', '—', 'разг'],
    ['95', 'Slng', 'жарг', 'жаргонное', '—', 'жарг'],
    ['96', 'Arch', 'арх', 'устаревшее', '—', 'арх'],
    ['97', 'Litr', 'лит', 'литературный вариант', '—', None],
    ['98', 'Erro', 'опеч', 'опечатка', '—', None],
    ['99', 'Dist', 'искаж', 'искажение', '—', None],
    ['100', 'Ques', 'вопр', 'вопросительное', '—', 'вопр'],
    ['101', 'Dmns', 'указ', 'указательное', '—', 'указат'],
    ['103', 'Prnt', 'вводн', 'вводное слово', '—', None], # fixme: ВВОДН
    ['104', 'V-be', '*ье', 'форма на -ье', '—', None],
    ['105', 'V-en', '*енен', 'форма на -енен', '—', None],
    ['106', 'V-ie', '*ие', 'отчество через -ие-', '—', None],
    ['107', 'V-bi', '*ьи', 'форма на -ьи', '—', None],
    ['108', 'Fimp', '*несов', 'деепричастие от глагола несовершенного вида', '—', None], # fixme: aot
    ['109', 'Prdx', 'предк?', 'может выступать в роли предикатива', '—', None], # fixme: aot
    ['110', 'Coun', 'счетн', 'счётная форма', '—', None],
    ['111', 'Coll', 'собир', 'собирательное числительное', '—', None],
    ['112', 'V-sh', '*ши', 'деепричастие на -ши', '—', None],
    ['113', 'Af-p', '*предл', 'форма после предлога', '—', None],
    ['114', 'Inmx', 'неодуш?', 'может использоваться как неодушевлённое', '—', None],
    ['115', 'Vpre', 'в_предл', 'Вариант предлога ( со, подо, ...)',	'—', None],
    ['116', 'Anph', 'Анаф', 'Анафорическое (местоимение)', '-', None],
    ['117', 'Init', 'иниц', 'Инициал', '-', None],
]

INTERNAL_TO_EXTERNAL = dict((item[1], item[2]) for item in GRAM_TABLE)
EXTERNAL_TO_INTERNAL = invert_mapping(INTERNAL_TO_EXTERNAL)

EXTERNAL_TO_AOT = dict((item[2], item[5]) for item in GRAM_TABLE
                        if item[5] is not None)

def _translate_comma_separated(tag_part, mapping):
    return ",".join([mapping.get(tok, tok).strip() for tok in tag_part.split(',')])

def _translate_tag(tag, mapping):
    return " ".join([
        _translate_comma_separated(part, mapping)
        for part in tag.split()
    ])


def external_to_internal(external_tag, word=None):
    return _translate_tag(external_tag, EXTERNAL_TO_INTERNAL)

def internal_to_external(internal_tag, word=None):
    return _translate_tag(internal_tag, INTERNAL_TO_EXTERNAL)


def to_aot(open_tag, word=None):
    open_tags = open_tag.replace(" ", ',').split(',')
    open_pos, open_info = open_tags[0], open_tags[1:]

    pos = EXTERNAL_TO_AOT.get(open_pos, None)
    info = [EXTERNAL_TO_AOT.get(tag, None) for tag in open_info]
    info = [tag for tag in info if tag is not None]

    if open_pos == 'ПРИЛ':
        if 'мест-п' in open_info:
            pos = 'МС-П'
        elif 'числ-п' in open_info:
            pos = 'ЧИСЛ-П'

    if 'пвл' in info:
        info.append('2л')

    if not pos:
        return ''
    return ','.join([pos] + info)


converters.add('opencorpora-int', 'opencorpora-ext', internal_to_external)
converters.add('opencorpora-ext', 'opencorpora-int', external_to_internal)
converters.add('opencorpora-ext', 'aot', to_aot)
