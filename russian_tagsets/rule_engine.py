# -*- coding: utf-8 -*-
"""
A simple rewriting rules engine.
"""
from __future__ import absolute_import


def _parse_rule(rule):
    """ Parse a single rule. """
    left_txt, right_txt = rule.split(' => ')

    left = left_txt.split(',')
    right = ['_' + t for t in right_txt.split(',')]

    return left, right

def parse(rules_text):
    """ Convert rules text to a list of rules. """
    return [_parse_rule(r)
            for r in rules_text.splitlines()
            if r and not r.startswith('#')]


def apply_rules(parsed_rules, tag, remove_untouched=True):
    """
    Transform ``tag`` according to ``parsed_rules``.
    If ``remove_untouched`` is true the grammemes that
    were not converted are removed.
    """

    grammemes = set(tag)

    for from_, to_ in parsed_rules:
        from_set = set(from_)

        if not from_set <= grammemes:
            # rule doesn't apply
            continue

        #print('rule:', from_, '=>', to_)

        last_index = None
        for gr_from, gr_to in zip(from_, to_):
            for idx, gr in enumerate(tag):
                if gr == gr_from:
                    tag[idx] = gr_to
                    last_index = idx

        if len(from_) > len(to_):
            for gr in from_[len(to_):]:
                tag.remove(gr)

        if len(from_) < len(to_):
            tag = tag[:last_index+1] + to_[len(from_):] + tag[last_index+1:]

        grammemes -= from_set
        #print('res: ', tag)

    return [g.lstrip('_') for g in tag
            if not remove_untouched or g not in grammemes]
