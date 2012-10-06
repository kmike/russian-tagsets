===============
russian-tagsets
===============

``russian-tagsets`` - библиотека для преобразования между
различными форматами обозначения грамматической информации
для слов русского языка. Лицензия - MIT.

На данный момент поддерживается (с разной степенью корректности)
преобразование между следующими форматами:

* `OpenCorpora`_;
* `aot.ru`_ (в.т.ч. pymorphy_ 0.5.6);
* `Диалог-2010`_
* `A Positional Tagset for Russian`_ (Jirka Hana and Anna Feldman, 2010);

.. _OpenCorpora: http://opencorpora.org/dict.php?act=gram
.. _aot.ru: http://aot.ru/docs/rusmorph.html
.. _pymorphy: http://pymorphy.readthedocs.org/en/v0.5.6/ref/gram_info_ru.html
.. _Диалог-2010: http://ru-eval.ru/
.. _A Positional Tagset for Russian: http://ufal.mff.cuni.cz/~hana/morph/rutags.html

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
     (u'opencorpora', u'opencorpora-int'),
     (u'opencorpora', u'aot'),
     (u'aot', u'positional'),
     (u'aot', u'dialog2010'),
     (u'dialog2010', u'aot'),
     (u'opencorpora-int', u'opencorpora')]

"Ручной" режим (быстрее, но преобразование только напрямую)::

    >>> import russian_tagsets
    >>> russian_tagsets.aot.to_positional(u"С,од,мр,мн,им")
    Tag("NNMAP1-------A--")


Разработка
==========

Репозитории:

* https://github.com/kmike/russian-tagsets
* https://bitbucket.org/kmike/russian-tagsets

Баг-трекер - на гитхабе.

Для запуска тестов выполните

    tox

из папки с репозиторием.
