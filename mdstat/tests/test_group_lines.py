# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from ..utils import group_lines


class TestGroupLines(unittest.TestCase):

    def test_empty(self):
        lines = []
        expected = []
        groups = group_lines(lines)
        self.assertEquals(groups, expected)

    def test_one(self):
        lines = ["foo", "bar"]
        expected = [["foo", "bar"]]
        groups = group_lines(lines)
        self.assertEquals(groups, expected)

    def test_many(self):
        lines = ["foo bar", "", "qux", "baz"]
        expected = [["foo bar"], ["qux", "baz"]]
        groups = group_lines(lines)
        self.assertEquals(groups, expected)
