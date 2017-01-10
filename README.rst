===============
russian-tagsets
===============

.. image:: https://img.shields.io/pypi/v/russian-tagsets.svg
    :target: https://pypi.python.org/pypi/russian-tagsets

.. image:: https://img.shields.io/pypi/l/russian-tagsets.svg

.. image:: https://img.shields.io/travis/kmike/russian-tagsets.svg
    :target: https://travis-ci.org/kmike/russian-tagsets


``russian-tagsets`` - библиотека для преобразования между
различными форматами обозначения грамматической информации
для слов русского языка. Лицензия - MIT.

На данный момент поддерживается (с разной степенью корректности)
преобразование между следующими форматами:

* `OpenCorpora`_ (в.т.ч. русские словари pymorphy2_);
* `aot.ru`_ (в.т.ч. pymorphy_ 0.5.6);
* `Диалог-2010`_;
* `A Positional Tagset for Russian`_ (Jirka Hana and Anna Feldman, 2010);
* `НКРЯ`_;
* `Universal Dependencies`_ (v1.4);

.. _OpenCorpora: http://opencorpora.org/dict.php?act=gram
.. _aot.ru: http://aot.ru/docs/rusmorph.html
.. _pymorphy: https://pymorphy.readthedocs.io/en/v0.5.6/ref/gram_info_ru.html
.. _pymorphy2: https://github.com/kmike/pymorphy2
.. _Диалог-2010: http://ru-eval.ru/
.. _A Positional Tagset for Russian: http://ufal.mff.cuni.cz/~hana/morph/rutags.html
.. _НКРЯ: http://www.ruscorpora.ru/corpora-morph.html
.. _Universal Dependencies: http://universaldependencies.org/ru/pos/all.html

Идея такая: для каждого формата в библиотеке определяется
несколько функций, которые преобразуют тег в другие форматы;
если какое-то преобразование явным образом не определено,
``russian-tagsets`` пытается построить цепочку преобразований,
приводящую к нужному результату.

.. warning::

    Преобразование почти никогда не выходит осуществить без потерь;
    если можно эту библиотеку не использовать, то лучше и не использовать.

Установка
=========

pip install russian-tagsets

Использование
=============

"Автоматический" режим (библиотека пытается найти пути преобразования)::

    >>> from russian_tagsets import converters
    >>> to_aot = converters.converter('opencorpora-int', 'aot')
    >>> to_aot("NOUN,anim,masc plur,nomn")
    С,од,мр,мн,им

Поддерживаемые напрямую форматы::

    >>> converters.get_supported()
    [(u'positional', u'aot'),
     (u'opencorpora-ext', u'opencorpora-int'),
     (u'opencorpora-ext', u'aot'),
     (u'aot', u'positional'),
     (u'aot', u'dialog2010'),
     (u'dialog2010', u'aot'),
     (u'opencorpora-int', u'ruscorpora'),
     (u'opencorpora-int', u'opencorpora-ext'),
     (u'opencorpora-int', u'ud14')]

"Ручной" режим (быстрее, преобразование только напрямую)::

    >>> import russian_tagsets
    >>> russian_tagsets.aot.to_positional(u"С,од,мр,мн,им")
    Tag("NNMAP1-------A--")

Разработка
==========

* Исходный код: https://github.com/kmike/russian-tagsets
* Баг-трекер: https://github.com/kmike/russian-tagsets/issues

Для запуска тестов выполните

    tox

из папки с репозиторием.
